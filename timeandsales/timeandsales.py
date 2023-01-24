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
        
    def filter_trades():
        # Get value from user input
        filter_value = int(display.filter_entry.get())
        display.clear_tree() # Clear tree before adding new data
        selected_symbol = display.symbol_combobox.get()
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
    
    selected_symbol = display.symbol_combobox.get()
    trade_data.display_trades(selected_symbol, display, 1)
    display.start()

if __name__ == "__main__":
    main()