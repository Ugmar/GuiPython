from tkinter import Tk, Button, Entry, Label, Menu, messagebox, END
from main import ternary_summation, ternary_subtraction

# Вызов окна "информации"
def info_click():
    messagebox.showinfo("Информация",
                        "Выполнил Марчуков Антон. Группа ИУ7-25Б. "
                        "Программа написана на языке программирования Python. "
                        "Для реализации интерфейса используется библиотека Tkinter. "
                        "Работа программы: Сложение и вычитание вещественных чисел в 3-й симметричной системе счисления.")

# Очистка всех полей
def clear_all():
    entry_input_a.delete(0, END)
    entry_input_b.delete(0, END)
    entry_result.delete(0, END)
    entry_result.insert(0, 'Result')

# Очистка поля для числа а
def clear_entry_a():
    entry_input_a.delete(0, END)

# Очистка поля для числа b
def clear_entry_b():
    entry_input_b.delete(0, END)

# Проверка валидности введенного числа
def check(string):
    if string == '':
        messagebox.showerror("ОШИБКА", 'Пустая строка')
        return False
    if string.count('.') > 1:
        messagebox.showerror("ОШИБКА", f'В числе {string} 2 или больше точек')
        return False
    for i in string:
        if i != '+' and i != '-' and i != '0' and i != '.':
            messagebox.showerror("ОШИБКА", f'В числе {string} содержатся символы не из алфавита')
            return False
    return True

# Вычисление суммы и обновление поля результата
def get_sum():
    a = entry_input_a.get()
    b = entry_input_b.get()
    if check(a) and check(b):
        result = ternary_summation(a, b)
        entry_result.delete(0, END)
        entry_result.insert(0, result)

# Вычисление разности и обновление поля результата
def get_sub():
    a = entry_input_a.get()
    b = entry_input_b.get()
    if check(a) and check(b):
        result = ternary_subtraction(a, b)
        entry_result.delete(0, END)
        entry_result.insert(0, result)

# Реализация клавиатуры допустимого алфавита
def print_el(event):
    # считывание текста на кнопке
    text = event.widget.cget('text')
    # Находим виджет в, котором необходимо внести изменения и производим его
    focus = window.focus_get()
    if focus == entry_input_a:
        entry_input_a.insert(entry_input_a.index('insert'), text)
    elif focus == entry_input_b:
        entry_input_b.insert(entry_input_b.index('insert'), text)
    else:
        entry_result.insert(entry_result.index('insert'), text)

# Стирание последнего введенного символа
def backspace():
    focus = window.focus_get()
    if focus == entry_input_a:
        entry_input_a.delete(len(entry_input_a.get()) - 1, END)
    elif focus == entry_input_b:
        entry_input_b.delete(len(entry_input_b.get()) - 1, END)
    else:
        entry_result.delete(len(entry_result.get()) - 1, END)


# Главное окно
window = Tk()
window.geometry('700x700+400+50')
window.title('Лабораторная №1 Марчуков А.И.')

# Меню для основной работы программы
work_menu = Menu(tearoff=0)
work_menu.add_command(label="Summation", command=get_sum)
work_menu.add_command(label="Subtraction", command=get_sub)

# Меню для очистки
clear_menu = Menu(tearoff=0)
clear_menu.add_command(label="Clear all", command=clear_all)
clear_menu.add_command(label="Clear number a", command=clear_entry_a)
clear_menu.add_command(label="Clear number b", command=clear_entry_b)

# Основное меню
main_menu = Menu()
main_menu.add_cascade(label="Work", menu=work_menu)
main_menu.add_cascade(label="Clear", menu=clear_menu)
main_menu.add_cascade(label="Info", command=info_click)

# Кнопка, обновляющая все поля
btn_clear_all = Button(text='clear all', background='#FF9999', font=10, command=clear_all)
btn_clear_all.place(relheight=.05, relwidth=.65, relx=.19, rely=.92)

