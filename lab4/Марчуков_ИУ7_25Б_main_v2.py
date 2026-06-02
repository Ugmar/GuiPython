# Марчуков Антон ИУ7-25Б. Заданы два множества
# точек. Найти такой треугольник с вершинами – точками первого множества, внутри которого
# находится одинаковое количество точек из первого и из второго множеств.

from tkinter import Tk, Canvas, Button, Label, ttk, Entry, END, messagebox, ALL, Menu
from Марчуков_ИУ7_25Б_logic_v2 import search_triangle

# Инициализация констант

WIDTH = 700
HEIGHT = 700
COLOR_A = "RED"
COLOR_B = "BLUE"
COLOR_TRIANGLE = "GREEN"
SIZE = 5


# Функция для вывода найденного треугольника
def get_result(canvas, id_points_a, id_points_b, table):
    # Преобразование id в координаты
    points_a = id_to_coord(canvas, id_points_a)
    points_b = id_to_coord(canvas, id_points_b)

    # Поиск треугольника
    triangle = search_triangle(points_a, points_b)

    # Проверка на существование треугольника
    if triangle is None:
        clear_result(table, canvas)
        messagebox.showinfo('', 'Для данного набора точек невозможно определить искомый треугольник')
    else:

        # Очистка таблицы результата и предыдущего треугольника на холсте
        clear_result(table, canvas)

        # Заполнение таблицы вершинами треугольника
        for point in triangle:
            table.insert("", END, values=point)

        # Отрисовка треугольника на холста
        x1, y1 = triangle[0]
        x2, y2 = triangle[1]
        x3, y3 = triangle[2]
        canvas.create_polygon(x1, y1, x2, y2, x3, y3,
                              outline=COLOR_TRIANGLE, fill='', tags="last_triangle")


# Функция очистки всех полей. Фактические перезапуск программы
def clear_all(canvas, table_a, table_b, table_res, x_a, y_a, x_b, y_b, id_points_a, id_points_b):
    # Очистка холста
    canvas.delete(ALL)

    # Очистка таблиц, содержащих множества точек
    for item in table_a.get_children():
        table_a.delete(item)

    for item in table_b.get_children():
        table_b.delete(item)

    # Очистка полей ввода точек
    x_a.delete(0, END)
    y_a.delete(0, END)
    x_b.delete(0, END)
    y_b.delete(0, END)

    # Очистка списков, содержащих точки
    id_points_a.clear()
    id_points_b.clear()

    # Очистка найденного результата в таблице
    clear_result(table_res, canvas)


# Функция преобразования id точки в координаты
def id_to_coord(canvas, list_id):
    return list(map(lambda id: tuple(map(lambda cord: int(cord + SIZE), canvas.coords(id)))[:2], list_id))


# Функция очистки найденного результата в таблице
def clear_result(table, canvas):
    for item in table.get_children():
        table.delete(item)

    canvas.delete("last_triangle")


# Функция проверки введенных координат на корректность
def check_cords(x, y):
    # Проверка на пустые поля
    if not (x and y):
        return 1

    # Проверка на нечисловые данные
    if not (x.isdigit() and y.isdigit()):
        return 2

    # Проверка на ввод точек, больших размера холста
    width, height = window.winfo_width(), window.winfo_height()
    if int(x) > width or int(y) > height * 0.4:
        return 3

    return 0


# Функция отрисовки точки
def draw_point(canvas, point, color, list_id):
    x, y = point
    list_id.append(canvas.create_oval(x - SIZE, y - SIZE, x + SIZE, y + SIZE, fill=color, outline=color))


# Функция обновление таблицы множества точек
def update_table(table, point):
    table.insert("", END, values=point)


# Функция обновление холста и таблиц
def update_info(canvas, table, list_id, color, x, y):
    point = (x, y)
    if point in id_to_coord(canvas, list_id):
        messagebox.showerror('Ошибка', 'Данная точка уже отмечена')
    else:
        draw_point(canvas, point, color, list_id)
        update_table(table, point)


