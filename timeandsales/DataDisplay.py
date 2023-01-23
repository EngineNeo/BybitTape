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
        self.symbol_combobox = ttk.Combobox(self.root, width = 27, textvariable = self.symbol_selector, state="readonly")
        self.symbol_combobox['values'] = (current_symbols)
        self.symbol_combobox.set("ETHUSD") #set default value to ETHUSD
        self.symbol_combobox.grid(sticky='W', row = 0, column = 0)

        self.selected_symbol = self.symbol_selector.get()
        
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
        self.tree.grid(row=1, column=0, columnspan=2, rowspan=99,sticky='nsew') 

        # Add a row and column configuration to the grid layout manager
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    # Inserting data into columns
    def insert_data(self, ticker, side, price, quantity, timestamp):
        self.tree.tag_configure("Buy", background="blue", foreground = "white")
        self.tree.tag_configure("Sell", background="red", foreground = "white")
        item_id = self.tree.insert("", "end", values=(ticker, side, price, quantity, timestamp), tags = side.lower())
        self.tree.see(item_id)

    # Method to clear the treeview
    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    # Making the gui operable 
    def start(self):
        self.root.mainloop()