# # Марчуков Антон ИУ7-25Б
# # Лабораторная 3. Сокрытие строки в изображение
#
# from tkinter import Tk, filedialog, Entry, Button, Label, END, messagebox
# from hide import string_to_img
# from seek import img_to_string
#
#
# # Инициализация окна
# window = Tk()
# window.geometry('600x600+400+50')
# window.title('Марчуков Антон ИУ7-25')
#
# # смена режима
# def change():
#     global mode
#     if mode == 1:
#         change_to_seek()
#         mode = 0
#     else:
#         change_to_hide()
#         mode = 1
#
# # размещение виджетов для скрытия строки
# def change_to_hide():
#     entry_string_seek.place_forget()
#     btn_input_seek.place_forget()
#     btn_res_seek.place_forget()
#     btn_clear_seek.place_forget()
#     label_string_seek.place_forget()
#     label_input_seek.place_forget()
#
#     entry_string.place(relx=.6, rely=.1, relheight=.1, relwidth=0.3)
#     label_string.place(relx=.05, rely=.1, relheight=0.1, relwidth=0.5)
#     label_input.place(relx=.05, rely=.3, relheight=0.1, relwidth=0.5)
#     btn_input.place(relx=.6, rely=.3, relheight=.1, relwidth=0.3)
#     label_output.place(relx=.04, rely=.5, relheight=0.1, relwidth=0.55)
#     btn_output.place(relx=.6, rely=.5, relheight=.1, relwidth=0.3)
#     btn_res.place(relx=.05, rely=.7, relheight=.1, relwidth=0.3)
#     btn_clear.place(relx=.4, rely=.7, relheight=.1, relwidth=0.3)
#
# # размещение виджетов для расшифровки строки
# def change_to_seek():
#     entry_string.place_forget()
#     label_string.place_forget()
#     label_input.place_forget()
#     btn_input.place_forget()
#     label_output.place_forget()
#     btn_output.place_forget()
#     btn_res.place_forget()
#     btn_clear.place_forget()
#
#     label_input_seek.place(relx=.05, rely=.1, relheight=0.1, relwidth=0.5)
#     entry_string_seek.place(relx=.6, rely=.3, relheight=.1, relwidth=0.3)
#     label_string_seek.place(relx=.05, rely=.3, relheight=0.1, relwidth=0.5)
#     btn_res_seek.place(relx=.05, rely=.5, relheight=.1, relwidth=0.3)
#     btn_clear_seek.place(relx=.4, rely=.5, relheight=.1, relwidth=0.3)
#     btn_input_seek.place(relx=.6, rely=.1, relheight=.1, relwidth=0.3)
#
# # выбор файла для сокрытия
# def choose_input_file():
#     global file_input
#     # имя файла
#     file_input = filedialog.askopenfilename(
#         title="Выберите изображение",
#         filetypes=[("", "*.bmp")])
#     if file_input != '':
#         # отображение только самого названия файла
#         name = file_input.split('/')[-1]
#         btn_input.config(text=name)
#     else:
#         btn_input.config(text='Выберите файл')
#
# # выбор выходного файла
# def choose_output_file():
#     global file_output
#     file_output = filedialog.asksaveasfilename(
#         title="Выберите изображение",
#         filetypes=[("", "*.bmp")])
#     if file_output != '':
#         name = file_output.split('/')[-1]
#         # добавление формата для файла, при его отсутствие
#         if len(name.split('.')) < 2:
#             name += '.bmp'
#             file_output += '.bmp'
#         btn_output.config(text=name)
#     else:
#         btn_output.config(text='Выберите файл')
#
# # выбор входного файла для расшифровки
# def choose_input_seek_file():
#     global file_input_seek
#     file_input_seek = filedialog.askopenfilename(
#         title="Выберите изображение",
#         filetypes=[("", "*.bmp")])
#     if file_input_seek != '':
#         name = file_input_seek.split('/')[-1]
#         btn_input_seek.config(text=name)
#     else:
#         btn_input_seek.config(text='Выберите файл')
#
# # очистка всех изменяемых виджетов
# def clear():
#     global file_output, file_input
#     file_input = 'Выберите файл'
#     file_output = 'Выберите файл'
#
#     btn_output.config(text=file_output)
#     btn_input.config(text=file_input)
#
#     entry_string.delete(0, END)
# # очистка всех изменяемых виджетов в режиме извлечения строки
# def clear_seek():
#     global file_input_seek
#     file_input_seek = 'Выберите файл'
#
#     btn_input_seek.config(text=file_input_seek)
#
#     entry_string_seek.delete(0, END)
#
# # выполнение скрытие строки
# def hide():
#     string = entry_string.get()
#     # обработка ошибок связанных с не определением нужных полей
#     if not string:
#         messagebox.showerror('ОШИБКА', "Введите пожалуйста строку")
#         return
#     elif file_input == 'Выберите файл':
#         messagebox.showerror('ОШИБКА', "Выберите файл для сокрытия")
#         return
#     elif file_output == 'Выберите файл':
#         messagebox.showerror('ОШИБКА', "Выберите файл для сохранения результата")
#         return
#     # скрытие
#     result = string_to_img(string, file_input, file_output)
#     # ошибки возникшее при скрытии
#     if result == 3:
#         messagebox.showerror('ОШИБКА', "Первый символ введеной строки не должен являться числом")
#     elif result == 2:
#         messagebox.showerror('ОШИБКА', "Файл для сокрытия должен иметь формат bmp")
#     elif result == 1:
#         messagebox.showerror('ОШИБКА', "Введенную строку невозможно сокрыть")
#     else:
#         messagebox.showinfo('Успешно', 'Изображение успешно сохранено')
#
# # расшифровка
# def seek():
#     if file_input_seek == 'Выберите файл':
#         messagebox.showerror('ОШИБКА', "Введите файл для извлечения строки")
#         return
#
#     # Расшифровка
#     result = img_to_string(file_input_seek)
#     # Ошибки возникшее при выполнении расшифровки
#     if type(result) == int:
#         if result == 2:
#             messagebox.showerror('ОШИБКА', "Файл для извлечения должен иметь формат bmp")
#         else:
#             messagebox.showerror('ОШИБКА', "В выбранном файле нет сокрытой строки")
#     else:
#         entry_string_seek.delete(0, END)
#         entry_string_seek.insert(0, result)
#
# # базовые надписи на кнопках
# file_input = 'Выберите файл'
# file_output = 'Выберите файл'
# file_input_seek = 'Выберите файл'
#
#
# # Создание виджетов для окна скрытия
# entry_string = Entry(justify='center', font=("Arial", 14))
#
# label_string = Label(text='''Введите строку,
# которую хотите сокрыть: ''', font=("Arial", 14))
#
# label_input = Label(text='''Выберите изображение,
#  в котором хотите сокрыть строку: ''', font=("Arial", 14))
#
# btn_input = Button(font=('Arial', 14), justify='center', text=file_input, command=choose_input_file)
#
# label_output = Label(text='''Выберите изображение,
#  в котором хотите получить результат: ''', font=("Arial", 14))
#
# btn_output = Button(font=('Arial', 14), justify='center', text=file_output, command=choose_output_file)
#
# btn_res = Button(font=('Arial', 14), justify='center', text='Вычислить', command=hide)
#
# btn_clear = Button(font=('Arial', 14), justify='center', text='Сбросить', command=clear)
#
# # Создание виджетов для окна расшифровки
# label_input_seek = Label(text='''Выберите изображение,
#  в котором хотите сокрыть строку: ''', font=("Arial", 14))
#
# btn_input_seek = Button(font=('Arial', 14), justify='center', text=file_input, command=choose_input_seek_file)
#
# entry_string_seek = Entry(justify='center', font=("Arial", 14))
#
# label_string_seek = Label(text='''Полученная строка: ''', font=("Arial", 14))
#
# btn_res_seek = Button(font=('Arial', 14), justify='center', text='Вычислить', command=seek)
#
# btn_clear_seek = Button(font=('Arial', 14), justify='center', text='Сбросить', command=clear_seek)
#
# # Заполнение окна. Режим скрытия
# mode = 1
# change_to_hide()
# btn_change = Button(font=('Arial', 14), justify='center', text='Смена режима', command=change)
# btn_change.place(relx=.05, rely=.83, relheight=.1, relwidth=0.3)
#
#
#
#
# window.mainloop()