# fastapi-demo

学生成绩管理系统后端项目，基于 FastAPI + MySQL + SQLAlchemy ORM 开发。

完整项目说明请查看根目录 `README.md`。

## 技术栈

- FastAPI
- SQLAlchemy ORM
- MySQL
- Pydantic
- JWT
- Uvicorn
- pytest

## 主要功能

- 查询学生列表
- 查询单个学生
- 新增学生成绩
- 修改学生成绩
- 删除学生
- 成绩统计
- 用户注册
- 用户登录
- JWT token 鉴权
- admin / viewer 角色权限控制
- 参数校验与错误处理

## 环境变量

复制 `.env.example` 为 `.env`：

```powershell
copy .env.example .env
```

配置数据库连接和 JWT 密钥：

```env
DATABASE_URL=mysql+pymysql://fastapi_user:your_password@127.0.0.1:3306/fastapi_demo?charset=utf8mb4
SECRET_KEY=change-this-secret-key
```

说明：

- `.env` 保存本机真实配置，不应提交到 Git
- `DATABASE_URL` 用于连接 MySQL
- `SECRET_KEY` 用于生成和校验 JWT token

## 安装依赖

进入后端目录：

```powershell
cd E:\vscodeprogram\student-management-system\fastapi-demo
```

安装依赖：

```powershell
pip install -r requirements.txt
```

## 启动服务

```powershell
python -m uvicorn main:app --reload
```

接口文档地址：

```text
http://127.0.0.1:8000/docs
```

## 主要接口

| 方法 | 路径 | 说明 | 权限 |
| --- | --- | --- | --- |
| GET | `/students` | 查询学生列表 | 公开 |
| GET | `/students/{name}` | 查询单个学生 | 公开 |
| POST | `/students` | 新增学生 | admin |
| PUT | `/students/{name}` | 修改学生成绩 | admin |
| DELETE | `/students/{name}` | 删除学生 | admin |
| GET | `/stats` | 查询成绩统计 | 公开 |
| POST | `/auth/register` | 用户注册 | 公开 |
| POST | `/auth/login` | 用户登录并获取 token | 公开 |

## 鉴权说明

登录成功后，后端返回 JWT token。

访问需要权限的接口时，请求头需要携带：

```text
Authorization: Bearer <token>
```

状态码说明：

- `401`：未登录或 token 无效
- `403`：已登录但角色权限不足
- `422`：请求参数不符合 Pydantic 校验规则

## 运行测试

```powershell
python -m pytest test_main.py
```

