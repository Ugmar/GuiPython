from math import sqrt

def search_area(dot1, dot2, dot3):
    a = sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1])**2)
    b = sqrt((dot1[0] - dot3[0]) ** 2 + (dot1[1] - dot3[1])**2)
    c = sqrt((dot3[0] - dot2[0]) ** 2 + (dot3[1] - dot2[1])**2)
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def search_triangles(list_triangle):
    min_area = abs(search_area(*list_triangle[0]) - search_area(*list_triangle[1]))
    min_triangle = (0, 1)

    for index_triangle_1 in range(len(list_triangle)):
        area_1 = search_area(*list_triangle[index_triangle_1])
        for index_triangle_2 in range(index_triangle_1 + 1, len(list_triangle)):
            area_2 = search_area(*list_triangle[index_triangle_2])

            if abs(area_1 - area_2) < min_area:
                min_area = abs(area_1 - area_2)
                min_triangle = (index_triangle_1, index_triangle_2)

    min_triangle = list_triangle[min_triangle[0]], list_triangle[min_triangle[1]]
    return min_triangle
