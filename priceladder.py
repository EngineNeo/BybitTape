# from pybit import WebSocket
# subs = [
#     "orderBook_200.100ms.ETHUSD"
# ]
# ws = WebSocket(
#     "wss://stream.bybit.com/realtime",
#     subscriptions=subs
# )
# while True:
#     data = ws.fetch(subs[0])
#     if data:
#         for i in range(200):
#             print(data[i], end='\r', flush=True)