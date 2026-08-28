# 学生成绩管理系统

本项目是一个前后端分离的学生成绩管理系统，包含 FastAPI 后端和 Vue3 前端。系统支持学生成绩增删改查、成绩统计、用户注册登录、JWT 鉴权、路由守卫、请求 loading 和错误提示等功能。

## 项目组成

```text
student-grade-manage
├── fastapi-demo     # FastAPI 后端
└── student-web      # Vue3 前端
```

## 技术栈

后端：

- Python
- FastAPI
- MySQL
- SQLAlchemy ORM
- Pydantic
- JWT
- pytest

前端：

- Vue3
- Vite
- TypeScript
- Vue Router
- Pinia
- Fetch API

## 功能

- 用户注册
- 用户登录
- JWT 登录鉴权
- 学生列表查询
- 学生成绩新增
- 学生成绩修改
- 学生删除
- 成绩统计
- 前端路由守卫
- token 失效自动跳转登录页
- 请求 loading 和错误提示

## 启动步骤

### 1. 启动后端

```powershell
cd fastapi-demo
pip install -r requirements.txt
```

复制 `.env.example` 为 `.env`，并根据本机 MySQL 修改配置：

```env
DATABASE_URL=mysql+pymysql://fastapi_user:your_password@127.0.0.1:3306/fastapi_demo?charset=utf8mb4
SECRET_KEY=change-me
```

启动服务：

```powershell
uvicorn main:app --reload
```

后端接口文档：

```text
http://127.0.0.1:8000/docs
```

### 2. 启动前端

```powershell
cd student-web
npm install
npm run dev
```

前端访问地址：

```text
http://localhost:5173
```

## 测试

后端测试：

```powershell
cd fastapi-demo
python -m pytest test_main.py
```

前端构建：

```powershell
cd student-web
npm run build
```

## 登录说明

可以通过后端接口注册用户：

```text
POST /auth/register
```

示例请求：

```json
{
  "username": "admin",
  "password": "123456"
}
```

登录后，后端返回 JWT token。前端保存 token，并在新增、修改、删除学生时自动携带：

```text
Authorization: Bearer <token>
```

## 项目亮点

- 前后端分离架构
- FastAPI 构建 RESTful API
- SQLAlchemy ORM 操作 MySQL
- JWT 实现登录鉴权
- Vue Router 实现页面切换和路由守卫
- Pinia 统一管理登录状态
- request.js 统一封装请求和 401 错误处理
- pytest 覆盖核心后端接口
