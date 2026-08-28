# 学生成绩管理系统

本项目是一个前后端分离的学生成绩管理系统，支持学生成绩增删改查、成绩统计、用户注册登录、JWT 登录鉴权、角色权限控制、前端路由守卫、统一请求封装和统一错误提示。

项目用于学习和实践 FastAPI + Vue3 全栈开发流程，覆盖了后端接口设计、数据库持久化、前端组件化、登录状态管理、权限控制和项目配置规范等内容。

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

- Vue 3
- TypeScript
- Vite
- Vue Router
- Pinia
- Fetch API

## 功能说明

- 用户注册与登录
- JWT token 鉴权
- 学生列表查询
- 学生成绩新增、修改、删除
- 成绩统计，包括平均分、最高分、最低分
- 基于角色的权限控制
- 前端路由守卫
- 前端根据角色隐藏无权限操作按钮
- 统一请求封装
- 统一错误信息解析
- loading 状态与防重复提交

## 权限说明

系统包含两类角色：

- `admin`：可以查看、新增、修改、删除学生成绩
- `viewer`：只能查看学生列表和成绩统计，不能执行新增、修改、删除

后端对新增、修改、删除接口进行权限校验：

- 未登录或 token 无效：返回 `401`
- 已登录但权限不足：返回 `403`

前端会根据当前用户 token 中的角色信息控制页面显示：

- `admin` 显示添加、修改、删除功能
- `viewer` 隐藏添加、修改、删除功能

## 项目结构

```text
student-management-system
├── fastapi-demo          # FastAPI 后端项目
│   ├── main.py           # 接口入口
│   ├── database.py       # 数据库连接配置
│   ├── models.py         # SQLAlchemy ORM 模型
│   ├── schemas.py        # Pydantic 请求/响应模型
│   ├── storage.py        # 数据库操作层
│   ├── services.py       # 业务逻辑层
│   ├── auth.py           # 密码加密与 JWT 鉴权
│   ├── test_main.py      # 后端接口测试
│   ├── requirements.txt  # 后端依赖
│   └── .env.example      # 后端环境变量示例
│
├── student-web           # Vue3 前端项目
│   ├── src
│   │   ├── api           # 请求封装
│   │   ├── components    # 页面组件
│   │   ├── router        # 前端路由
│   │   ├── stores        # Pinia 状态管理
│   │   ├── types         # TypeScript 类型定义
│   │   └── views         # 页面视图
│   ├── package.json      # 前端依赖与脚本
│   └── .env.example      # 前端环境变量示例
│
├── .gitignore
└── README.md
```

## 环境要求

- Python 3.11+
- Node.js 18+
- MySQL 8.0+
- Git

建议使用 Python 官方环境和 `venv` 虚拟环境。

## 后端配置

进入后端目录：

```powershell
cd fastapi-demo
```

复制环境变量示例文件：

```powershell
copy .env.example .env
```

然后在 `.env` 中配置数据库连接和 JWT 密钥：

```env
DATABASE_URL=mysql+pymysql://fastapi_user:your_password@127.0.0.1:3306/fastapi_demo?charset=utf8mb4
SECRET_KEY=change-this-secret-key
```

说明：

- `.env` 保存真实配置，不应提交到 Git
- `.env.example` 是示例模板，可以提交到 Git
- `DATABASE_URL` 用于连接 MySQL
- `SECRET_KEY` 用于生成和校验 JWT token

## 后端启动

安装依赖：

```powershell
pip install -r requirements.txt
```

启动开发服务：

```powershell
python -m uvicorn main:app --reload
```

后端接口文档：

```text
http://127.0.0.1:8000/docs
```

## 前端配置

进入前端目录：

```powershell
cd student-web
```

复制环境变量示例文件：

```powershell
copy .env.example .env
```

前端 `.env` 示例：

```env
VITE_API_BASE=http://127.0.0.1:8000
```

说明：

- 前端环境变量必须以 `VITE_` 开头，才能在 Vite 项目中通过 `import.meta.env` 读取
- `VITE_API_BASE` 表示后端接口地址

## 前端启动

安装依赖：

```powershell
npm install
```

启动开发服务：

```powershell
npm run dev
```

前端访问地址：

```text
http://localhost:5173
```

## 生产打包

前端打包：

```powershell
npm run build
```

打包产物会生成到：

```text
student-web/dist
```

本地预览打包结果：

```powershell
npm run preview
```

## 后端测试

在后端目录运行：

```powershell
python -m pytest test_main.py
```

## Git 提交注意事项

以下文件或目录不应提交：

```text
.env
node_modules/
dist/
__pycache__/
.pytest_cache/
```

提交前建议检查：

```powershell
git status
```

## 常见状态码

- `200`：请求成功
- `400`：业务请求错误，例如学生已存在
- `401`：未登录或 token 无效
- `403`：已登录但权限不足
- `404`：资源不存在
- `422`：请求参数格式不符合后端校验规则

