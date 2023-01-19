import tkinter as tk
from tkinter import ttk

class DataDisplay:
    def __init__(self):

        # Init tkinter
        self.root = tk.Tk()
        self.root.title("Trade Data")
        self.root.geometry("1000x800")
        
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
        self.tree.column("#1", stretch=tk.YES)
        self.tree.column("#2", stretch=tk.YES)
        self.tree.column("#3", stretch=tk.YES)
        self.tree.column("#4", stretch=tk.YES)
        self.tree.column("#5", stretch=tk.YES)

        # Create a vertical scrollbar
        v_scroll = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)

        # Create a horizontal scrollbar
        h_scroll = ttk.Scrollbar(self.root, orient="horizontal", command=self.tree.xview)

        # Configure horizontal and vertical scrollbars
        self.tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        # Set scrollbars
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        # Pack the tree widget
        self.tree.pack(expand=True, fill='both')
        
    # Inserting data into columns
    def insert_data(self, ticker, side, price, quantity, timestamp):
        self.tree.tag_configure("buy", background="blue", foreground = "white")
        self.tree.tag_configure("sell", background="red", foreground = "white")
        self.tree.insert("", "end", values=(ticker, side, price, quantity, timestamp), tags = side.lower())

    # Making the gui operable 
    def start(self):
        self.root.mainloop()