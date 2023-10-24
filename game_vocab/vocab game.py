from tkinter import *
from tkinter import ttk
import random
import copy

# Open GUI
GUI = Tk()
GUI.title("Test tkineter Game")
GUI.geometry("500x300")

# Text on GUI
L1 = ttk.Label(GUI, text="Vocab Game", font=("Angsana New",20), foreground="Blue")
L1.pack()
L2 = ttk.Label(GUI, text="RULES", font=("Angsana New",12), foreground="Gray")
L2.place(x=15, y=40)
L3 = ttk.Label(GUI, text="1. กด \"ENG\" เพื่อสุ่มคำศัพท์", font=("Angsana New",12), foreground="Gray")
L3.place(x=15, y=65)
L4 = ttk.Label(GUI, text="2. พิมพ์ คำแปลลงในช่องว่าง", font=("Angsana New",12), foreground="Gray")
L4.place(x=15, y=90) 
L5 = ttk.Label(GUI, text="3. กด \"Check\" เพื่อตรวจคำตอบ", font=("Angsana New",12), foreground="Gray")
L5.place(x=15, y=115)
L6 = ttk.Label(GUI, text="Score :", font=("Angsana New",15), foreground="Red")
L6.place(x=400, y=0)

#  Text on GUI can be changed
EN = StringVar()
TH = StringVar()
CK = StringVar()
N = IntVar()

L2 = ttk.Label(GUI, textvariable=EN, font=("Angsana New",15))
L2.pack(pady=5)
EN.set("------")

L3 = ttk.Label(GUI, textvariable=TH, font=("Angsana New",15))
L3.pack(pady=5)
TH.set("------")

L4 = ttk.Entry(GUI, textvariable=CK, font=("Angsana New",15))
L4.pack(pady=10, ipadx=5, ipady=1)

L5 = ttk.Label(GUI, textvariable=N, font=("Angsana New",15), foreground="Red")
L5.place(x=460, y=0)
N.set(0)

def readVocab():
    results = {}
    f = open("Oxford_3000.txt", "r")
    
    for line in f:
        key, value = line.strip().split(" = ")
        value = [v.strip() for v in value.split(",")]
        results[key] = value
        
    return results

# function when press button
dicts = readVocab()
vocab = list(dicts.keys())
vocab2 = []
checked = False

def English() :
    EN.set(random.choice(vocab))
    TH.set("")
    CK.set("")
    
    global checked
    checked = False
    
    if len(vocab2) == 0 : N.set(0)
    
def Thai() :
    global checked
    global vocab
    global vocab2
    
    if EN.get() not in vocab : return
    TH.set(dicts[EN.get()])
    
    checked = True
    
    x = vocab.pop(vocab.index(EN.get()))
    vocab2.append(x)
    
def check() :
    global checked
    global vocab
    global vocab2
    
    if checked == True : return
    if L4.get() in dicts[EN.get()] :
        N.set(N.get()+1)
        TH.set(L4.get()+" ^-^")
        checked = True
        x = vocab.pop(vocab.index(EN.get()))
        vocab2.append(x) # make it unique random you have the correct word.
    else :
        an = ["ยังไม่ถูกนะ TT", "ลองใหม่อีกครั้งนะ", "พยายามอีกครั้งนะ", ""]
        TH.set(random.choice(an))
    if len(vocab) == 0 : # end game
        if N.get() == len(dicts) : 
            EN.set("Congreat")
            TH.set("You Win!!!!!!!!!")
        else :
            EN.set("Game Over")
            TH.set(f"Your score : {N.get()}")
        
        vocab = copy.deepcopy(vocab2)
        vocab2 = []

# Create Button, connect button to function, Draw Button on Frame
F = Frame(GUI)
F.pack()

B1 = ttk.Button(F, text= "ENG",command=English)
B1.grid(row=0, column=0,ipadx=20,ipady=10)

B2 = ttk.Button(F, text= "TH",command=Thai)
B2.grid(row=0, column=1,ipadx=20,ipady=10)

B3 = ttk.Button(F, text= "Check Answer",command=check)
B3.grid(row=0, column=2,ipadx=20,ipady=10)

GUI.mainloop()
