from tkinter import Tk, Entry, Button, filedialog, DISABLED, END, NORMAL, messagebox
from bleaching import bleach

def choose_input_file():
    file = filedialog.askopenfilename(title="Выберите изображение",
        filetypes=[("", "*.bmp")])
    global file_input
    file_input = file
    name = file.split('/')[-1]
    entry_input.config(state=NORMAL)
    entry_input.delete(0, END)
    entry_input.insert(0, name)
    entry_input.config(state=DISABLED)

def choose_output_file():
    file = filedialog.asksaveasfilename(title="Выберите изображение",
        filetypes=[("", "*.bmp")])
    global file_output
    file_output = file
    name = file.split('/')[-1]
    if len(name.split('.')) < 2 and file:
        name += '.bmp'
        file_output += '.bmp'
    entry_output.config(state=NORMAL)
    entry_output.delete(0, END)
    entry_output.insert(0, name)
    entry_output.config(state=DISABLED)

def work():
    if file_output and file_input:
        bleach(file_input, file_output)
        messagebox.showinfo('Успешно',  ' Файл успешно сохранен')
    else:
        messagebox.showerror('Ошибка', 'Укажите все имена файлов')

window = Tk()
window.title('Марчуков Антон ИУ7-25Б Защита')
window.geometry('700x700+400+50')

file_input = ''
file_output = ''

btn_input_file = Button(font=('Arial', 14), justify='center', text='Выбор входного файла', command=choose_input_file)
btn_input_file.place(relx=.05, rely=.2, relheight=.1, relwidth=0.4)

btn_output_file = Button(font=('Arial', 14), justify='center', text='Выбор выходного файла', command=choose_output_file)
btn_output_file.place(relx=.5, rely=.2, relheight=.1, relwidth=0.4)

entry_output = Entry(justify='center', font=("Arial", 14), state=DISABLED)
entry_output.place(relx=.5, rely=.4, relheight=.1, relwidth=.4)

entry_input = Entry(justify='center', font=("Arial", 14), state=DISABLED)
entry_input.place(relx=.05, rely=.4, relheight=.1, relwidth=.4)

btn_res = Button(font=('Arial', 14), justify='center', text='Вычислить', command=work)
btn_res.place(relx=.05, rely=.6, relheight=.1, relwidth=.4)

window.mainloop()