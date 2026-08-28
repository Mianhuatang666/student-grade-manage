# 学生成绩管理系统

本项目是一个前后端分离的学生成绩管理系统，包含 FastAPI 后端和 Vue3 前端。系统支持学生成绩增删改查、成绩统计、用户注册登录、JWT 鉴权、路由守卫、请求 loading 和错误提示等功能。

## 项目组成

```text
student-management-system
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

## 启动后端

```powershell
cd fastapi-demo
pip install -r requirements.txt
uvicorn main:app --reload
```

后端接口文档：

```text
http://127.0.0.1:8000/docs
```

## 启动前端

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

## 配置说明

后端复制 `.env.example` 为 `.env`，配置 MySQL 地址和 JWT 密钥。

前端复制 `.env.example` 为 `.env`，配置后端接口地址：

```env
VITE_API_BASE=http://127.0.0.1:8000
```