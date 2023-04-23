# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.
import calendar
year = int(input('Введите год: '))
month = int(input('Введите месяц (числом): '))

def get_dates_in_month(year, month):
    num_days = calendar.monthrange(year, month)[1]
    return [f"{day:02d}.{month:02d}.{year}" for day in range(1, num_days + 1)]
print(get_dates_in_month(year, month))