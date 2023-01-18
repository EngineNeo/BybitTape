from pybit import inverse_perpetual
from datetime import datetime

class TradeData:
    def __init__(self, test=False):
        self.ws = inverse_perpetual.WebSocket(test=test)

    def display_trades(self, symbol, display):
        def handle_trades(message):
            try:
                topic = message['topic']
                data = message['data']
                for trade in data:
                    ticker = trade.get('symbol')
                    side = trade['side']
                    price = trade['price']
                    quantity = trade['size']
                    timestamp = trade['timestamp']
                    timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
                    timestamp = timestamp.time()
                    display.insert_data(ticker, side, price, quantity, timestamp)
            except Exception as e:
                print(e)
        
        self.ws.trade_stream(handle_trades, symbol)