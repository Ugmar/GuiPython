from math import sin, cos

def f(x):
    return sin(x)

def df(x):
    return cos(x)

def calc(a, b, eps):
    x = (a + b) / 2
    for i in range(1000):
        fx = f(x)
        dfx = df(x)
        x_next = x - fx / dfx
        if abs(x - x_next) < eps:
            return x_next
        x = x_next
    return None
