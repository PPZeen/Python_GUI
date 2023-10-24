from tkinter import  *
from tkinter import messagebox
import tkinter as tk

items = {"Water":7, "Congee":30, "Papaya Salad":40, "Fried Rice":45, "Chicken fried":60, "Zoju":100, "Pork fried":60,\
         "Steak":150, "Ramyon":70}

class Order :
    def __init__(self):
        self.orders = {} # list of tuple
    def add(self, fname, amount):
        if fname in items.keys() :
            if fname not in self.orders :
                self.orders[fname] = amount
            else : self.orders[fname] += amount
            print(f"add {amount} {fname}")
        else:
            print(f"{fname} not in items")
    def get_total(self):
        return sum([items[fname]*amount for fname, amount in list(self.orders.items())])
    def __str__(self):
        return "\n".join([fname+": "+str(amount) for fname, amount in list(self.orders.items())])

def add_water():mylist.insert(END,f"Water               x1") ; order.add("Water", 1)
def add_congee(): mylist.insert(END,f"Congee             x1") ; order.add("Congee", 1)
def add_ppysl(): mylist.insert(END,f"Papaya Salad        x1") ; order.add("Papaya Salad", 1)
def add_fried(): mylist.insert(END,f"Fried Rice          x1") ; order.add("Fried Rice", 1)
def add_chicken(): mylist.insert(END,f"Chicken fried     x1") ; order.add("Chicken fried", 1)
def add_pork(): mylist.insert(END,f"Pork fried           x1") ; order.add("Pork fried", 1)
def add_ramyon(): mylist.insert(END,f"Ramyon             x1") ; order.add("Ramyon", 1)
def add_zoju(): mylist.insert(END,f"Zoju                 x1") ; order.add("Zoju", 1)
def add_steak(): mylist.insert(END,f"Steak               x1") ; order.add("Steak", 1)

def bill() : messagebox.showinfo("BILL", f"{order}\ntotal food cost : {order.get_total()} THB")

order = Order() # Open new order

root = Tk()
root.title("Order food")
root.geometry("350x600")

frame = Frame(root, bg="pink", width=270, height=160).place(x=25, y=20)
low_frame = Frame(root, bg="sky blue", width=300, height=380).place(x=25, y=200)
#------------------------------------------------------------------------------------
mylist = Listbox(frame, font=("Angsana New",13), width=45, height=7, selectmode=MULTIPLE)
mylist.grid(row=0, column=0, padx=25, pady=20)

scrollbar = Scrollbar(frame, command=mylist.yview)
scrollbar.grid(row=0, column=1,padx=0, pady=20, sticky=N+S)
mylist.config(yscrollcommand=scrollbar.set)
#-------------------------------------------------------------------------------------
Bwater = Label(low_frame, text="Water\n7 THB\n\n\n", width=10, height=5).place(x=37,y=210)
BFried = Label(low_frame, text="Fried Rice\n 45 THB\n\n\n", width=10, height=5).place(x=37,y=305)
BZoju = Label(low_frame, text="Zoju\n100 THB\n\n\n", width=10, height=5).place(x=37,y=400)
Bcongee = Label(low_frame, text="Condee\n 30 THB\n\n\n", width=10, height=5).place(x=135,y=210)
BChicken = Label(low_frame, text="Chicken fried\n 60 THB\n\n\n", width=10, height=5).place(x=135,y=305)
BRamyon = Label(low_frame, text="Ramyon\n 70 THB\n\n\n", width=10, height=5).place(x=135,y=400)
Bppysl = Label(low_frame, text="Papaya Salad\n 40 THB\n\n\n", width=10, height=5).place(x=233,y=210)
BPork = Label(low_frame, text="Pork fried\n60 THB\n\n\n", width=10, height=5).place(x=233,y=305)
BSteak = Label(low_frame, text="Steak\n 150 THB\n\n\n", width=10, height=5).place(x=233,y=400)
BBill = Button(low_frame, text="Bill", font=("Angsana New",18) ,command=bill, width=29, height=1).place(x=37,y=495)
#--------------------------------------------------------------------------------------
Awater = Button(low_frame, text="Add", width=6, height=1, command=add_water).place(x=50,y=260)
AFried = Button(low_frame, text="Add", width=6, height=1, command=add_fried).place(x=50,y=355)
AZoju = Button(low_frame, text="Add", width=6, height=1, command=add_zoju).place(x=50,y=450)
Acongee = Button(low_frame, text="Add", width=6, height=1, command=add_congee).place(x=148,y=260)
AChicken = Button(low_frame, text="Add", width=6, height=1, command=add_chicken).place(x=148,y=355)
ARamyon = Button(low_frame, text="Add", width=6, height=1, command=add_ramyon).place(x=148,y=450)
Appysl = Button(low_frame, text="Add", width=6, height=1, command=add_ppysl).place(x=246,y=260)
APork = Button(low_frame, text="Add", width=6, height=1, command=add_pork).place(x=246,y=355)
ASteak = Button(low_frame, text="Add", width=6, height=1, command=add_steak).place(x=246,y=450)
#---------------------------------------------------------------------------------------
root.mainloop()