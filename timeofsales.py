# TO-DO

# CRASH LOGGING FOR DEBUGGING

import requests
import json
import pandas as pd
import time
import ctypes
from colorama import init, Back

init() # Colorama init

# Select which symbol to track
def starttimeofSales():
    symbol = input('Enter Symbol to Track (i.e - BTCUSD, ETHUSD):\n')
    symbol = str(symbol)
    url = (f"https://api.bybit.com/v2/public/trading-records?symbol={symbol}")
    print('initializing..')
    return url

url = starttimeofSales()
class LatestData:
        def __init__(self, id, ticker, price, qty, side, time):
            self.id = id
            self.ticker = ticker
            self.price = price
            self.qty = qty
            self.side = side
            self.time = time
        
        def display(self, title = False):
            if (title == True): # Title is a normal string
                display = (f" {self.ticker} | {self.side: ^4}"
                        f" | {self.price: <7} | {self.qty: <7}"
                        f" | {self.time}")
            elif (self.side == 'Buy'): # Buy Color
                blue_buy = (Back.BLUE + self.side + ' ' + Back.RESET)
                display = (f" {self.ticker} | {blue_buy: ^4}"
                        f" | {self.price: <7} | {self.qty: <7}"
                        f" | {self.time} ")
            elif (self.side == 'Sell'): # Sell Color
                red_sell = (Back.RED + self.side + Back.RESET)
                display = (f" {self.ticker} | {red_sell}"
                           f" | {self.price: <7} | {self.qty: <7}"
                           f" | {self.time} ")
            return display

# To count first loop
i = 0
while (i >= 0):

    response = requests.request("GET", url)
    response_json = json.loads(response.text)
    latest_data = response_json['result'][0]

    eth_info = LatestData(latest_data['id'],
            latest_data['symbol'],
            str(latest_data['price']),
            str(latest_data['qty']),
            latest_data['side'],
            latest_data['time'])

    # Timecode conversions
    eth_info.time = pd.to_datetime(eth_info.time) # converting date to timecode
    eth_info.time = eth_info.time.tz_convert('US/Eastern') # converting to EST
    eth_info.time = str(eth_info.time.strftime('%H:%M:%S')) # converting to hour:minute

    idmain = eth_info.id # unique ID per transaction
    if (i == 0):
        idprev = idmain

    # Only print data if new transaction is live
    if (idprev != idmain or i == 0):
        print(eth_info.display(title=False))
        ctypes.windll.kernel32.SetConsoleTitleW(eth_info.display(title=True)) # sets window title
        idprev = idmain
    elif (idprev == idmain):
        pass
    i += 1
    time.sleep(0.05) # API call speed (Current: 50ms)