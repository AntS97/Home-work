# todo: Ввод: 2 слова, разделенных пробелами. Для ввода используем функцию s = input().split()
#  Определить, являются ли эти слова анаграммами (словами с одинаковым набором букв). Если да, то True. Если нет, то False.
#  (Примеры: АКВАРЕЛИСТ-КАВАЛЕРИСТ, АНТИМОНИЯ-АНТИНОМИЯ, АНАКОНДА-КАНОНАДА, ВЕРНОСТЬ-РЕВНОСТЬ, ВЛАДЕНИЕ-ДАВЛЕНИЕ, ЛЕПЕСТОК-ТЕЛЕСКОП)
a = input().split()
first_list = a[:1]
second_list = a[1:]
equal = True
for i in first_list:
    sort_list1 = ''.join(sorted(i))
for x in second_list:
    sort_list2 = ''.join(sorted(x))
if len(sort_list1) != len(sort_list2):
    equal = False
else:
    for z in range(len(sort_list1)):
        if sort_list1[z] != sort_list2[z]:
            equal = False
if equal:
    print('Слова являются анаграммами')
else:
    print('Не является анаграммой')