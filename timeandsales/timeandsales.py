from TradeData import handle_trades
from DataDisplay import DataDisplay
import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)

    trade_data = handle_trades() # Call the handle_trades function from TradeData.py

    display = DataDisplay(trade_data) # Create a DataDisplay object with the trade data
    display.show() # Show the DataDisplay window

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
