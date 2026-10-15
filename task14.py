#Кондратьева Настя ПИЗИ23о2
#Задана целочисленная квадратная матрица размером n*n. Написать программу,
#преобразующую исходную матрицу по правилу: нечетные столбцы разделить на
#значение диагональных элементов матрицы, а четные оставить без изменения
n = int(input("n = "))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if j % 2 == 0:       
            a[i][j] = a[i][j] / a[i][i]

for row in a:
    for x in row:
        print(round(x, 2), end=' ')
    print()

