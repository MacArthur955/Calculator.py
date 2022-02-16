from tkinter import *

def print_value(number):
    if not [x for x in entry.get() if x in '1234567890+-*/e.'] and entry.get(): return
    if number in "+-*/" and not entry.get(): return
    if number in "+-*/" and entry.get()[-1] in "+-*/": entry.delete(len(entry.get()) -1)
    entry.insert(END, number)
def equals():
    if not [x for x in entry.get() if x in '1234567890+-*/e.']: return
    try:
        result = eval(entry.get())
        if result > 999999999999999999999: result = '{:e}'.format(result)
    except ZeroDivisionError: result = 'Division by zero'
    except Exception: return
    entry.delete(0,END)
    entry.insert(0,result)
def configure_buttons():
    Button(text="C", command=lambda:entry.delete(0, END)).grid(row=4, column=1, stick=NSEW)
    Button(text="=", command= equals).grid(row=4, column=2, stick=NSEW)
    def create_Button(value): return Button(text=value, command=lambda: print_value(value))
    for i,r,c in zip('123+456-789*0/','11112222333344','01230123012303'):
        create_Button(i).grid(row=r, column=c, stick=NSEW)
    for i in range(0,4):
        root.columnconfigure(i, minsize=60)
        root.rowconfigure(i+1, minsize=60)

# System variables
root = Tk()
entry = Entry(root, font=('Arial', 15), justify = "right")
configure_buttons()

# Configuration
root.title('Calculator')
root.resizable(False, False)
entry.grid(row=0, column=0, columnspan=4, stick=EW)

# Main loop
root.mainloop()