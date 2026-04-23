import requests
import os

print("API 테스트 시작")

APP_KEY = os.getenv("KIS_APP_KEY")
APP_SECRET = os.getenv("KIS_APP_SECRET")

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

print(res.json())
