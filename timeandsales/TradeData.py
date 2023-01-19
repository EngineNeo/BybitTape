from pybit import inverse_perpetual
from datetime import datetime

class TradeData:
    def __init__(self):
        self.ws = inverse_perpetual.WebSocket(test=False) # Initializing bybit websocket

        self.current_symbols = []
        self.invalid_symbols = []
        self.session_auth = inverse_perpetual.HTTP(
            endpoint="https://api-testnet.bybit.com"
        )

        for symbol in self.session_auth.query_symbol()['result']:
            if symbol['status'] == 'Trading':
                self.current_symbols.append(symbol['name'])
            else:
                self.invalid_symbols.append(symbol['name'])

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
        
        self.ws.trade_stream(handle_trades, symbol) # Output of data based on symbol