# Поле вывода результата
entry_result = Entry(justify='center', background='#99FF99', font=10)
entry_result.insert(0, 'Result')
entry_result.place(relheight=.05, relwidth=.65, relx=.19, rely=.85)
# Поле ввода числа а
entry_input_a = Entry(justify='center', background='#3399FF', font=10)
entry_input_a.place(relheight=.05, relwidth=.25, relx=.19, rely=.3)
entry_input_a.focus()
# Текст для дополнительной информации
label_a = Label(text="Enter the number a", font=('Arial', 12), background='#CCCCFF')
label_a.place(relheight=.03, relwidth=.25, relx=.19, rely=.27)
# Поле ввода числа b
entry_input_b = Entry(justify='center', background='#3399FF', font=10)
entry_input_b.place(relheight=.05, relwidth=.25, relx=.6, rely=.3)
# Текст для дополнительной информации
label_b = Label(text="Enter the number b", font=('Arial', 12), background='#CCCCFF')
label_b.place(relheight=.03, relwidth=.25, relx=.6, rely=.27)
# Кнопка очистки поля для числа а
btn_clear_a = Button(text='clear', background='#FF9999', font=10, command=clear_entry_a)
btn_clear_a.place(relheight=.05, relwidth=.25, relx=.19, rely=.37)
# Кнопка очистки поля для числа b
btn_clear_b = Button(text='clear', background='#FF9999', font=10, command=clear_entry_b)
btn_clear_b.place(relheight=.05, relwidth=.25, relx=.6, rely=.37)
# Кнопка получение результата суммирования
btn_summation = Button(text='a + b', background='#A0A0A0', font=10, command=get_sum)
btn_summation.place(relheight=.1, relwidth=.35, relx=.35, rely=.5)
# Текст для дополнительной информации
label_sum = Label(text="Summation a and b", font=('Arial', 12), background='#CCCCFF')
label_sum.place(relheight=.03, relwidth=.25, relx=.37, rely=.47)
# Кнопка для получения результата вычитания
btn_subtraction = Button(text='a - b', background='#A0A0A0', font=10, command=get_sub)
btn_subtraction.place(relheight=.1, relwidth=.35, relx=.35, rely=.7)
# Текст для дополнительной информации
label_sub = Label(text="Subtraction a and b", font=('Arial', 12), background='#CCCCFF')
label_sub.place(relheight=.03, relwidth=.25, relx=.37, rely=.67)
# Кнопка печати "+" в текущем поле
btn_plus = Button(text='+', background='#9933FF', font=10)
btn_plus.place(relheight=0.05, relwidth=0.05, relx=.4, rely=.15)
btn_plus.bind('<Button-1> ', print_el)
# Кнопка печати "-" в текущем поле
btn_minus = Button(text='-', background='#9933FF', font=10)
btn_minus.place(relheight=0.05, relwidth=0.05, relx=.47, rely=.15)
btn_minus.bind('<Button-1> ', print_el)
# Кнопка печати "0" в текущем поле
btn_zero = Button(text='0', background='#9933FF', font=10)
btn_zero.place(relheight=0.05, relwidth=0.05, relx=.54, rely=.15)
btn_zero.bind('<Button-1> ', print_el)
# Кнопка печати "." в текущем поле
btn_dot = Button(text='.', background='#9933FF', font=10)
btn_dot.place(relheight=0.05, relwidth=0.05, relx=.61, rely=.15)
btn_dot.bind('<Button-1> ', print_el)
# Текст для дополнительной информации
label_alphabet = Label(text="Alphabet: ", font=('Arial', 12), background='#CCCCFF')
label_alphabet.place(relheight=.03, relwidth=.1, relx=.27, rely=.16)
# Кнопка для стирания последнего элемента
btn_backspace = Button(text='Backspace', background='#9933FF', font=10, command=backspace)
btn_backspace.place(relheight=0.05, relwidth=0.2, relx=.75, rely=.15)

window.config(background='#CCCCFF', menu=main_menu)
window.mainloop()
