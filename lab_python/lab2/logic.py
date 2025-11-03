# Код ошибки 1 - Лимит итераций
# Код ошибки 2 - Деление на 0
# Код ошибки 3 - Выход из ОДЗ
# Код ошибки 0 - корень найден успешно
# Код ошибки 4 - на локальном отрезке нет корня

from math import *
import numpy as np
import matplotlib.pyplot as plt

# Коды возврата
NORMAL_CODE = 0
DEVIZING_ZERO = 2
LIMIT_IT = 1
VALUE_ERROR = 3
NOT_X = 4


# y(x)=
def func(x, y):
    return eval(y)

# функция в нормальном виде
def normal_float(y):
    return float(f'{y:.0e}')


# уточнение x на локальном отрезке, делением пополам
def search_x(a, b, eps, mnmax, y):
    try:
        # Проверка начало и конца отрезка
        if abs(func(a, y)) < eps:
            return a, 0, NORMAL_CODE
        elif abs(func(b, y)) < eps:
            return b, 0, NORMAL_CODE
        # Основное вычисление
        elif func(a, y) * func(b, y) < 0:
            count = 0
            while (b - a) > eps and count < mnmax + 1:
                c = (a + b) / 2
                if func(b, y) * func(c, y) < 0:
                    a = c
                else:
                    b = c
                count += 1
            # Проверка на лимит операций
            if count > mnmax:
                return None, None, LIMIT_IT
            x = (a + b) / 2
            # Если получилось "случайное значение" != ~0
            if abs(func(x, y)) > 2:
                return None, None, NOT_X
            return (a + b) / 2, count, NORMAL_CODE
        else:
            return None, None, NOT_X
    except ZeroDivisionError:
        return None, None, DEVIZING_ZERO
    except ValueError:
        return None, None, VALUE_ERROR


# вычисление корней на всем промежутке
def main_calc(a, b, h, eps, mnmax, y):
    result = []
    xi_last = a
    count = 1
    # Проверка каждого отрезка на наличии корня
    for i in range(1, int((b - a) // h) + 2):
        xi = min(a + h * i, b)
        x, count_it, code = search_x(xi_last, xi, eps, mnmax, y)
        # Проверка на наличие корня
        if code != NOT_X:
            if code == NORMAL_CODE:
                result.append((count, (xi_last, xi), x, normal_float(func(x, y)), count_it, code))
            else:
                # Ошибка при вычислении корня
                result.append((count, (xi_last, xi), None, None, None, code))
            count += 1
            xi += eps
        xi_last = xi
    return result

# Основная функция
def main_logic(a, b, h, eps, nmax, y_0, y_1, y_2):
    # Экстремумы функции
    list_extremums = list(
        map(lambda j: j[2], filter(lambda i: i[5] == NORMAL_CODE, main_calc(a, b, h, eps, nmax, y_1))))
    # Точки перегиба в функции
    list_infection = list(
        map(lambda j: j[2], filter(lambda i: i[5] == NORMAL_CODE, main_calc(a, b, h, eps, nmax, y_2))))
    result = main_calc(a, b, h, eps, nmax, y_0)
    # Нули функции
    list_base = list(
        map(lambda j: (j[2], j[3]), filter(lambda i: i[5] == NORMAL_CODE, result)))

    # Заполнение массивов нулями функции, экстремума и точками перегиба
    x_base = []
    y_base = []
    for x, y in list_base:
        x_base.append(x)
        y_base.append(y)

    x_extr = []
    y_extr = []
    for x in list_extremums:
        x_extr.append(x)
        y_extr.append(func(x, y_0))

    x_infection = []
    y_infection = []
    for x in list_infection:
        x_infection.append(x)
        y_infection.append(func(x, y_0))

    # Создание X на всем промежутке
    x = np.linspace(a, b, 1000)
    y = []
    # Если при xi произошла, то он не выводится на графике
    for i, xi in enumerate(x):
        try:
            y.append(func(xi, y_0))
        except (ValueError, ZeroDivisionError):
            x[i] = a - 1
    x = list(filter(lambda k: k != (a - 1), x))

    # Создание графика
    plt.figure(figsize=(10, 5), label='График')
    plt.plot(x, y, label='f(x)', color='blue')
    plt.scatter(x_extr, y_extr, color='#FF0000', label='Экстремумы')
    plt.scatter(x_infection, y_infection, color='#00FF00', label='Точки перегиба')
    plt.scatter(x_base, y_base, color='black', marker='*', label='Корни уравнения')

    plt.title("График функции")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show(block=False)
    return result