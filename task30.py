# todo:
#     Дан список чисел lst и число x. Найти и напечатать самый близкий к числу x элемент списка lst.
#     Например: lst = [1, 10, 21, 30].
#     Наиболее близкое к числу 16 является 21:
#     16 – 1= 15, 16 – 10 = 6, 21 – 16 = 5, 30 – 16 = 14.
#     Какую лямбда-функцию лучше всего здесь использовать в операторе min()?
#     print(min(lst, key = lambda x: ????????? ))

x = int(input())
lst = [1, 10, 21, 30]
out = []
close_number = min(lst, key=lambda i: abs(x - i))
print(close_number)
print('Наиболее близкое к числу ',
      x, 'является число ', close_number)

for close_number in lst:
    if close_number < x:
        out.append(f' {x} - {close_number} = {abs(x - close_number)}')
    else:
        out.append(f' {close_number} - {x} = {abs(x - close_number )}')

print(*out, sep=", ")
