import tkinter as tk
from tkinter import ttk

class DataDisplay:
    def __init__(self, current_symbols):

        # Init tkinter
        self.root = tk.Tk()
        self.root.title("Trade Data")
        self.root.geometry("600x800")

        # Dropdown menu/combobox for symbols
        self.symbol_selector = tk.StringVar()
        self.symbol_combobox = ttk.Combobox(self.root, width = 27, textvariable = self.symbol_selector, state="normal")
        self.symbol_combobox['values'] = (current_symbols)
        self.symbol_combobox.set("ETHUSD") # Default value of ticker to track
        self.symbol_combobox.grid(sticky='W', row = 0, column = 0)
        
        self.selected_symbol = self.symbol_selector.get()
        
        # Adding "Filter" label
        filter_label = tk.Label(self.root, text="Filter", font=("Arial", 10))
        filter_label.grid(row=0, column=0, padx=10, sticky='W')

        # Adding input field for filtering by quantity
        self.filter_entry = tk.Entry(self.root, width=5)
        self.filter_entry.grid(row=0, column=1, padx=10, sticky='W')

        # Adding a button to apply the filter
        self.apply_filter_button = tk.Button(self.root, text="Apply Filter")
        self.apply_filter_button.grid(row=0, column=2, padx=10, sticky='W')


        # Creating column headers
        self.tree = ttk.Treeview(self.root, columns=("Ticker", "Side", "Price", "Quantity", "Timestamp"))
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("#1", text="Ticker", anchor=tk.W)
        self.tree.heading("#2", text="Side", anchor=tk.W)
        self.tree.heading("#3", text="Price", anchor=tk.W)
        self.tree.heading("#4", text="Quantity", anchor=tk.W)
        self.tree.heading("#5", text="Timestamp", anchor=tk.W)

        # Creating columns
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("#1", width=50, stretch=tk.YES)
        self.tree.column("#2", width=50, stretch=tk.YES)
        self.tree.column("#3", width=100, stretch=tk.YES)
        self.tree.column("#4", width=100, stretch=tk.YES)
        self.tree.column("#5", width=100, stretch=tk.YES)
        
        # Adding scrollbar
        v_scroll = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        v_scroll.grid(row=1, column=2, sticky='ns')

        # Connect scrollbar to tree
        self.tree.configure(yscrollcommand=v_scroll.set)

        # Pack the tree widget
        self.tree.grid(row=1, column=0, rowspan=99,sticky='nsew') 

        # Add a row and column configuration to the grid layout manager
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    # Inserting data into columns
    def insert_data(self, ticker, side, price, quantity, timestamp):
    # Add tags to the side column
        if side == "Sell":
            self.tree.tag_configure("sell", background="red", foreground="white")
            item_id = self.tree.insert("", "end", values=(ticker, side, price, quantity, timestamp), tags = "sell")
        elif side == "Buy":
            self.tree.tag_configure("buy", background="blue", foreground="white")
            item_id = self.tree.insert("", "end", values=(ticker, side, price, quantity, timestamp), tags = "buy")
        self.tree.see(item_id)

    # Method to clear the treeview
    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    # Making the gui operable 
    def start(self):
        self.root.mainloop()