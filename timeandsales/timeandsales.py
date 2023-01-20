from TradeData import TradeData
from DataDisplay import DataDisplay

def main():
    trade_data = TradeData()
    allowed_symbols = trade_data.inverseperp_symbols
    display = DataDisplay(allowed_symbols) # Create an instance of DataDisplay
    selected_symbol = display.selected_symbol
    trade_data.display_trades(selected_symbol, display)
    display.start()

if __name__ == "__main__":
    main()