"""виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;"""
import numpy as np

ro = 0
no = []
to = []
while True:
    n, p = int(input('Введіть кількість рядків1:  ')), int(
        input('Введіть кількість стовбців1: '))  # вводим розмірність матриці 1
    v, x = int(input('Введіть кількість рядків2:  ')), int(
        input('Введіть кількість стовбців2: '))  # вводим розмірність матриці 2
    while n != 3 and p != 3:
        n, p = int(input('Введіть кількість рядків1:  ')), int(input('Введіть кількість стовбців1: '))
        v, x = int(input('Введіть кількість рядків2:  ')), int(input('Введіть кількість стовбців2: '))
    a = np.zeros((n, p), dtype=int)
    m = np.zeros((v, x), dtype=int)
    for i in range(n):
        for j in range(p):
            a[i, j] = int(input(f'A[{i + 1},{j + 1}]='))  # заповнюєм 1 матрицю значеннями
    print('Наша матриця 1')
    print(a)
    for o in range(v):
        for z in range(x):
            m[o, z] = int(input(f'M[{o + 1},{z + 1}]='))  # заповнюєм 2 матрицю значеннями
    print('Наша матриця 2')
    print(m)
    for i in range(n):
        for z in range(x):
            for j in range(p):
                ro = ro + a[i][j] * m[j][z]  # перемножаємо матриці 1 и 2
            no.append(ro)  # додаємо значення в список
            ro = 0
        to.append(no)  # після обчислень записуємо у список
        no = []
    print(f' матриця 3{to}')
