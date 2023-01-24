from TradeData import TradeData
from DataDisplay import DataDisplay

def main():
    trade_data = TradeData()
    allowed_symbols = trade_data.open_symbols
    display = DataDisplay(allowed_symbols) # Create an instance of DataDisplay
    filter_value = display.filter_quantity.get()
    selected_symbol = display.symbol_combobox.get()

    def on_select():
        display.clear_tree()
        trade_data.display_trades(selected_symbol, display, filter_value)
        
    def filter_trades():
        # Get value from user input
        display.clear_tree() # Clear tree before adding new data
        trade_data.display_trades(selected_symbol, display, filter_value)

    def validate_int(P): # Function for the following int validation
        if P.isdigit():
            return True
        return False

    # Only allow integers to be entered
    display.filter_entry.config(validate="key")
    display.filter_entry.config(validatecommand=(display.root.register(validate_int), '%P'))

    # Combobox event
    display.symbol_combobox.bind("<<ComboboxSelected>>", on_select)

    # Filter Event
    display.filter_entry.bind("<Return>", filter_trades)

    selected_symbol = display.symbol_combobox.get() # Retrive Ticker from combobox
    trade_data.display_trades(selected_symbol, display, filter_value)
    display.start()

if __name__ == "__main__":
    main()