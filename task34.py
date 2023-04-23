# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(n):
    if n == 0:
        return 0
    else:
        return n + sumn(n-1)

n = int(input())
result = sumn(n)
print(f"Сумма чисел от 0 до {n} равна {result}.")


