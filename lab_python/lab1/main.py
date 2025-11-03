# Функция считает сумму вещественных чисел
def ternary_summation(a, b):
    # Разделяем входные числа на целую часть и дробную
    dot = '.' in a or '.' in b
    whole_a, fractional_a = a.split('.') if '.' in a else (a, '')
    whole_b, fractional_b = b.split('.') if '.' in b else (b, '')
    # длина для выравнивания дробной части
    fractional_len = max(len(fractional_a), len(fractional_b))
    # меняем числа местами, так чтобы число "а" было длиннее
    if len(fractional_a) < len(fractional_b):
        fractional_a, fractional_b = fractional_b, fractional_a
    # выравниваем остатки
    fractional_b = fractional_b.ljust(len(fractional_a), '0')
    # считаем сумму остатков
    fractional_ab = base_summation(fractional_a, fractional_b)
    # разделяем полученную сумму на ответ и перенос в целую часть
    fractional_in_whole, fractional_res = fractional_ab[:len(fractional_ab) - fractional_len], fractional_ab[-fractional_len:]
    if dot:
        fractional_res = '.' + fractional_res
    # считаем сумму целой части
    whole_ab = base_summation(whole_a, whole_b)
    # складываем полученную сумму с переносом из дробной части
    whole_res = base_summation(fractional_in_whole, whole_ab)
    # добавляем незначащий ноль в дробную часть, при ее отсутствии
    if dot and fractional_res == '.':
        fractional_res = '.0'
    # формируем ответ
    if whole_res == '':
        whole_res = '0'
    res = whole_res + fractional_res
    return res

# функция суммирования двух целых 3-ых симметричных чисел
def base_summation(a, b):
    if len(a) < len(b):
        a, b = b, a
    # создаем "ответ" на 1 разряд больше максимальной длины числа
    res = ['0'] * (len(a) + 1)
    # выравниваем "короткое" число
    b = b.rjust(len(a), '0')
    # Складываем по символьно числа, исходя из правил сложения в заданной СС
    for index in range(len(a) - 1, -1, -1):
        el1 = a[index]
        el2 = b[index]
        # прошлый переход в разряд
        current = res[index + 1]
        # переход в новый разряд и сам разряд
        ost = out = '0'
        if (el1 == '0' and el2 == '+') or (el1 == '+' and el2 == '0'):
            if current == '0':
                out = '+'
            elif current == '+':
                out = '-'
                ost = '+'
        elif (el1 == '0' and el2 == '-') or (el1 == '-' and el2 == '0'):
            if current == '0':
                out = '-'
            elif current == '-':
                out = '+'
                ost = '-'
        elif el1 == '+' and el2 == '+':
            if current == '0':
                out = '-'
                ost = '+'
            elif current == '-':
                out = '+'
            else:
                ost = '+'
        elif el1 == '-' and el2 == '-':
            if current == '0':
                out = '+'
                ost = '-'
            elif current == '+':
                out = '-'
            else:
                ost = '-'
        elif (el1 == '+' and el2 == '-') or (el1 == '-' and el2 == '+'):
            out = current
        # формируем число
        res[index + 1] = out
        res[index] = ost
    # избавляемся от незначащих нулей и формируем строку
    return ''.join(res).lstrip('0')

# вычитание 2 чисел
def ternary_subtraction(a, b):
    # инвертируем число b и складываем
    b = b.replace('+', '1').replace('-', '+').replace('1', '-')
    return ternary_summation(a, b)
