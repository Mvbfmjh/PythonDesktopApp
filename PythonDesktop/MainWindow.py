from tkinter import *
from tkinter import ttk
import sqlite3
import os

root = Tk()
root.minsize(500,300)

def dbselection():
    try:
        selection = combo.get()
        local_DB_path = "./DB/"
        conn = sqlite3.connect(local_DB_path + selection)
        #print(selection)
        cur = conn.cursor()

        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

        cur.execute(sql_query)

        rowCount = 0

        for row in cur:
            print(row)
    except sqlite3.Error:
        print("Some error with sqlite3")

    

class MainWindow:
    def __init__(self, root):
        root.minsize(500,300)
        self.pagenum = 1
        self.mainpage()
        

    def changePage(self):
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum == 1:
            self.newPage()
            self.pagenum = 2
        else:
            self.mainpage()
            self.pagenum = 1

    def mainpage(self):
        root.title("My Window Class")

        self.db_list = dataset.getDataSet()

        content = ttk.Frame(root)
        image_frame1 = ttk.Frame(content, borderwidth=5, relief="ridge", width=150, height=300)
        image_frame2 = ttk.Frame(content, borderwidth=5, relief="ridge", width=150, height=300)
        #center_frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=350, height=300)
        label = ttk.Label(content, text="Select DB", font=("Arial", 12))
        combo = ttk.Combobox(content, width=30, values=self.db_list, font=("Arial", 12))
        button = ttk.Button(content, text="Select", command=self.changePage)

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

    def newPage(self):
        root.title("New page")
        content = ttk.Frame(root)
        back_btn = ttk.Button(content, text="Back", command=self.changePage)

        content.grid(column=0, row=0, sticky=(N,W,E,S))
        back_btn.grid(column=1, row=1, sticky=(N,W))

class dataset:
    def getDataSet():
        DBPATH = os.getcwd() + "\\DB"
        dblist = []
        for filepath in os.listdir(DBPATH):
            file = filepath.split('.')
            if file[1] == "db":
                print(filepath + " is a .db file")
                dblist.append(filepath)

        return dblist

root = Tk()
MainWindow(root)
root.mainloop()
