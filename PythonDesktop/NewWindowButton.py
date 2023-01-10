import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('My First App')
root.geometry("400x400")

def OpenNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("300x300")
    Label(newWindow,
        text='This is a new window').pack()

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='This is the main window')
button1 = ttk.Button(
    frame1,
    text='New Window',
    command=OpenNewWindow)

# レイアウト
frame1.pack()
label1.pack(side=TOP)
button1.pack(side=BOTTOM)

# ウィンドウの表示開始
root.mainloop()
