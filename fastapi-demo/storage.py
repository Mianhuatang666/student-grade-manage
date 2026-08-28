
from sqlalchemy import select
from database import SessionLocal
from models import StudentModel, UserModel, ClassModel



def get_all_students():
    with SessionLocal() as session:
        stmt = select(StudentModel)
        result = session.execute(stmt)
        students_list = result.scalars().all()

        students = {}

        for student in students_list:
            students[student.name] = student.score

        return students


def get_student(name):
    with SessionLocal() as session:
        stmt = select(StudentModel).where(StudentModel.name == name)
        result = session.execute(stmt)
        student = result.scalar_one_or_none()

        if student is None:
            return None

        return {
            "name": student.name,
            "score": student.score
        }


def create_student(name,score,class_id):
    with SessionLocal() as session:
        student = StudentModel(name=name, score=score, class_id=class_id)

        session.add(student)
        session.commit()


def update_student_score(name, score):
    with SessionLocal() as session:
        stmt = select(StudentModel).where(StudentModel.name == name)
        result = session.execute(stmt)
        student = result.scalar_one_or_none()

        if student is None:
            return 0

        student.score = score
        session.commit()

        return 1

def delete_student_by_name(name):
    with SessionLocal() as session:
        stmt = select(StudentModel).where(StudentModel.name == name)
        result = session.execute(stmt)
        student = result.scalar_one_or_none()

        if student is None:
            return 0

        session.delete(student)
        session.commit()

        return 1



def get_user_by_username(username):
    with SessionLocal() as session:
        stmt = select(UserModel).where(UserModel.username == username)
        result = session.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            return None

        return user


def create_user(username, password_hash):
    with SessionLocal() as session:
        user = UserModel(username=username, password_hash=password_hash)

        session.add(user)
        session.commit()

def get_students_with_class():
    db = SessionLocal()

    try:
        students = db.query(StudentModel).all()

        result = []

        for student in students:
            class_name = None

            if student.class_info is not None:
                class_name = student.class_info.name

            result.append({
                "name": student.name,
                "score": student.score,
                "class_name": class_name
            })
        return result

    finally:
        db.close()

def get_all_classes():
    db = SessionLocal()

    try:
        classes = db.query(ClassModel).all()

        result = []

        for class_obj in classes:
            result.append({
                "id": class_obj.id,
                "name": class_obj.name
            })

        return result

    finally:
        db.close()