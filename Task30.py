# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии:
# n
#  = a1
#  + (n-1) * d.
 
# Каждое число вводится с новой строки.
# Пример:Ввод: 7 2 5
#        Вывод: 7 9 11 13 15


a1, d, n = int(input()), int(input()), int(input())
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)

# Вот еще вариант.
x = int(input('input a[0]'))
d = int(input('input d'))
n = int(input('input n'))
print(*range(x,x + d * n, d))