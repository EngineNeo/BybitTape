from pybit import WebSocket
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)
from time import sleep

# class basicWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         grid_layout = QGridLayout()
#         self.setLayout(grid_layout)

#         for x in range(25): # Column Length
#             for y in range(3): # Row Length
#                 button = QPushButton('  ')
#                 grid_layout.addWidget(button, x, y)
        
#         self.setWindowTitle('Price Ladder')

# Displays the window on run
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     windowExample = basicWindow()
#     windowExample.show()
#     sys.exit(app.exec_())

class LadderData:
    def __init__(self, symbol, bid, ask, size):
        self.symbol = symbol
        self.bid = bid
        self.ask = ask
        self.size = size
    def getBids(self):
        mostRecentBids = []
        for i in range(data[i]):
            if data[i]['side'] == 'Buy':
                mostRecentBids.append(data[i]['size'])
        
    def getAsks(self):
        mostRecentAsks = []
        for i in range(data[i]):
            if data[i]['side'] == 'Sell':
                mostRecentAsks.append(data[i]['size'])


subs = [
    "orderBookL2_25.ETHUSD"
]
ws = WebSocket(
    "wss://stream.bybit.com/realtime",
    subscriptions=subs
)
while True:
    data = ws.fetch(subs[0])
    if data:
        print 