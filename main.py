import requests
import os

APP_KEY = os.getenv("KIS_APP_KEY")
APP_SECRET = os.getenv("KIS_APP_SECRET")

# 토큰 발급
url = "https://openapi.koreainvestment.com:9443/oauth2/tokenP"
headers = {"content-type": "application/json"}
data = {
    "grant_type": "client_credentials",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET
}
res = requests.post(url, headers=headers, json=data)
ACCESS_TOKEN = res.json()["access_token"]

print("토큰 발급 완료")

# 현재가 조회
url = "https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/quotations/inquire-price"

headers = {
    "authorization": f"Bearer {ACCESS_TOKEN}",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
    "tr_id": "FHKST01010100"
}

params = {
    "fid_cond_mrkt_div_code": "J",
    "fid_input_iscd": "005930"
}

res = requests.get(url, headers=headers, params=params)

print(res.json())
