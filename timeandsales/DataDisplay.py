from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication
import sys

class DataDisplay:
    def init(self):
        self.app = QApplication(sys.argv) # Initializing PyQt application
        self.table = QTableWidget() # Creating a table widget
        self.table.setWindowTitle("Trade Data") # Setting the title of the table widget
        self.table.setColumnCount(5) # Setting the number of columns in the table
        self.table.setHorizontalHeaderLabels(["Ticker", "Side", "Price", "Quantity", "Timestamp"]) # Setting the header labels
        self.table.show() # Showing the table

    def insert_data(self, ticker, side, price, quantity, timestamp):
        row = self.table.rowCount() # Getting the current number of rows
        self.table.insertRow(row) # Adding a new row
        self.table.setItem(row, 0, QTableWidgetItem(ticker)) # Setting the values for the new row
        self.table.setItem(row, 1, QTableWidgetItem(side))
        self.table.setItem(row, 2, QTableWidgetItem(str(price)))
        self.table.setItem(row, 3, QTableWidgetItem(str(quantity)))
        self.table.setItem(row, 4, QTableWidgetItem(str(timestamp)))
    def show(self): # Adding the show method
        self.showMaximized()