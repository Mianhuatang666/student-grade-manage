
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from schemas import Student, StudentPage, UpdateScore, UserRegister, UserLogin, TokenResponse, StudentWithClassResponse,ClassResponse
from auth import hash_password, verify_password, create_access_token, decode_access_token
from services import calculate_stats
from storage import (
    get_all_students,
    get_student,
    create_student,
    update_student_score,
    delete_student_by_name,
    get_user_by_username,
    create_user,
    get_students_with_class,
    get_all_classes
)


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    token_data = decode_access_token(token)

    if token_data is None:
        raise HTTPException(status_code=401, detail="未登录或登录已过期")

    username = token_data["username"]

    user = get_user_by_username(username)

    if user is None:
        raise HTTPException(status_code=401, detail="用户不存在")

    return user


def require_admin(current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="权限不足，只有管理员可以操作")

    return current_user

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "学生成绩管理系统"}

@app.get("/students")
def get_students():
    return get_all_students()

@app.get("/students/{name}")
def get_student_api(name: str):
    student = get_student(name)

    if student is None:
        raise HTTPException(status_code=404,detail="学生不存在")

    return student

@app.post("/students")
def add_student(student: Student, current_user = Depends(require_admin)):
    old_student = get_student(student.name)

    if old_student is not None:
        raise HTTPException(status_code=400, detail="学生已存在")

    create_student(student.name, student.score, student.class_id)

    return{
        "message": "添加成功",
        "name": student.name,
        "score": student.score,
        "class_id": student.class_id
    }

@app.post("/auth/register")
def register(user: UserRegister):
    old_user = get_user_by_username(user.username)

    if old_user is not None:
        raise HTTPException(status_code=400, detail="用户名已存在")

    password_hash = hash_password(user.password)
    create_user(user.username, password_hash)

    return {
        "message": "注册成功",
        "username": user.username
    }

@app.post("/auth/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = get_user_by_username(form_data.username)

    if db_user is None:
        raise HTTPException(status_code=401, detail="用户名或密码错误")

    if not verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="用户名或密码错误")

    token = create_access_token({
        "sub": db_user.username,
        "role": db_user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.put("/students/{name}")
def update_student(name: str, data: UpdateScore, current_user = Depends(require_admin)):
    row_count = update_student_score(name, data.score)

    if row_count == 0:
        raise HTTPException(status_code=404, detail="学生不存在")

    return {
        "message": "修改成功",
        "name": name,
        "score": data.score
    }

@app.delete("/students/{name}")
def delete_student(name: str, current_user=Depends(require_admin)):
    old_student = get_student(name)

    if old_student is None:
        raise HTTPException(status_code=404, detail="学生不存在")

    row_count = delete_student_by_name(name)

    if row_count == 0:
        raise HTTPException(status_code=404, detail="学生不存在")

    return {
        "message": "删除成功",
        "name": name,
        "score": old_student["score"]
    }

@app.get("/stats")
def get_stats():
    students = get_all_students()
    stats = calculate_stats(students)

    if stats is None:
        raise HTTPException(status_code=404, detail="暂无学生，无法统计")

    return stats

@app.get("/students-with-class", response_model=StudentPage)
def read_students_with_class(
    class_id: int | None = None,
    keyword: str | None = None,
    page: int = 1,
    page_size: int = 10
):
    return get_students_with_class(class_id, keyword, page, page_size)

@app.get("/classes", response_model=list[ClassResponse])
def read_classes():
    return get_all_classes()
