# Марчуков Антон ИУ7-25Б Лабораторная 5 защита
import pygame
from math import sin, cos, sqrt

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Марчуков Антон ИУ7-25Б защита")
a = 100
h = a * sqrt(3) / 2
t = (400, 300)
speed = 0.1
angle = 0

# Матрица поворота
def rotate_point(x_center, y_center, x, y, angle):
    rotated_x = (x - x_center) * cos(angle) - (y - y_center) * sin(angle) + x_center
    rotated_y = (x - x_center) * sin(angle) + (y - y_center) * cos(angle) + y_center
    return rotated_x, rotated_y

def draw_triangle(window, x, y, angle):
    x1, y1 = x, y
    x2, y2 = x + a, y1
    x3, y3 = x + a / 2, y - h

    x1r, y1r = rotate_point(x, y, x1, y1, angle)
    x2r, y2r = rotate_point(x, y, x2, y2, angle)
    x3r, y3r = rotate_point(x, y, x3, y3, angle)
    pygame.draw.polygon(window, "black", ((x1r, y1r), (x2r, y2r), (x3r, y3r)))

    x1, y1 = x, y1 - 2 * h / 3
    x2, y2 = x + a, y1
    x3, y3 = x + a / 2, y1 - h

    x1r, y1r = rotate_point(x, y, x1, y1, angle)
    x2r, y2r = rotate_point(x, y, x2, y2, angle)
    x3r, y3r = rotate_point(x, y, x3, y3, angle)
    pygame.draw.polygon(window, "black", ((x1r, y1r), (x2r, y2r), (x3r, y3r)))

    x1, y1 = x, y1 - 2 * h / 3
    x2, y2 = x + a, y1
    x3, y3 = x + a / 2, y1 - h

    x1r, y1r = rotate_point(x, y, x1, y1, angle)
    x2r, y2r = rotate_point(x, y, x2, y2, angle)
    x3r, y3r = rotate_point(x, y, x3, y3, angle)
    pygame.draw.polygon(window, "black", ((x1r, y1r), (x2r, y2r), (x3r, y3r)))

run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill('white')

    draw_triangle(window, *t, angle)
    angle += speed

    pygame.display.flip()

    clock.tick(60)

pygame.quit()