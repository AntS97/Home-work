#todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …

def palindrome_generator():
    n = 1
    while True:
        s = str(n)
        if s == s[::-1]:
            yield n
        n += 1

palindrome_iter = palindrome_generator()
n = int(input('Введите длину числовых палиндромов: '))
print(' '.join(str(next(palindrome_iter)) for i in range(n)))
