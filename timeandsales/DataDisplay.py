from PyQt5 import QtWidgets, QtCore
import time
import sys

class DataDisplay(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Trade Data Display')

        # Start timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.addData)
        self.timer.start(1000)

        # Create table
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(0)

        # Set table headers
        self.header_labels = ['symbol', 'side', 'price', 'quantity', 'timestamp']
        self.table.setHorizontalHeaderLabels(self.header_labels)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.setCentralWidget(self.table)
        
        self.table.verticalHeader().setVisible(False) # Removing vertical header 
    
        self.setCentralWidget(self.table)
        self.resize(600, 800)
    
    @QtCore.pyqtSlot()
    def addData(self):
        # Get the current row count
        row = self.table.rowCount()

        # Add a new row
        self.table.insertRow(row)

        for col in range(5):
            if col == 0:
                value = "symbol"
            elif col == 1:
                value = "side"
            elif col == 2:
                value = "price"
            elif col == 3:
                value = f"{row + 1}"
            else:
                value = str(time.time())

            item = QtWidgets.QTableWidgetItem(value)
            self.table.setItem(row, col, item)
            self.table.scrollToItem(item)

    # def add_trade_data(self, trade_data):
    #     row = self.table.rowCount()
    #     self.table.insertRow(row)
    #     self.table.setItem(row, 0, QtWidgets.QTableWidgetItem('ETHUSD'))
    #     self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(trade_data['side']))
    #     self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(trade_data['price'])))
    #     self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(trade_data['quantity'])))
    #     self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(trade_data['timestamp'])))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    display = DataDisplay()
    display.show()
    sys.exit(app.exec_())