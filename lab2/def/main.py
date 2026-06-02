# Марчуков Антон ИУ7-25Б

from tkinter import Tk, Entry, Button, Label, END
from logic import calc

def search_x():
    a = float(entry_a.get())
    b = float(entry_b.get())
    eps = float(entry_eps.get())
    x = f'{calc(a, b, eps)}'
    entry_res.delete(0, END)
    if x is None:
        entry_res.insert(0, 'Метод не сошелся за 1000 операций')
    else:
        entry_res.insert(0, x)

window = Tk()
window.geometry('700x700+400+50')

entry_a = Entry(justify='center')
entry_a.place(relx=.12, rely=.04, relheight=.03, relwidth=0.2)
label_a = Label(text='  A =')
label_a.place(relx=.04, rely=.04, relheight=0.03, relwidth=0.07)

entry_b = Entry(justify='center')
entry_b.place(relx=.12, rely=.14, relheight=.03, relwidth=0.2)
label_b = Label(text='  B =')
label_b.place(relx=.04, rely=.14, relheight=0.03, relwidth=0.07)

entry_eps = Entry(justify='center')
entry_eps.place(relx=.12, rely=.24, relheight=.03, relwidth=0.2)
label_eps = Label(text='  EPS =')
label_eps.place(relx=.04, rely=.24, relheight=0.03, relwidth=0.07)

btn = Button(justify='center', text='Вычислить', command=search_x)
btn.place(relx=.5, rely=.15, relheight=.03, relwidth=0.2)

entry_res = Entry(justify='center')
entry_res.place(relx=.12, rely=.34, relheight=.03, relwidth=0.2)
label_eps = Label(text='  RESULT =')
label_eps.place(relx=.04, rely=.34, relheight=0.03, relwidth=0.07)
window.mainloop()