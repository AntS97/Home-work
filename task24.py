#todo: Напишите программу, которая:
# Получает на вход две строки, в которых перечисляются книги, прочитанные двумя учениками.
# Выводит количество книг, которые прочитали оба ученика.
# Пример ввода:
# Война и мир, Над пропастью во ржи, Мастер и Маргарита, Идиот
# Евгений Онегин, Идиот, Мастер и Маргарита, Война и мир
first = 'Война и мир, Над пропастью во ржи, Мастер и Маргарита, Идиот' #можно заменить на input()
second = 'Евгений Онегин, Идиот, Мастер и Маргарита, Война и мир'
first_set = set(first.split(', '))
second_set = set(second.split(', '))
intersection = first_set.intersection(second_set)
print(intersection)