from TradeData import TradeData
from DataDisplay import DataDisplay

def main():
    trade_data = TradeData()
    allowed_symbols = trade_data.open_symbols
    display = DataDisplay(allowed_symbols) # Create an instance of DataDisplay

    def on_select():
        display.clear_tree()
        selected_symbol = display.symbol_combobox.get()
        trade_data.display_trades(selected_symbol, display)

    display.symbol_combobox.bind("<<ComboboxSelected>>", on_select)
    selected_symbol = display.symbol_combobox.get()
    trade_data.display_trades(selected_symbol, display)
    display.start()

if __name__ == "__main__":
    main()