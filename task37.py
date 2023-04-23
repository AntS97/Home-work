#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.


from datetime import datetime

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1 
    wrapper.counter = 0
    return wrapper

tuple_list = [('Иванов', 100), ('Петров', 200), ('Сидоров', 200), ('Воробьев', 100), ('Лунин', 200)]

@count_calls   
def render():
    sorted_list = sorted(tuple_list, key=lambda x: (-x[1], x[0]))
    for item in sorted_list:
        return (item)  
    
for i in range(6): 
    ans = render()

@count_calls   
def show():
    sorted_list = sorted(tuple_list, key=lambda x: (-x[1], x[0]))
    for item in sorted_list:
        return (item)  

for i in range(4): 
    ans = show()

with open('debug.log', 'a') as f:
    f.write(f"render, {render.counter}, {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
    f.write(f"show, {show.counter}, {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")


