import requests
import os

print("API 테스트 시작")

APP_KEY = os.getenv("KIS_APP_KEY")
APP_SECRET = os.getenv("KIS_APP_SECRET")

print("APP_KEY:", APP_KEY is not None)
print("APP_SECRET:", APP_SECRET is not None)

url = "https://openapi.koreainvestment.com:9443/oauth2/tokenP"

headers = {
    "content-type": "application/json"
}

data = {
    "grant_type": "client_credentials",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET
}

res = requests.post(url, headers=headers, json=data)

print("응답 전체 ↓↓↓")
print(res.json())

if "access_token" in res.json():
    ACCESS_TOKEN = res.json()["access_token"]
    print("토큰 발급 성공")
else:
    print("토큰 없음 → 위 에러 확인해라")
