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
        
    def apply_filter():
            # Get the filter value from the input field
            filter_value = display.filter_entry.get()
            if filter_value:
                # Convert the value to an int and use it to filter the data displayed in the treeview
                filter_value = int(filter_value)
                for item in display.tree.get_children():
                    quantity = display.tree.item(item, "values")[3]
                    if quantity < filter_value:
                        display.tree.delete(item)

    # Combobox events
    display.symbol_combobox.bind("<<ComboboxSelected>>", on_select)
    display.filter_entry.bind("<Return>", apply_filter)
    
    selected_symbol = display.symbol_combobox.get()
    trade_data.display_trades(selected_symbol, display)
    display.start()

if __name__ == "__main__":
    main()