#todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами. Накапливает сон обеих функций отдельно и печатает две суммы.

import time

def sleep_2_seconds():
    time.sleep(2)
    return 2

def sleep_3_seconds():
    time.sleep(3)
    return 3

sleep_time_2 = 0
sleep_time_3 = 0

for i in range(11):
    if i % 2 == 0:
        sleep_time_2 += sleep_2_seconds()
    else:
        sleep_time_3 += sleep_3_seconds()

print(f"Сон функции sleep_2: {sleep_time_2} секунд")
print(f"Сон функции sleep_3: {sleep_time_3} секунд")
