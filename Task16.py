# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# Пример:5
#        1 2 3 4 5
#        3
#        -> 1

input()
lst = map(int, (input().split()))
n = int(input())
inc = 0
for i in lst:
    if i == n:
        inc += 1
print(inc)

# n = int(input())
# a = map(int, input().split())
# x = int(input())
# print(sum(map(lambda z: int(z == x), a)))