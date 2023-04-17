# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".
a = int(input())
first_digit = a // 1000
second_digit = a // 100 % 10
third_digit = a // 10 % 10
four_digit = a % 10
if first_digit == four_digit and third_digit == second_digit:
    print('Число читается одинаково')
else:
    print('Ошибка')
    