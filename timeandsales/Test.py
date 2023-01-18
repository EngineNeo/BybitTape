from pybit import inverse_perpetual

ws = inverse_perpetual.WebSocket(
        test=False
    )

# Check trades through WebSocket.
def handle_trades(message):
    print(message)

trade_data = ws.trade_stream(handle_trades, "ETHUSD")

while True:
    pass