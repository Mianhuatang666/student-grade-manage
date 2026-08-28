# student-web

学生成绩管理系统前端项目，基于 Vue 3 + TypeScript + Vite 开发。

完整项目说明请查看根目录 `README.md`。

## 技术栈

- Vue 3
- TypeScript
- Vite
- Vue Router
- Pinia
- Fetch API
- jwt-decode

## 主要功能

- 用户登录与退出登录
- 登录状态保存
- 路由守卫
- 学生列表展示
- 学生成绩新增、修改、删除
- 成绩统计展示
- 根据角色控制操作按钮显示
- 统一请求封装
- 统一错误提示
- loading 状态与防重复提交

## 环境变量

复制 `.env.example` 为 `.env`：

```powershell
copy .env.example .env
```

配置后端接口地址：

```env
VITE_API_BASE=http://127.0.0.1:8000
```

说明：

- Vite 前端环境变量必须以 `VITE_` 开头
- `VITE_API_BASE` 表示后端 FastAPI 服务地址

## 安装依赖

进入前端目录：

```powershell
cd E:\vscodeprogram\student-management-system\student-web
```

安装依赖：

```powershell
npm install
```

## 启动开发服务

```powershell
npm run dev
```

默认访问地址：

```text
http://localhost:5173
```

## 生产打包

```powershell
npm run build
```

打包产物会生成到：

```text
dist/
```

## 预览打包结果

```powershell
npm run preview
```

## 依赖后端服务

前端运行前，需要先启动后端 FastAPI 服务：

```text
http://127.0.0.1:8000
```

