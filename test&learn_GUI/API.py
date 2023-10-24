from tkinter import *
import tkinter as tk
#import requests


root = Tk()
root.title("API")
root.geometry("800x500")

mail = StringVar()
row_mail = StringVar()

frame = tk.Frame(root, bg="Pink", width=500, height=50).place(x=150, y=50)
#frame.place(x=150, y=50)

B1 = tk.Button(frame, text="search",width=15, height=2, command=lambda: search(mail.get())).place(x=530, y=55)
#B1.place(x=530, y=55)

B2 = tk.Entry(frame, textvariable=mail, font=("Angsana New",20), width=40).place(x=155, y=55)
#B2.place(x=155, y=55)

low_frame = tk.Frame(root, bg="Pink", width=500, height=300).place(x=150, y=150)
#low_frame.place(x=150, y=150)

B3 = tk.Label(low_frame, anchor='nw', justify='left', textvariable=row_mail, font=("Angsana New",18), width=53, height=8).place(x=158, y=165)
#B3.place(x=155, y=155)

#-------------------------------------------------------------------------------------

def search(entry) :
    print(f"ข้อความคือ: {entry}")
    row_mail.set(f"ข้อความคือ: {entry}\nOne\ntwo\nthree")
root.mainloop()