import requests


BASE_URL = "http://127.0.0.1:8000"

def test_chat():
  url = f"{BASE_URL}/chat"
  
  headers = {
    "content-type": "application/json"
  }
  
  data = {
    "text":"你是谁？",
  }
  
  res = requests.post(
    url=url,
    headers=headers,
    json=data
  )
  print(res.status_code)
  print(res.json())
    
def test_echo():
    """测试 POST /echo 接口"""
    url = f"{BASE_URL}/echo"
    
    headers = {
        "Content-Type": "application/json",
        "x-token": "123"  # 测试请求头
    }
    
    data = {"number": 10}
    
    res = requests.post(url, headers=headers, json=data)
    print(f"Echo 结果: {res.json()}")  # 应该返回 {"number": 11}
    
    
def test_hello():
    """测试 GET /hello/{name} 接口"""
    url = f"{BASE_URL}/"
    
    res = requests.get(url)
    print(f"Hello 结果: {res.json()}")  # 应该返回 {"messages": "hello 小明"}
    
if __name__ == "__main__":
    # print("🧪 开始测试...\n")
    
    # print("1️⃣ 测试 /hello 接口")
    
    # test_hello()
    # print()
    
    # print("2️⃣ 测试 /echo 接口")
    # test_echo()
    # print()
    
    print("3️⃣ 测试 /chat 接口（需要 API Key）")
    test_chat()