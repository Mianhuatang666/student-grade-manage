
"""
FILE_NAME = "students.txt"


def load_students():
    result = {}

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                name, score_text = line.split(",")
                result[name] = int(score_text)
    except FileNotFoundError:
        pass

    return result


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for name, score in students.items():
            file.write(f"{name},{score}\n")
"""



"""
from sqlalchemy import text
from database import engine
"""
from sqlalchemy import select
from database import SessionLocal
from models import StudentModel, UserModel


"""
def get_all_students():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT name, score FROM students"))

        students = {}

        for row in result:
            students[row.name] = row.score

        return students
"""

def get_all_students():
    with SessionLocal() as session:
        stmt = select(StudentModel)
        result = session.execute(stmt)
        students_list = result.scalars().all()

        students = {}

        for student in students_list:
            students[student.name] = student.score

        return students

"""
def get_student(name):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT name, score FROM students WHERE name =:name"),
            {"name": name}
        )

        row = result.fetchone()

        if row is None:
            return None

        return {
            "name": row.name,
            "score": row.score
        }
"""

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
'''
def create_student(name,score):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO students (name,score) VALUES (:name, :score)"),
            {
                "name": name,
                "score": score
            }
        )
'''   

def create_student(name,score):
    with SessionLocal() as session:
        student = StudentModel(name=name, score=score)

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


'''
def update_student_score(name, score):
    with engine.begin() as conn:
        result = conn.execute(
            text("UPDATE students SET score = :score WHERE name = :name"),
            {
                "name": name,
                "score": score
            }
        )

        return result.rowcount

def delete_student_by_name(name):
    with engine.begin() as conn:
        result = conn.execute(
            text("DELETE FROM students WHERE name = :name"),
            {"name": name}
        )

        return result.rowcount
'''

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