# Функция удаления точки
def delete_dot(canvas, table, list_id):
    selected_items = table.selection()
    if selected_items:
        for item in selected_items:
            cord = tuple(map(int, table.item(item, option="values")))
            index = id_to_coord(canvas, list_id).index(cord)

            canvas.delete(list_id[index])
            list_id.pop(index)
            table.delete(item)
    else:
        messagebox.showerror('Ошибка', "Пожалуйста выделите в таблице точку, которую хотите удалить")


# Функция для обработки нажатия на холсте
def canvas_add(canvas, table, event, list_id, color):
    update_info(canvas, table, list_id, color, event.x, event.y)


# Функция для добавления точки через кнопку
def button_add(canvas, table, x, y, list_id, color):
    rc = check_cords(x.get(), y.get())

    # Обработка результатов проверки
    if rc == 1:
        messagebox.showerror('ОШИБКА', 'Введите, пожалуйста все поля')
    elif rc == 2:
        messagebox.showerror('Ошибка',
                             'Во входных данных посторонние символы. Корректными являются только целочисленные числа')
    elif rc == 3:
        messagebox.showerror('Ошибка', 'Введенная точка находится за пределами холста.')
    else:
        update_info(canvas, table, list_id, color, int(x.get()), int(y.get()))


# Инициализация виджетов окна
def init_window():
    # Списки точек множества
    list_id_a = []
    list_id_b = []

    # Холст
    canvas = Canvas(window, bg='#e5dcdc')
    canvas.place(relx=.0, rely=.0, relwidth=1, relheight=.4)
    canvas.bind("<Button-1>", lambda event: canvas_add(canvas, table_dot_a, event, list_id_a, COLOR_A))
    canvas.bind("<Button-3>", lambda event: canvas_add(canvas, table_dot_b, event, list_id_b, COLOR_B))

    # Кнопка для поиска треугольника
    btn_res = Button(text='Посчитать результат', command=lambda: get_result(canvas, list_id_a, list_id_b, table_res))
    btn_res.place(relx=.0, rely=.41, relwidth=.2, relheight=.07)

    # Кнопка очистки всех данных
    btn_clear_all = Button(text='Очистить все', command=lambda: clear_all(canvas, table_dot_a, table_dot_b, table_res,
                                                                          entry_a_x, entry_a_y,
                                                                          entry_b_x, entry_b_y,
                                                                          list_id_a, list_id_b))
    btn_clear_all.place(relx=.21, rely=.41, relwidth=.2, relheight=.07)

    # Очистка результата
    btn_clear_res = Button(text='Очистить результат', command=lambda: clear_result(table_res, canvas))
    btn_clear_res.place(relx=.42, rely=.41, relwidth=.2, relheight=.07)

    # Надпись для удобства навигации
    label_res = Label(text='Результат:', background='#FFFFFF')
    label_res.place(relx=.63, rely=.41, relwidth=.09, relheight=.05)

    # Таблица результата
    columns = ('X', 'Y')
    table_res = ttk.Treeview(columns=columns, show="headings")
    table_res.place(relx=.73, rely=.41, relheight=.21, relwidth=.26)

    for name in columns:
        table_res.heading(name, text=name)

    table_res.column("#1", width=13, anchor='c')
    table_res.column("#2", width=13, anchor='c')

    # Надпись для удобства навигации
    label_set_a = Label(text='Точки множество A', background="#FFFFFF")
    label_set_a.place(relx=.03, rely=.5, relwidth=.2, relheight=.05)

    label_a_x = Label(text="X:", background="#FFFFFF")
    label_a_x.place(relx=.01, rely=.55, relwidth=.05, relheight=.05)

    label_a_y = Label(text="Y:", background="#FFFFFF")
    label_a_y.place(relx=.01, rely=.6, relwidth=.05, relheight=.05)

    # Поле ввода координат
    entry_a_x = Entry(background="#e5dcdc")
    entry_a_x.place(relx=.1, rely=.56, relwidth=.15, relheight=.03)

    entry_a_y = Entry(background="#e5dcdc")
    entry_a_y.place(relx=.1, rely=.61, relwidth=.15, relheight=.03)

    # Кнопка добавления точки
    btn_add_dot_a = Button(text='Добавить точку', command=lambda: button_add(canvas, table_dot_a, entry_a_x,
                                                                             entry_a_y, list_id_a, COLOR_A))
    btn_add_dot_a.place(relx=.1, rely=.66, relwidth=.15, relheight=.03)

    # Кнопка удаления точки
    btn_delete_dot_a = Button(text='Удалить точку', command=lambda: delete_dot(canvas, table_dot_a, list_id_a))
    btn_delete_dot_a.place(relx=.1, rely=.70, relwidth=.15, relheight=.03)

    # Надпись для удобства навигации
    label_set_b = Label(text='Точки множество B', background="#FFFFFF")
    label_set_b.place(relx=.4, rely=.5, relwidth=.2, relheight=.05)

    label_b_x = Label(text="X:", background="#FFFFFF")
    label_b_x.place(relx=.4, rely=.55, relwidth=.05, relheight=.05)

    label_b_y = Label(text="Y:", background="#FFFFFF")
    label_b_y.place(relx=.4, rely=.6, relwidth=.05, relheight=.05)

    # Поле ввода координат
    entry_b_x = Entry(background="#e5dcdc")
    entry_b_x.place(relx=.5, rely=.56, relwidth=.15, relheight=.03)

    entry_b_y = Entry(background="#e5dcdc")
    entry_b_y.place(relx=.5, rely=.61, relwidth=.15, relheight=.03)

    # Кнопка добавления точки
    btn_add_dot_b = Button(text='Добавить точку', command=lambda: button_add(canvas, table_dot_b, entry_b_x,
                                                                             entry_b_y, list_id_b, COLOR_B))
    btn_add_dot_b.place(relx=.5, rely=.66, relwidth=.15, relheight=.03)

    # Кнопка удаления точки
    btn_delete_dot_b = Button(text='Удалить точку', command=lambda: delete_dot(canvas, table_dot_b, list_id_b))
    btn_delete_dot_b.place(relx=.5, rely=.70, relwidth=.15, relheight=.03)

    # Таблица множества А
    table_dot_a = ttk.Treeview(columns=columns, show="headings")
    table_dot_a.place(relx=.01, rely=.75, relheight=.24, relwidth=.25)

    for name in columns:
        table_dot_a.heading(name, text=name)

    table_dot_a.column("#1", width=12, anchor='c')
    table_dot_a.column("#2", width=12, anchor='c')

    # Таблица множества B
    table_dot_b = ttk.Treeview(columns=columns, show="headings")
    table_dot_b.place(relx=.4, rely=.75, relheight=.24, relwidth=.25)

    for name in columns:
        table_dot_b.heading(name, text=name)

    table_dot_b.column("#1", width=12, anchor='c')
    table_dot_b.column("#2", width=12, anchor='c')


