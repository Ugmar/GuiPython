# Марчуков Антон ИУ7-25Б. Защита 4
from tkinter import Tk, Canvas, Button, ALL
from logic import search_triangles

WIDTH = 700
HEIGHT = 700
SIZE = 5
COLOR_DOT = 'red'
COLOR_RES = 'blue'
list_triangle = []
point = []

def clear_all(canvas):
    canvas.delete(ALL)
    list_triangle.clear()
    point.clear()

def draw_point(event, canvas, point, list_triangle):
    x, y = event.x, event.y
    canvas.create_oval(x - SIZE, y - SIZE, x + SIZE, y + SIZE, fill=COLOR_DOT, outline=COLOR_DOT)

    point.append((x, y))
    if len(point) == 3:
        canvas.create_polygon(*point[0], *point[1], *point[2],
                              outline=COLOR_DOT, fill='')
        list_triangle.append(tuple(point))
        point.clear()

def search_result(list_triangle):
    triangle_1, triangle_2 = search_triangles(list_triangle)
    canvas.create_polygon(*triangle_1[0], *triangle_1[1], *triangle_1[2],
                          outline=COLOR_RES, fill='')

    canvas.create_polygon(*triangle_2[0], *triangle_2[1], *triangle_2[2],
                          outline=COLOR_RES, fill='')

window = Tk()
window.title('Марчуков Антон ИУ7-25Б Защита 4')
window.geometry(f'{WIDTH}x{HEIGHT}+400+50')

canvas = Canvas(window, bg='#e5dcdc')
canvas.place(relx=.0, rely=.0, relwidth=1, relheight=.4)
canvas.bind("<Button-1>", lambda event: draw_point(event, canvas, point, list_triangle))

btn_res = Button(text='Получить результат', command=lambda : search_result(list_triangle))
btn_res.place(relx=.0, rely=.44, relwidth=.2, relheight=.07)

btn_res = Button(text='Очистить', command=lambda : clear_all(canvas))
btn_res.place(relx=.22, rely=.44, relwidth=.2, relheight=.07)

window.mainloop()
