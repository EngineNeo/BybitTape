import pandas as pd
from colorama import init, Back
import ctypes
from pybit import inverse_perpetual
from time import sleep

# TO-DO

# FILTER SIZE
# USER ABILITY TO CHANGE ENDPOINT
# USER ABILITY TO FILTER SIZE
# SOUND ALERTS AND HIGHLIGHTING

init() # Colorama init

ws = inverse_perpetual.WebSocket(
    test=False
)

# Display uniquely, traded orders
def Display(symbol, price, size, side, timestamps):
    if (side == 'Buy'): # Buy Trade
        blue_buy = (Back.BLUE + side + ' ' + Back.RESET)
        display = (f" {symbol} | {blue_buy: ^4}"
                f" | {price: <7} | {size: <7}"
                f" | {timestamps} ")
    elif (side == 'Sell'): # Sell Trades
        red_sell = (Back.RED + side + Back.RESET)
        display = (f" {symbol} | {red_sell}"
                    f" | {price: <7} | {size: <7}"
                    f" | {timestamps} ")
    return display

# Check trades through WebSocket.
def handle_trades(message):
    print(message)

trade_data = ws.trade_stream(handle_trades, "ETHUSD")
trade_data = trade_data['data']

for i in trade_data:
    latest_trade_info = trade_data[i]
    parsed_info = Display(latest_trade_info)
    print(parsed_info)

while True:
    # Run your main trading strategy here
    pass  # To avoid CPU utilisation, use time.sleep(1)

# class LatestData:
#         def __init__(self, ticker, price, size, side, time):
#             self.ticker = ticker
#             self.price = price
#             self.size = size
#             self.side = side
#             self.time = time
        
#         def display(self, title = False):
#             if (title == True): # Title is a normal string
#                 display = (f" {self.ticker} | {self.side: ^4}"
#                         f" | {self.price: <7} | {self.size: <7}"
#                         f" | {self.time}")
#             elif (self.side == 'Buy'): # Buy Color
#                 blue_buy = (Back.BLUE + self.side + ' ' + Back.RESET)
#                 display = (f" {self.ticker} | {blue_buy: ^4}"
#                         f" | {self.price: <7} | {self.size: <7}"
#                         f" | {self.time} ")
#             elif (self.side == 'Sell'): # Sell Color
#                 red_sell = (Back.RED + self.side + Back.RESET)
#                 display = (f" {self.ticker} | {red_sell}"
#                            f" | {self.price: <7} | {self.size: <7}"
#                            f" | {self.time} ")
#             return display

# ws_inverse = inverse_perpetual.WebSocket(
#     test = False,
#     domain="bytick"
# )
    
# def access_trades(message):
#     trade_data = message['data'][0]
#     data_info = LatestData(trade_data['symbol'],
#             str(trade_data['price']),
#             str(trade_data['size']),
#             trade_data['side'],
#             trade_data['timestamp'])

#     # Timecode conversions
#     data_info.time = pd.to_datetime(data_info.time) # converting date to timecode
#     data_info.time = data_info.time.tz_convert('US/Eastern') # converting to EST
#     data_info.time = str(data_info.time.strftime('%H:%M:%S')) # converting to hour:minute

#     if trade_data[0]:
#         print(data_info.display(title=False))
#         ctypes.windll.kernel32.SetConsoleTitleW(data_info.display(title=True)) # sets window title
#     if not trade_data[0]:
#         trade_data[1]
#         print(data_info.display(title=False))
#         ctypes.windll.kernel32.SetConsoleTitleW(data_info.display(title=True)) # sets window title
# ws_inverse.trade_stream(access_trades, 'ETHUSD')

# while True:

#     sleep(0.01)