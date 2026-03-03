# main.py
import os
from dotenv import load_dotenv
load_dotenv(override=True)
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, field_validator
import uvicorn

api_key = os.getenv("DASHSCOPE_API_KEY")
app = FastAPI(title="WebAgent", version="1.0")


# ========== 数据模型 ==========
class Chat_type(BaseModel):
    """聊天请求的数据格式"""
    text: str
    
    @field_validator('text')
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        """验证 text 不能为空"""
        if not v or not v.strip():
            raise ValueError('问题不能为空')
        return v.strip()


# ========== 路由接口 ==========
@app.get("/")
async def root():
    """根路径"""
    return {"messages": "hello world"}



@app.post("/echo")
async def echo(request: Request):
    """接收 JSON 并返回 +1 的结果"""
    # 读取请求头（你学的功能，保留）
    x_token = request.headers.get("x-token")
    content_type = request.headers.get("content-type")
    
    # 读取请求体
    data = await request.json()
    number = data.get("number")
    
    return {"number": number + 1}


@app.post("/chat")
async def post(request:Chat_type):
  
  text = request.text

  if text == "":
    raise HTTPException(status_code=400,detail="不能为null")
  
  try:
    from langchain_community.chat_models import ChatTongyi
    llm = ChatTongyi(
      model="qwen-plus",
      api_key=api_key
    )

    res = await llm.ainvoke(text)
    return res.content
    
  except Exception as e:
    print(f"后台错误：{e}")
    raise HTTPException(
      status_code=500,
      detail="AI服务器繁忙，请稍后重试"
    )


# ========== 全局异常处理 ==========
@app.exception_handler(Exception)
async def global_exception(request: Request, exc: Exception):
    """捕获所有未处理的异常"""
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "系统内部错误"}
    )


# ========== 启动入口 ==========
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)