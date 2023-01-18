from tkinter import *
from tkinter import ttk
import sqlite3
import os


class MainWindow:
    def __init__(self, root):
        self.pagenum = 1
        self.mainpage()

    def dbselected(self):
        self.selection = None
        self.selectedtitle = None
        for widget in self.window.winfo_children():
            #print(widget.winfo_class())
            if widget.winfo_class() == "TCombobox":
                self.selection = widget.get()

        if self.selection != None and self.selection != "":
            DBNAME = self.selection.split('.')
            if DBNAME[0] == "FE3H":
                #print(DBNAME[0])
                self.selectedtitle = DBNAME[0]
            print("The selected DB: " + self.selection)
            #print(selection)
            self.changePage()
        else:
            print("Nothing selected")

    def changePage(self):
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum == 1:
            self.contentspage()
            self.pagenum = 2
        else:
            self.mainpage()
            self.pagenum = 1

    def mainpage(self):
        root.title("My Window Class")
        root.minsize(200,150)
        self.db_path = "./DB/"
        self.db_list = dataset.getDataSet(self.db_path)

        content = ttk.Frame(root)
        self.window = content

        #center_frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=350, height=300)
        label = ttk.Label(content, text="Select DB", font=("Arial", 12))
        combo = ttk.Combobox(content, width=20, values=self.db_list, font=("Arial", 9))
        button = ttk.Button(content, text="Select", command=self.dbselected)

        content.grid(column=0, row=0, sticky=(N,W,E,S))
        #center_frame.grid(column=1, row=0, columnspan=1, rowspan=3, pady=10, sticky=(N, W, E, S))
        label.grid(column=1, row=0, padx=10, pady=10, sticky=S)
        combo.grid(column=1, row=1,  padx=10, pady=10)
        button.grid(column=1, row=2, padx=10, pady=10)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=0)
        content.columnconfigure(1, weight=1)
        content.columnconfigure(2, weight=0)
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)
        content.rowconfigure(2, weight=1)


    def contentspage(self):
        root.title("New page")
        root.minsize(500,300)
        content = ttk.Frame(root)
        self.window = content
        db_title_label = ttk.Label(content, text=self.selectedtitle, font=("Arial", 18))
        blankframe1 = ttk.Frame(content, height=300, width=50, relief="ridge")
        blankframe2 = ttk.Frame(content, height=300, width=50, relief="ridge")
        centerframe = ttk.Frame(content, height=300, width=300, relief="ridge")
        back_btn = ttk.Button(content, text="<", command=self.changePage, width=4)

        content.grid(column=0, row=0, sticky=(N,W,E,S))
        back_btn.grid(column=1, row=1, sticky=(N,W))
        blankframe1.grid(column=1, row=2, rowspan=3, sticky=(N,W,E,S), pady=(0,20))
        blankframe2.grid(column=4, row=2, rowspan=3, sticky=(N,W,E,S), pady=(0,20))
        centerframe.grid(column=2, row=2, columnspan=2, rowspan=3, sticky=(N,W,E,S), pady=(0,20))
        db_title_label.grid(column=2, row=1, columnspan=2)
        root.columnconfigure(0,weight=1)
        root.rowconfigure(0,weight=1)

        content.columnconfigure(1, weight=1)
        content.columnconfigure(2, weight=1)
        content.columnconfigure(3, weight=1)
        content.columnconfigure(4, weight=1)
        content.rowconfigure(1, weight=0)
        content.rowconfigure(2, weight=1)
        content.rowconfigure(3, weight=1)
        content.rowconfigure(4, weight=1)

        path = self.db_path + self.selection
        #print(path)
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
        cur.execute(sql_query)
        for row in cur:
            print(row)
            


class dataset:
    def getDataSet(path):
        DBPATH = path
        dblist = []
        for filepath in os.listdir(DBPATH):
            file = filepath.split('.')
            if file[1] == "db":
                #print(filepath + " is a .db file")
                dblist.append(filepath)

        return dblist

root = Tk()
MainWindow(root)
root.mainloop()
