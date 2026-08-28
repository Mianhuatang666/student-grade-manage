from main import app
from services import calculate_stats
from fastapi.testclient import TestClient
from sqlalchemy import text
from database import engine

import pytest

@pytest.fixture(autouse=True)
def clean_tables():
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM students"))
        conn.execute(text("DELETE FROM users"))

    yield

    with engine.begin() as conn:
        conn.execute(text("DELETE FROM students"))
        conn.execute(text("DELETE FROM users"))


client = TestClient(app)


@pytest.fixture
def auth_headers():
    client.post(
        "/auth/register",
        json={
            "username": "admin",
            "password": "123456"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "123456"
        }
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }

def test_calculate_stats():
    students = {
        "张三": 80,
        "李四": 90
    }

    result = calculate_stats(students)

    assert result["average"] == 85
    assert result["max_score"] == 90
    assert result["max_student"] == "李四"
    assert result["min_score"] == 80
    assert result["min_student"] == "张三"


def test_calculate_stats_empty():
    result = calculate_stats({})

    assert result is None

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "学生成绩管理系统"}

def test_get_students():
    response = client.get("/students")

    assert response.status_code == 200

def test_student_crud_flow(auth_headers):
    response = client.post(
        "/students",
        headers=auth_headers,
        json={
            "name": "wangwu",
            "score": 92
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "添加成功"

    response = client.get("/students/wangwu")

    assert response.status_code == 200
    assert response.json()["name"] == "wangwu"
    assert response.json()["score"] == 92

    response = client.put(
        "/students/wangwu",
        headers=auth_headers,
        json={
            "score": 95
        }
    )

    assert response.status_code == 200
    assert response.json()["score"] == 95

    response = client.delete("/students/wangwu", headers=auth_headers)

    assert response.status_code ==200
    assert response.json()["message"] == "删除成功"

    response = client.get("/students/wangwu")

    assert response.status_code == 404

def test_add_students_invaild_score(auth_headers):
    response = client.post(
        "/students",
        headers=auth_headers,
        json={
            "name": "bad_score",
            "score": 999
        }
    )

    assert response.status_code == 422


def test_add_student_empty_name(auth_headers):
    response = client.post(
        "/students",
        headers=auth_headers,
        json={
            "name": "   ",
            "score": 80
        }
    )

    assert response.status_code == 422


def test_add_student_requires_login():
    response = client.post(
        "/students",
        json={
            "name": "no_login",
            "score": 80
        }
    )

    assert response.status_code == 401


def test_login_wrong_password():
    client.post(
        "/auth/register",
        json={
            "username": "admin",
            "password": "123456"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "wrong-password"
        }
    )

    assert response.status_code == 401
