#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

def code(string, n):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbol = [' ', ',', '.', '!', '?', '"', "'"]
    result = ''
    for char in string:
        if char in eng_lower_alphabet:
            result += eng_lower_alphabet[(eng_lower_alphabet.index(char) + n) % 26]
        elif char in eng_upper_alphabet:
            result += eng_upper_alphabet[(eng_upper_alphabet.index(char) + n) % 26]
        elif char in symbol:
            result += char
    return result
    
string_1 = input()
shift = 1
code_string = code(string_1, shift)
print(code_string)