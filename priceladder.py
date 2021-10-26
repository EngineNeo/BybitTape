import requests
import json

url = "https://api.bybit.com/v2/public/orderBook/L2?symbol=ETHUSD"

response = requests.request("GET", url)
response_json = json.loads(response.text)