# 学生成绩管理系统后端

本项目是一个基于 FastAPI 的学生成绩管理系统后端服务，提供学生成绩管理、成绩统计、用户注册登录、JWT 鉴权等接口能力。项目使用 MySQL 作为数据存储，SQLAlchemy ORM 负责数据库操作，并使用 pytest 编写接口测试。

## 技术栈

- Python
- FastAPI
- MySQL
- SQLAlchemy ORM
- Pydantic
- JWT
- pytest
- Uvicorn
- Git

## 功能列表

- 查询学生列表
- 查询指定学生
- 新增学生成绩
- 修改学生成绩
- 删除学生
- 统计平均分、最高分、最低分
- 用户注册
- 用户登录
- JWT Token 鉴权
- 未登录用户禁止访问受保护接口
- pytest 自动化接口测试

## 项目结构

```text
fastapi-demo
├── main.py              # FastAPI 接口入口
├── database.py          # 数据库连接配置
├── models.py            # SQLAlchemy ORM 数据模型
├── schemas.py           # Pydantic 请求和响应模型
├── storage.py           # 学生数据增删改查逻辑
├── services.py          # 业务逻辑封装
├── auth.py              # 密码加密、登录校验、JWT 生成与解析
├── test_main.py         # pytest 接口测试
├── requirements.txt     # Python 依赖
├── .env.example         # 环境变量示例
└── .gitignore           # Git 忽略配置
```

## 环境变量

项目通过 `.env` 文件读取数据库连接和 JWT 密钥配置。

先复制 `.env.example` 为 `.env`，再根据本机 MySQL 修改配置：

```env
DATABASE_URL=mysql+pymysql://fastapi_user:your_password@127.0.0.1:3306/fastapi_demo?charset=utf8mb4
SECRET_KEY=change-me
```

说明：

- `DATABASE_URL`：MySQL 数据库连接地址
- `SECRET_KEY`：JWT token 签名密钥
- `.env` 中包含本机真实密码，不应提交到 Git

## 安装依赖

```powershell
cd E:\vscodeprogram\fastapi-demo
pip install -r requirements.txt
```

## 启动服务

```powershell
uvicorn main:app --reload
```

启动后访问：

```text
http://127.0.0.1:8000/docs
```

可以打开 FastAPI 自动生成的接口文档。

## 主要接口

| 方法 | 路径 | 说明 | 是否需要登录 |
|---|---|---|---|
| GET | `/students` | 查询学生列表 | 否 |
| GET | `/students/{name}` | 查询指定学生 | 否 |
| POST | `/students` | 新增学生 | 是 |
| PUT | `/students/{name}` | 修改学生成绩 | 是 |
| DELETE | `/students/{name}` | 删除学生 | 是 |
| GET | `/stats` | 查询成绩统计 | 否 |
| POST | `/auth/register` | 用户注册 | 否 |
| POST | `/auth/login` | 用户登录并获取 token | 否 |

## 登录与鉴权流程

用户登录时，前端向 `/auth/login` 提交用户名和密码。后端根据用户名查询用户记录，并使用密码哈希校验用户输入的密码。校验成功后，后端生成 JWT token 返回给前端。

访问新增、修改、删除学生等受保护接口时，请求头需要携带：

```text
Authorization: Bearer <token>
```

后端通过 `get_current_user` 解析并验证 token。验证通过后才允许继续执行数据库操作；验证失败则返回 `401 Unauthorized`。

## 运行测试

```powershell
pytest test_main.py
```

测试内容包括：

- 学生增删改查
- 成绩统计
- 参数校验
- 用户注册
- 用户登录
- JWT 鉴权
- 未登录访问拦截

## 项目亮点

- 使用 FastAPI 构建 RESTful API
- 使用 Pydantic 定义请求和响应数据模型
- 使用 SQLAlchemy ORM 操作 MySQL 数据库
- 使用 JWT 实现登录鉴权
- 对新增、修改、删除等写操作进行权限保护
- 使用 pytest 覆盖核心接口测试
- 通过分层结构拆分接口层、数据模型层、数据库操作层和鉴权逻辑
