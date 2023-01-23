from pybit import inverse_perpetual
from pybit import usdt_perpetual

from datetime import datetime

class TradeData:
    def __init__(self):
        self.ipws = inverse_perpetual.WebSocket(test=False) # Initializing bybit websocket
        self.upws = usdt_perpetual.WebSocket(test=False) # Initializing bybit websocket for USDT symbols 

        self.open_symbols = []
        self.inverseperp_symbols = []
        self.usdt_symbols = []
        self.closed_symbols = []
        self.session_auth = inverse_perpetual.HTTP( # Calling api endpoint for symbols
            endpoint="https://api.bybit.com"
        )

        for symbol in self.session_auth.query_symbol()['result']:
            if symbol['status'] == 'Trading':
                if 'usdt' in symbol['name'].lower():
                    self.usdt_symbols.append(symbol['name'])
                else:
                    self.inverseperp_symbols.append(symbol['name'])
            else:
                self.closed_symbols.append(symbol['name'])
                
        self.open_symbols = self.inverseperp_symbols + self.usdt_symbols

    def display_trades(self, symbol, display):
        def handle_trades(message):
            try: # Attemping the function before running
                data = message['data']
                for trade in data:
                    ticker = trade.get('symbol') # Retrieving the ticker from user
                    side = trade['side']
                    price = trade['price']
                    quantity = trade['size']
                    timestamp = trade['timestamp']
                    timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ') # Parsing timestamp information
                    timestamp = timestamp.time() # Only using H-M-S
                    display.insert_data(ticker, side, price, quantity, timestamp)
            except Exception as e: # Error handling
                print(e)
        
        if symbol in self.inverseperp_symbols:
            self.ipws.trade_stream(handle_trades, symbol) # Output of data based on symbol
        elif symbol in self.usdt_symbols:
            self.upws.trade_stream(handle_trades, symbol) # Output of data based on symbol
        else:
            print("Invalid symbol")