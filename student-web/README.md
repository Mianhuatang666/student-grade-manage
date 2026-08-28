# 学生成绩管理系统前端

本项目是学生成绩管理系统的前端部分，基于 Vue3 和 Vite 开发，实现学生成绩展示、新增、修改、删除、统计展示、用户登录、路由守卫和登录状态管理等功能。前端通过 HTTP API 与 FastAPI 后端交互。

## 技术栈

- Vue3
- Vite
- TypeScript
- Vue Router
- Pinia
- Fetch API
- HTML / CSS
- Git

## 功能列表

- 首页展示
- 用户登录
- 退出登录
- 登录状态保存
- 路由守卫保护学生管理页
- 学生列表自动加载
- 新增学生成绩
- 修改学生成绩
- 删除学生
- 成绩统计展示
- 请求 loading 状态
- 表单错误提示
- token 失效后自动跳转登录页

## 项目结构

```text
student-web
├── src
│   ├── api
│   │   ├── request.js        # 统一请求封装，自动携带 token，统一处理 401
│   │   └── students.ts       # 学生、统计、登录相关接口
│   ├── components
│   │   ├── StudentForm.vue   # 学生新增表单
│   │   ├── StudentList.vue   # 学生列表、修改、删除
│   │   └── StatsPanel.vue    # 成绩统计展示
│   ├── router
│   │   └── index.js          # 页面路由和登录守卫
│   ├── stores
│   │   └── authStore.js      # Pinia 登录状态管理
│   ├── types
│   │   └── index.ts          # TypeScript 类型定义
│   ├── views
│   │   ├── HomeView.vue      # 首页
│   │   ├── LoginView.vue     # 登录页
│   │   └── StudentView.vue   # 学生管理页
│   ├── App.vue
│   └── main.js
├── package.json
└── README.md
```

## 安装依赖

```powershell
cd E:\vscodeprogram\student-web
npm install
```

## 启动前端

```powershell
npm run dev
```

启动后访问：

```text
http://localhost:5173
```

## 后端依赖

前端需要配合 FastAPI 后端运行。

后端地址默认配置为：

```text
http://127.0.0.1:8000
```

如需修改后端地址，可以复制 `.env.example` 为 `.env`，并修改：

```env
VITE_API_BASE=http://127.0.0.1:8000
```

启动后端：

```powershell
cd E:\vscodeprogram\fastapi-demo
uvicorn main:app --reload
```

## 登录与鉴权流程

用户在登录页输入账号密码后，前端调用后端 `/auth/login` 接口。登录成功后，后端返回 JWT token，前端通过 Pinia 的 `authStore` 保存 token，并同步存入 `localStorage`。

访问新增、修改、删除学生等受保护接口时，前端会在请求头中自动携带：

```text
Authorization: Bearer <token>
```

如果后端返回 `401 Unauthorized`，统一请求函数会自动清空 token，并跳转到登录页。

## 状态管理

项目使用 Pinia 管理登录状态。

`authStore` 主要负责：

- 保存 token
- 清空 token
- 判断是否已登录
- 从 localStorage 恢复登录状态

## 请求封装

项目通过 `api/request.js` 统一封装请求逻辑：

- 自动携带 Authorization token
- 统一处理 401 登录失效
- 减少重复代码

## 页面交互优化

项目实现了基础的用户体验优化：

- 添加学生时显示添加中状态
- 加载学生列表时显示加载中状态
- 修改、删除时只禁用当前操作的学生按钮
- 表单错误使用页面提示，不使用浏览器弹窗
- 请求失败时显示错误信息

## 构建项目

```powershell
npm run build
```

构建成功后会生成：

```text
dist
```

## 项目亮点

- 使用 Vue3 Composition API 组织页面逻辑
- 使用组件拆分实现表单、列表、统计模块复用
- 使用 props 和 emit 实现父子组件通信
- 使用 Vue Router 实现页面切换和登录守卫
- 使用 Pinia 统一管理登录状态
- 使用统一请求封装处理 token 和 401 错误
- 与 FastAPI 后端完成前后端分离联调
