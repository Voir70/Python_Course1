# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# Пример:5
#        1 2 3 4 5
#        6
#        -> 5

N = int(input())
lst = map(int, (input().split()))
x = int(input())
print(min(lst, key=lambda a:abs(a-x)))

# l = input()
# numbers = list(map(int, input().strip().split()))
# x = int(input().strip())

# res = numbers[0]
# for i in numbers:
#     if abs(i - x) < abs(res - x):
#         res = i

# print(res)