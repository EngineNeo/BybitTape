from PyQt5.QtWidgets import QApplication
from TradeData import TradeData
from DataDisplay import DataDisplay

def main():
    app = QApplication([]) # Initializing QApplication
    trade_data = TradeData() # Initializing TradeData
    display = DataDisplay() # Initializing DataDisplay
    trade_data.display_trades("BTCUSD", display) # Displaying trades for BTCUSD
    display.show() # Showing the PyQt table
    app.exec_() # Running the PyQt GUI application

if __name__ == "__main__":
    main()