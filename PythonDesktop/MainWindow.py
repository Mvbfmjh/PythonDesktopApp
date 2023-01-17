from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(500,300)

db_list = ["cheese", "test"]

content = ttk.Frame(root)
image_frame1 = ttk.Frame(content, borderwidth=5, relief="ridge", width=150, height=300)
image_frame2 = ttk.Frame(content, borderwidth=5, relief="ridge", width=150, height=300)
#center_frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=350, height=300)
label = ttk.Label(content, text="Select DB", font=("Arial", 12))
combo = ttk.Combobox(content, width=30, values=db_list, font=("Arial", 12))
button = ttk.Button(content, text="Select")

content.grid(column=0, row=0, sticky=(N,W,E,S))
image_frame1.grid(column=0, row=0, columnspan=1, rowspan=3, padx=10, pady=10, sticky=(N, W, E, S))
image_frame2.grid(column=2, row=0, columnspan=1, rowspan=3, padx=10, pady=10, sticky=(N, W, E, S))
#center_frame.grid(column=1, row=0, columnspan=1, rowspan=3, pady=10, sticky=(N, W, E, S))
label.grid(column=1, row=0, padx=10, pady=10, sticky=S)
combo.grid(column=1, row=1,  padx=10, pady=10, sticky=(EW))
button.grid(column=1, row=2, padx=10, pady=10)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=0)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=0)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)

root.mainloop()