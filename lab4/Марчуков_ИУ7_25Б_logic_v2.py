EPS = 1e-9

# Функция проверки точки внутри треугольника
def point_in_triangle(point, triangle):
    # Координаты точек треугольника и проверяемой точки
    x, y = point
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]

    # Вычисление площади треугольника
    s = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    # Вычисление площадей треугольников, состоящих из проверяемой точки и вершин треугольника
    s1 = 0.5 * abs(x * (y2 - y3) + x2 * (y3 - y) + x3 * (y - y2))
    s2 = 0.5 * abs(x1 * (y - y3) + x * (y3 - y1) + x3 * (y1 - y))
    s3 = 0.5 * abs(x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2))

    # Проверка на равенство площадей
    return abs(s - (s1 + s2 + s3)) < EPS


# Поиск искомого треугольника
def search_triangle(points_a, points_b):
    # Перебор всех возможных троек точек
    for point1 in range(len(points_a)):
        for point2 in range(point1 + 1, len(points_a)):
            for point3 in range(point2 + 1, len(points_a)):
                triangle = (points_a[point1], points_a[point2], points_a[point3])

                # Количество точек множества A и B внутри текущего треугольника
                count_a = 0
                count_b = 0

                # Проверяем все точки множества A на принадлежность области треугольника
                for point_a in points_a:
                    if point_a not in triangle and point_in_triangle(point_a, triangle):
                        count_a += 1

                # Проверяем все точки множества B на принадлежность области треугольника
                for point_b in points_b:
                    if point_in_triangle(point_b, triangle):
                        count_b += 1

                # Проверка найденного количества. Это количество должно быть больше 0
                if count_a == count_b and count_a != 0:
                    return triangle

    # Если не нашли подходящий треугольник возвращаем None
    return None
