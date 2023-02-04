from pybit import inverse_perpetual
from datetime import datetime

ipws = inverse_perpetual.WebSocket(
    test=False,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)

def handle_trades(trade_data):
    try: # Attempting the function before running
        data = trade_data['data']
        for trade in data:
            keys_to_delete = ["trade_time_ms", "symbol", 
                              "trade_id", "cross_seq", 
                              "is_block_trade"]
            for key in keys_to_delete:
                trade.pop(key, None)
            trade['timestamp'] = datetime.strptime(trade['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ') # Parsing timestamp information
            trade['timestamp'] = trade['timestamp'].time() # Only using H-M-S
    except Exception as e: # Error handling
        print(e)
    
ipws.trade_stream(handle_trades, "ETHUSD") # Output of data based on symbol

while True:
    pass