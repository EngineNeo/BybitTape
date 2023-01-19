from TradeData import TradeData
from DataDisplay import DataDisplay

def main():
    trade_data = TradeData(test=False)
    current_symbols = trade_data.defined_symbol()
    display = DataDisplay(current_symbols, trade_data.display_trades) # Create an instance of DataDisplay
    trade_data = TradeData()
    trade_data.display_trades("ETHUSD", display)
    display.start()

if __name__ == "__main__":
    main()