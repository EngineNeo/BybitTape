from TradeData import TradeData
from DataDisplay import DataDisplay

def main():
    display = DataDisplay() # Create an instance of DataDisplay
    trade_data = TradeData()
    trade_data.display_trades("ETHUSD", display)
    display.start()

if __name__ == "__main__":
    main()