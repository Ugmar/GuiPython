from tkinter import Tk, Button, Entry
from main2 import func


def run_func():
    a = int(entry1.get())
    k = int(entry2.get())
    res, digit = func(a, k)
    if res:
        entry3.insert(0, f'{res}   {digit}')
    else:
        entry3.insert(0, f'{res}')
    
window = Tk()
window.geometry('700x700')
btn =  Button(text='Вычислить', command=run_func)
btn.place(relx=.5, rely=.5, relheight=.05, relwidth=.3)
entry1 = Entry()
entry1.place(relx=.1, rely=.5)
entry2 = Entry()
entry2.place(relx=.1, rely=.6)
entry3 = Entry()
entry3.place(relx=.1, rely=.7)


window.mainloop()
