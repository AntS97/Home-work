#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

import calendar

for month in range(1, 13):
    cal = calendar.monthcalendar(2023, month)
    thursdays = [week[calendar.THURSDAY] for week in cal if week[calendar.THURSDAY] != 0]
    if len(thursdays) >= 3:
        print(f"Вход бесплатный {calendar.month_name[month]}: {thursdays[2]}")
