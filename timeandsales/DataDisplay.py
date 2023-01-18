import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# class ApplicationWindow(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=root.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = ApplicationWindow(master=root)
# app.mainloop()

# Creating tkinter main window
win = tk.Tk()
win.title("ScrolledText Widget")
  
# Title Label
# ttk.Label(win, 
#           text = "ScrolledText Widget Example",
#           font = ("Arial", 15), 
#           background = 'green', 
#           foreground = "white").grid(column = 0,
#                                      row = 0)
  
# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(win, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Arial",
                                              15))
  
text_area.grid(column = 0, pady = 10, padx = 10)

# Inserting Text which is read only
text_area.insert(tk.INSERT, )
  
# Making the text read only
text_area.configure(state ='disabled')
win.mainloop()