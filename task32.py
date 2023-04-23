#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
#Ввод: GGCTAA
#Вывод: CCGATT
# В РНК нет T, вместо него там U

#DNA = ['G','C','T','A']
#RNA = ['C','G','A','T']


def code(string, n):
    DNA = ['C','G','A','T']
    RNA = ['A','G','C','T']
    result = ''
    for char in string:
        if char in DNA:
            result += RNA[(DNA.index(char) + int(n)) % 4]
        elif char in RNA:
           result += char
        else:
            print('Ошибка введенных данных')
            break   
    return result
    
x = input()
shift = 1
str_RNA = code(x, shift)
print(str_RNA)

