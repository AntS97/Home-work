#todo:
# Реализовать декоратор который подсчитывает время выполнения функции.
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        time.sleep(1)
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения {func.__name__}: {end_time - start_time}')
        return result
    return wrapper

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7

@timeit

def my_func(lst, x):
    result = []
    for num in lst:
        if num > x:
            result.append(num ** 2)
    return result
answ = my_func(lst, x)
print (answ)