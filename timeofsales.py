import requests
import json
import pandas as pd
import time
import ctypes
# import colorama
# from colorama import Fore, init

url = "https://api.bybit.com/v2/public/trading-records?symbol=ETHUSD"

payload={}
headers = {}

i = 0

class Latest_Data:
        def __init__(self, id, ticker, price, qty, side, time):
            self.id = id
            self.ticker = ticker
            self.price = price
            self.qty = qty
            self.side = side
            self.time = time
        
        def display(self):
            display = (f" {self.ticker} | {self.side: <4} | {self.price: <7} | {self.qty: <7} | {self.time} ")
            return display

while (i >= 0):
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    latest_data = response_json['result'][0]

    eth_info = Latest_Data(latest_data['id'],
            latest_data['symbol'],
            str(latest_data['price']),
            str(latest_data['qty']),
            latest_data['side'],
            latest_data['time'])

    eth_info.time = pd.to_datetime(eth_info.time) # converting date to timecode
    eth_info.time = eth_info.time.tz_convert('US/Eastern') # converting to EST
    eth_info.time = str(eth_info.time.strftime('%H:%M:%S')) # converting to hour:minute

    idmain = eth_info.id # unique ID per transaction
    if (i == 0):
        idprev = idmain

    if (idprev != idmain or i == 0):
        print(eth_info.display())
        ctypes.windll.kernel32.SetConsoleTitleW(eth_info.display()) # sets window title
        idprev = idmain
    elif (idprev == idmain):
        pass
    i += 1
    time.sleep(0.1)