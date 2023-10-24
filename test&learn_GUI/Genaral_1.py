from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.geometry("500x300")

def callback(event):
   print("clicked at", event.x, event.y)

def quit(event):
   print("Double clicked")
   frame.quit()

def A() : print("A")
def B() : print("B")
def C() : print("C")


frame = tk.Frame(root, bg="sky blue", width=300, height=300)
frame.bind("<Button-1>", callback) #คลิ้กเม้าส์
frame.bind("<Double-1>", quit) #ดับเบิ้ลคลิ้ก
#frame.bind("<Enter>", A) #ลากเม้าเข้าบริเวณนั้นๆ
frame.pack()

a = tk.Button(frame, text="This is ""A""!!", command=A).pack()
b = tk.Button(frame, text="This is ""B""!!", command=B).pack(side=LEFT)
c = tk.Button(frame, text="This is ""c""!!", command=C).pack(side=BOTTOM)


root.mainloop()