# 🤖 WebAgent
一个简单的 FastAPI + 阿里云大模型聊天接口

# ✨ 功能
- GET / - 返回欢迎消息
- GET /hello/{name} - 返回个性化问候
- POST /echo - 接收数字，返回 +1 的结果
- POST /chat - 调用阿里云通义千问回答用户问题

# 🚀 快速开始

## 1️⃣ 环境准备
```bash
# 1. 激活虚拟环境（Windows）
.venv\Scripts\activate
# .\.venv\Scripts\Activate.ps1

# Mac/Linux 用户：
# source .venv/bin/activate

# 2. 安装依赖
pip install -r requirements.txt
```

## 2️⃣ 配置 API Key
```bash
copy .env.example .env
```

## 3️⃣ 启动服务
```bash
python main.py
```
看到以下输出表示启动成功：
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

## 4️⃣ 测试接口
```bash
方案一：
http://127.0.0.1:8000/docs
方案二：
python test_api.py
```

# 📁 项目结构
```bash
webagent/
├── main.py              # 主程序（所有接口代码）
├── test_api.py          # 接口测试脚本
├── requirements.txt     # Python 依赖清单
├── .env.example         # 环境变量模板
├── .env                 # 真实配置（自己创建，不提交）
├── .gitignore           # Git 忽略规则
└── README.md            # 本文档
```




