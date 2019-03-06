# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


# Формируем матрицу для сложения шеснадцатиричных чисел
def gen_sum_mtx():
    mk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    md = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
          '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e']
    cal_mtx = dict()

    for x in range(len(mk)):
        cal_mtx[mk[x]] = dict()
        for y in range(len(mk)):
            cal_mtx[mk[x]][mk[y]] = md[x+y]
    return cal_mtx


def sum_hex(p_a, p_b):
    m = gen_sum_mtx()
    res = deque()
    num_over = '0'

    a = list(p_a.lower())
    b = list(p_b.lower())

    while len(a) > 0 or len(b) > 0:
        if len(a) > 0:
            num_a = a.pop()
        else:
            num_a = '0'
        if len(b) > 0:
            num_b = b.pop()
        else:
            num_b = '0'
        num_r = m[num_a][num_b]
        num = m[num_over][num_r[-1]]

        if len(num_r) > 1 or len(num) > 1:
            num_over = '1'
        else:
            num_over = '0'
        res.appendleft(num[-1])
    else:
        if num_over == '1':
            res.appendleft(num_over)

    return ''.join(res).lstrip('0')


# Алгоритм крайне неэффективный (большие цифры лучше не умножать), но на реализацию через матрицу
# или др. не хватило времени
def mult_hex(p_a, p_b):
    a = p_a.lower()
    b = p_b.lower()

    inc = '1'
    nul = '0' * len(b)
    one = '0'*(len(b)-1) + '1'
    idx = one
    res = a
    while True:
        if b == nul:
            return nul
        elif b == one:
            return a
        elif idx == b:
            return res

        res = sum_hex(res, a)
        idx = sum_hex(idx, inc)


an = input("Введите первое число:")
bn = input("Введите второе число:")

print(f"a + b = {sum_hex(an, bn).upper()}")
print(f"a * b = {mult_hex(an, bn).upper()}")
