from pybit import inverse_perpetual
from datetime import datetime

def defined_symbol():
        current_symbols = []
        invalid_symbols = []
        session_auth = inverse_perpetual.HTTP(
            endpoint="https://api-testnet.bybit.com"
        )

        for symbol in session_auth.query_symbol()['result']:
            if symbol['status'] == 'Trading':
                current_symbols.append(symbol['name'])
            else:
                invalid_symbols.append(symbol['name'])

        return current_symbols

class TradeData:
    def __init__(self, test=False):
        self.ws = inverse_perpetual.WebSocket(test=False) # Initializing bybit websocket

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
