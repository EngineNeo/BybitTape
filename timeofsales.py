from pybit import WebSocket
import pandas as pd
from colorama import init, Back

init() # Colorama init

class LatestData:
        def __init__(self, ticker, price, size, side, time):
            self.ticker = ticker
            self.price = price
            self.size = size
            self.side = side
            self.time = time
        
        def display(self, title = False):
            if (title == True): # Title is a normal string
                display = (f" {self.ticker} | {self.side: ^4}"
                        f" | {self.price: <7} | {self.size: <7}"
                        f" | {self.time}")
            elif (self.side == 'Buy'): # Buy Color
                blue_buy = (Back.BLUE + self.side + ' ' + Back.RESET)
                display = (f" {self.ticker} | {blue_buy: ^4}"
                        f" | {self.price: <7} | {self.size: <7}"
                        f" | {self.time} ")
            elif (self.side == 'Sell'): # Sell Color
                red_sell = (Back.RED + self.side + Back.RESET)
                display = (f" {self.ticker} | {red_sell}"
                           f" | {self.price: <7} | {self.size: <7}"
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

    if data:
        FIData = data[0]

        data_info = LatestData(FIData['symbol'],
                str(FIData['price']),
                str(FIData['size']),
                FIData['side'],
                FIData['timestamp'])

        # Timecode conversions
        data_info.time = pd.to_datetime(data_info.time) # converting date to timecode
        data_info.time = data_info.time.tz_convert('US/Eastern') # converting to EST
        data_info.time = str(data_info.time.strftime('%H:%M:%S')) # converting to hour:minute
        if data[0]:
            print(data_info.display(title=False))
        if not data[0]:
            FIData = data[1]
            print(data_info.display(title=False))