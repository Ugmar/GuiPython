# Марчуков Антон ИУ7-25Б рк
# Вариант 1

# 1 номер
# Код d в 2-ой системе = 01100100
# p1(255, 96, 12), p2(25, 17, 127) p3 (60, 60, 139)
# p1:
# 255: 11111111 -> 11111110
# 96: 01100000 -> 01100001
# 12: 00001100 -> 00001101
# p1(254, 97, 13)
# p2:
# 25: 00011001 -> 00011000
# 17: 00010001 -> 00010000
# 127: 01111111 -> 01111111
# p2(24, 26, 127)
# p3:
# 60: 00111100 -> 00111100
# 60: 00111100 -> 00111100
# 139: без изменений
# p3(60, 60, 139)
#
# 2 номер
#x_n+1 = x_n - f(x_n) * (x_n - x_n-1) / (f(x_n) - f(x_n-1))

import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Марчуков Антон ИУ7-25Б рк")


run = True
clock = pygame.time.Clock()
x, y = 400, 400
x_trap, y_trap = WIDTH, y
r = 10

speed = 2
len_less = randint(2 * r, 6 * r)
len_more = 2 * len_less
x_up = x_trap + (len_more - len_less) / 2
h = randint(2 * r, 7 * r)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0,0,0))

    x_trap -= speed
    x_up = x_trap + (len_more - len_less) / 2

    if x_trap <= x:
        y_trap = y_trap + h / len_less * 2  * speed
    pygame.draw.circle(window, 'white', (x, y), r)

    pygame.draw.polygon(window, 'white', ((x_trap, y_trap), (x_up, y_trap - h), (x_up + len_less, y_trap - h), (x_trap + len_more, y_trap)), 1)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
