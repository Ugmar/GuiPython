from tkinter import Tk, Entry, Button, Label, messagebox, ttk, END
from tkinter.font import Font
from logic import main_logic


# Проверка введенных данных
def correct_input(s):
    s = s.replace('e-', '', 1).replace('e+', '', 1).replace('e', '', 1).replace('.', '', 1)
    if s == '':
        return False
    if s[0] == '-':
        s = s[1:]
    return s.isdigit()

# Убирает все пробелы в функциях
def normal_form_func(s):
    return ''.join(s.split())

# Информация о кодах ошибки
def info():
    messagebox.showinfo('Code Error', '''# Код ошибки 0 - корень найден успешно
# Код ошибки 1 - Лимит итераций
# Код ошибки 2 - Деление на 0
# Код ошибки 3 - Выход из ОДЗ
''')

# Функция выполнения основной части
def work():
    # Получение данных от пользователя
    a = entry_a.get()
    b = entry_b.get()
    h = entry_h.get()
    eps = entry_eps.get()
    nmax = entry_nmax.get()
    y_0 = entry_func.get()
    y_1 = entry_derivative1.get()
    y_2 = entry_derivative2.get()

    # Проверка на корректность
    if (not correct_input(a) or not correct_input(b) or not correct_input(h) or not correct_input(eps)
            or not nmax.isdigit() or y_0 == '' or y_1 == '' or y_2 == ''):
        messagebox.showerror('Ошибка', 'Пожалуйста, заполните все поля корректно')
    else:
        a, b, h, eps = map(float, (a, b, h, eps))
        nmax = int(nmax)

        # Проверка на корректность
        if not b > a:
            messagebox.showerror('Ошибка', 'Конец отрезка должен быть больше начала')
        elif not 0 < eps < 1:
            messagebox.showerror('Ошибка', 'Eps принадлежать (0, 1)')
        elif not nmax > 0:
            messagebox.showerror('Ошибка', 'Максимальное количество операция это натуральное число')
        elif not h > 0:
            messagebox.showerror('Ошибка', 'Шаг разбиения это натуральное число')
        else:
            try:
                # Получение списка корней
                result = main_logic(a, b, h, eps, nmax,
                                    normal_form_func(y_0), normal_form_func(y_1), normal_form_func(y_2))

                # Создание таблицы
                columns = ('number', 'section', 'x', 'f(x)', 'count it', 'error')
                table = ttk.Treeview(columns=columns, show="headings")
                table.place(relx=.02, rely=.2, relheight=.5, relwidth=.9)

                # Создание шрифта для таблицы
                font = Font(family='Arial', size=14)

                # Заполнение заголовков
                for name in columns:
                    table.heading(name, text=name)

                # Создание столбцов таблицы
                table.column("#1", width=40, anchor='c')
                table.column("#2", width=200, anchor='c')
                table.column("#3", width=100, anchor='c')
                table.column("#4", width=100, anchor='c')
                table.column("#5", width=40, anchor='c')
                table.column("#6", width=40, anchor='c')

                # Заполнение таблицы
                for value in result:
                    if value[-1] == 0:
                        value = (value[0], f'[{value[1][0]:.6f} : {value[1][1]:.6f}]', f'{value[2]:.6f}',
                                 value[3], value[4], value[5])
                    else:
                        value = (value[0], f'[{value[1][0]:.6f} : {value[1][1]:.6f}]', value[2],
                                 value[3], value[4], value[5])
                    table.insert("", END, values=value)

                # Обновление шрифтов в таблице
                table.tag_configure('custom', font=font)
                for item in table.get_children():
                    table.item(item, tags=('custom',))

            except (SyntaxError, NameError):
                messagebox.showerror('Ошибка', 'Введена функция с не известными параметрами')


window = Tk()
window.geometry('700x700+400+50')
window.title('Лабораторная работа 2 Марчуков Антон')

# Ввод функции
entry_func = Entry(justify='center', font=("Arial", 14))
entry_func.place(relx=.12, rely=.04, relheight=.03, relwidth=0.2)
label_func = Label(text='  f(x)=', font=("Arial", 14))
label_func.place(relx=.04, rely=.04, relheight=0.03, relwidth=0.07)

# Первая производная
entry_derivative1 = Entry(justify='center', font=("Arial", 14))
entry_derivative1.place(relx=.12, rely=.09, relheight=.03, relwidth=0.2)
label_derivative1 = Label(text="f `(x)=", font=("Arial", 14))
label_derivative1.place(relx=.04, rely=.09, relheight=0.03, relwidth=0.07)

# Вторая производная
entry_derivative2 = Entry(justify='center', font=("Arial", 14))
entry_derivative2.place(relx=.12, rely=.14, relheight=.03, relwidth=0.2)
label_derivative2 = Label(text="f ``(x)=", font=("Arial", 14))
label_derivative2.place(relx=.03, rely=.14, relheight=0.03, relwidth=0.08)

# Начало отрезка
entry_a = Entry(justify='center', font=("Arial", 14))
entry_a.place(relx=.39, rely=.04, relheight=.03, relwidth=0.1)
label_a = Label(text="a =", font=("Arial", 14))
label_a.place(relx=.33, rely=.04, relheight=0.03, relwidth=0.06)

# Конец отрезка
entry_b = Entry(justify='center', font=("Arial", 14))
entry_b.place(relx=.39, rely=.09, relheight=.03, relwidth=0.1)
label_b = Label(text="b =", font=("Arial", 14))
label_b.place(relx=.33, rely=.09, relheight=0.03, relwidth=0.06)

# Шаг деления отрезка
entry_h = Entry(justify='center', font=("Arial", 14))
entry_h.place(relx=.39, rely=.14, relheight=.03, relwidth=0.1)
label_h = Label(text="h =", font=("Arial", 14))
label_h.place(relx=.33, rely=.14, relheight=0.03, relwidth=0.06)

# Nmax
entry_nmax = Entry(justify='center', font=("Arial", 14))
entry_nmax.place(relx=.6, rely=.04, relheight=.03, relwidth=0.1)
label_nmax = Label(text="Nmax =", font=("Arial", 14))
label_nmax.place(relx=.5, rely=.04, relheight=0.03, relwidth=0.09)

# EPS
entry_eps = Entry(justify='center', font=("Arial", 14))
entry_eps.place(relx=.6, rely=.09, relheight=.03, relwidth=0.1)
label_eps = Label(text="EPS =", font=("Arial", 14))
label_eps.place(relx=.505, rely=.09, relheight=0.03, relwidth=0.09)

# Кнопка вычисления
button = Button(font=('Arial', 14), justify='center', text='Вычислить', command=work)
button.place(relx=.72, rely=.05, relheight=0.05, relwidth=0.25)

# Кнопка для вывода информации о кодах ошибки
button_info = Button(font=('Arial', 14), justify='center', text='Справка', command=info)
button_info.place(relx=.72, rely=.12, relheight=0.05, relwidth=0.25)

window.mainloop()
