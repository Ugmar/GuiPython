# Марчуков Антон ИУ7-25Б Лабораторная 5

import time
import pygame
from math import sin, cos, radians

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Марчуков Антон ИУ7-25Б л/р 5")

# Цвета
COLOR_BACKGROUND = (255, 255, 255)
COLOR_WHEEL = (0, 0, 0)
COLOR_AXIS = (255, 0, 0)
COLOR_POST = 'black'
COLOR_TRAFIC = "#474422"

# Светофор
trafic_height = 100
trafic_width = 40
trafic_x = 683
trafic_y = 351 - trafic_height
trafic_y_centr = trafic_y + trafic_height // 2

trafic_radius = 10

# текущий свет светофора
current_color = 0

# Столб для светофора
post_height = 50
post_width = 7
post_x, post_y = 700, 351

# Автомобиль
car_width = 200
car_height = 60
car_x = 50
car_y = HEIGHT - car_height - 50
car_speed = 3

# Колеса
wheel_radius = 20
# расстояние между центрами колес
wheel_distance = car_width * 0.3
# Угол поворота колес
wheel_angle = 0
# Скорость вращения колес
wheel_rotation_speed = 0.1

# Картинка машины
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (car_width, car_height))

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Матрица поворота
def rotate_point(x_center, y_center, angle, x, y):
    rotated_x = (x - x_center) * cos(angle) - (y - y_center) * sin(angle) + x_center
    rotated_y = (x - x_center) * sin(angle) + (y - y_center) * cos(angle) + y_center
    return rotated_x, rotated_y


# Функции для рисования вращающегося колеса
def draw_wheel(window, color, x, y, radius, angle):
    pygame.draw.circle(window, color, (int(x), int(y)), radius)

    # Рисуем спицы
    for i in range(4):
        # Распределяем спицы равномерно и добавляем угол поворота
        angle_rad = radians(i * 90) + angle

        line_end_x, line_end_y = rotate_point(x, y, angle_rad, x, (y - radius))
        pygame.draw.line(window, COLOR_AXIS, (int(x), int(y)), (int(line_end_x), int(line_end_y)), 2)


def move_car(car_x, car_y):
    car_x += car_speed
    if car_x > WIDTH:
        # Перемещаем автомобиль в начало экрана
        car_x = -car_width

    return car_x, car_y


def rotate_wheel(wheel_angle):
    # Вращение колес
    wheel_angle += wheel_rotation_speed

    # Вычисляем координаты центров колес
    wheel1_x = car_x + wheel_distance / 2
    wheel1_y = car_y + car_height - 10
    wheel2_x = car_x + car_width - wheel_distance / 2 - 12
    wheel2_y = car_y + car_height - 6

    return wheel1_x, wheel1_y, wheel2_x, wheel2_y, wheel_angle

def draw_traficlight(window, color):
    pygame.draw.rect(window, COLOR_POST, (post_x, post_y, post_width, post_height))

    pygame.draw.rect(window, COLOR_TRAFIC, (trafic_x, trafic_y, trafic_width, trafic_height))

    red, yellow, green = "black", "black", "black"

    # Обновляем свет светофора
    if color == 0:
        red = 'red'
    elif color == 1:
        yellow = 'yellow'
    else:
        green = 'green'

    pygame.draw.circle(window, red, (trafic_x + trafic_width // 2, trafic_y_centr - 2 * trafic_radius - 10),
                       trafic_radius)
    pygame.draw.circle(window, yellow, (trafic_x + trafic_width // 2, trafic_y_centr),
                       trafic_radius)
    pygame.draw.circle(window, green, (trafic_x + trafic_width // 2, trafic_y_centr + 2 * trafic_radius + 10),
                       trafic_radius)

# Основной цикл
run = True
clock = pygame.time.Clock()

# Время начала
last_time = time.time()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Движение автомобиля вправо
    car_x, car_y = move_car(car_x, car_y)

    # Поворот колес
    wheel1_x, wheel1_y, wheel2_x, wheel2_y, wheel_angle = rotate_wheel(wheel_angle)

    # Очищаем экран
    window.fill(COLOR_BACKGROUND)

    # Отображаем фон
    window.blit(background, (0, 0))

    # Отображаем автомобиль
    window.blit(car, (int(car_x), int(car_y)))

    # Рисуем колеса
    draw_wheel(window, COLOR_WHEEL, wheel1_x, wheel1_y, wheel_radius, wheel_angle)
    draw_wheel(window, COLOR_WHEEL, wheel2_x, wheel2_y, wheel_radius, wheel_angle)

    if time.time() - last_time > 1.1:
        current_color = (current_color + 1) % 3
        last_time = time.time()

    draw_traficlight(window, current_color)

    # Обновляем экран
    pygame.display.flip()

    # Управляем частотой кадров
    clock.tick(60)

# Завершение Pygame
pygame.quit()
