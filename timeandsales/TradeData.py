from pybit import inverse_perpetual
from pybit import usdt_perpetual

from datetime import datetime

class TradeData:
    def __init__(self):
        self.ipws = inverse_perpetual.WebSocket(test=False) # Initializing bybit websocket
        self.upws = usdt_perpetual.WebSocket(test=False) # Initializing bybit websocket for USDT symbols 

        # self.open_symbols = []
        # self.inverseperp_symbols = []
        # self.usdt_symbols = []
        # self.closed_symbols = []
        # self.session_auth = inverse_perpetual.HTTP( # Calling api endpoint for symbols
        #     endpoint="https://api.bybit.com"
        # )

        # for symbol in self.session_auth.query_symbol()['result']:
        #     if symbol['status'] == 'Trading':
        #         if 'usdt' in symbol['name'].lower():
        #             self.usdt_symbols.append(symbol['name'])
        #         else:
        #             self.inverseperp_symbols.append(symbol['name'])
        #     else:
        #         self.closed_symbols.append(symbol['name'])
                
        # self.open_symbols = self.inverseperp_symbols + self.usdt_symbols

    def display_trades(self, symbol, display):
        def handle_trades(message):
            try: # Attemping the function before running
                data = message['data']
                tickers = [trade['symbol'] for trade in data] # Retrieving the tickers from user
                sides = [trade['side'] for trade in data]
                prices = [trade['price'] for trade in data]
                quantities = [trade['size'] for trade in data]
                timestamps = [datetime.strptime(trade['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ').time() for trade in data] # Parsing timestamp information and only using H-M-S
                for i in range(len(data)):
                    display.insert_data(tickers[i], sides[i], prices[i], quantities[i], timestamps[i])
            except Exception as e: # Error handling
                print(e)
        
        # if symbol in self.inverseperp_symbols:
        self.ipws.trade_stream(handle_trades, symbol) # Output of data based on symbol
        # elif symbol in self.usdt_symbols:
        #     self.upws.trade_stream(handle_trades, symbol) # Output of data based on symbol
        # else:
        #     print("Invalid symbol")