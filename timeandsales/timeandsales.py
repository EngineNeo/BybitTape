from TradeData import TradeData
from DataDisplay import DataDisplay

def main():
    trade_data = TradeData()
    allowed_symbols = trade_data.open_symbols
    display = DataDisplay(allowed_symbols)
    filter_value = display.filter_quantity.get()

    def on_select(event):
        display.clear_tree()
        filter_value = display.filter_quantity.get()
        selected_symbol = display.symbol_combobox.get()
        trade_data.display_trades(selected_symbol, display, filter_value)

    def validate_int_backspace_return(P, d):
        if d == '1':  # key pressed is backspace
            return True
        elif d == '0':  # key pressed is return
            return True
        elif P.isdigit():  # input is an int
            return True
        else:
            return False


    display.filter_entry.insert(0, '1')
    # Only allow integers to be entered
    display.filter_entry.config(validate="key")
    display.filter_entry.config(validatecommand=(display.root.register(validate_int_backspace_return), '%P', '%d'))

    # Combobox event
    display.symbol_combobox.bind("<<ComboboxSelected>>", on_select)

    # Filter Event
    display.filter_entry.bind("<Return>", on_select)

    selected_symbol = display.symbol_combobox.get()
    trade_data.display_trades(selected_symbol, display, filter_value)
    display.start()

if __name__ == "__main__":
    main()