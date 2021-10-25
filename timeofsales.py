import requests
import json
import pandas as pd
import time
import ctypes

url = "https://api.bybit.com/v2/public/trading-records?symbol=ETHUSD"

payload={}
headers = {}

i = 0
while (i >= 0):
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    latest_data = response_json['result'][0]

    class Latest_Data:
        def __init__(self, ticker, price, qty, side, time):
            self.ticker = ticker
            self.price = price
            self.qty = qty
            self.side = side
            self.time = time

    eth_info = Latest_Data(latest_data['symbol'],
            str(latest_data['price']),
            str(latest_data['qty']),
            latest_data['side'],
            latest_data['time'])

    eth_info.time = pd.to_datetime(eth_info.time)#converting date to timecode
    eth_info.time = eth_info.time.tz_convert('US/Eastern') #converting to EST
    eth_info.time = str(eth_info.time.strftime('%H:%M:%S')) #converting to hour:minute

    spacer = ' | '
    eth_all = (eth_info.ticker + spacer + eth_info.side
               + spacer + eth_info.price + spacer + 
               eth_info.qty + spacer + eth_info.time)
    if (i == 0):
        eth_prev = eth_all

    if (eth_prev != eth_all or i == 0):
        print(eth_all)
        ctypes.windll.kernel32.SetConsoleTitleW(eth_all)
        eth_prev = eth_all
    else:
        pass
    i += 1
    time.sleep(0.25)