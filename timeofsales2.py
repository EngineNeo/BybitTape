from pybit import WebSocket
import pandas as pd
from colorama import init, Back
import json

init() # Colorama init

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

subs = [
    "trade.ETHUSD"
]
ws = WebSocket(
    "wss://stream-testnet.bybit.com/realtime",
    subscriptions=subs
)
while True:
    data = ws.fetch(subs[0])

    # data_info = (data['trade_id'],
    #         data['symbol'],
    #         str(data['price']),
    #         str(data['qty']),
    #         data['side'],
    #         data['time_stamp'])

    # Timecode conversions
    # data_info.time = pd.to_datetime(data_info.time) # converting date to timecode
    # data_info.time = data_info.time.tz_convert('US/Eastern') # converting to EST
    # data_info.time = str(data_info.time.strftime('%H:%M:%S')) # converting to hour:minute
    if data:
        print(data[0])
        if not data[0]:
            print(data[1])
        else:
            print(data[0])