# Функция для меня, отображения информации
def info_program():
    messagebox.showinfo('Информация', '''Выполнил Марчуков Антон ИУ7-25Б. Лабораторная №4. Вариант: заданы два множества
точек. Найти такой треугольник с вершинами – точками первого множества, внутри которого 
находится одинаковое количество точек из первого и из второго множеств. ''')


# Функция для меня, отображения информации
def info_work():
    messagebox.showinfo('Информация',
                        '''Чтобы отобразить точки из первого множества, наведите курсор мыши на необходимую точку внутри холста и нажмите на ЛКМ.
Аналогичные действия проделываются для точек второго множества, только для их создания используется ПКМ. 
Так же точки Вы можете внести, используя таблицу. Введите координаты X и Y точки множества и нажмите на кнопку "Добавить точку". 
Чтобы удалить точку/точки выделите ее/их в соответствующей таблице и нажмите кнопку удалить точку.
Чтобы найти треугольник, нажмите на кнопку "Посчитать результат"
После на холсте отобразится найденный треугольник. В таблице-результате будут видны его координаты. 
При нахождение нового треугольника информация о старом будет удалена.''')


# Инициализация окна
window = Tk()
window.title('Марчуков Антон ИУ7-25Б Лаб 4')
window.geometry(f'{WIDTH}x{HEIGHT}+400+50')

init_window()

# Инициализация меню
menu = Menu()
menu.add_command(label="О программе", command=info_program)
menu.add_command(label="Как работать", command=info_work)

window.config(background='#FFFFFF', menu=menu)

window.mainloop()
