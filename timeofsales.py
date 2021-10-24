import requests
import json

url = "https://api.bybit.com/v2/public/trading-records?symbol=ETHUSD"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)