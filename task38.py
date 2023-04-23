
"""""
#todo Задача 1. Транспонирование матрицы, transpose(matrix)
Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10


#todo Задача 2. Транспонирование матрицы, transpose(matrix)
Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
Пример:
>>> transpose([[1, 2, 3], [4, 5, 6]])

[[1, 4], [2, 5], [3, 6]]


||1 2 3||      ||1 4||
||4 5 6||  =>  ||2 5||
               ||3 6||



#todo Задача 3. Найти сумму элементов матрицы
Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
Задачу решить с помощью генераторов.

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> msum(matrix)
"""
# Задача 1
a =[i for i in range(1, 11) for _ in range(i)]
print(*a, sep =', ')

#Задача 2
matrix = [1, 2, 3], [4, 5, 6]

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose(matrix))

#Задача 3

matrix = [[1, 2, 3], [4, 5, 6]]

def msum(matrix):
    return sum([sum(row) for row in matrix])
print(msum(matrix))

 

