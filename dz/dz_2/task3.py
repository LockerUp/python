# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N: "))
two = 1
for i in range(N):
    tmp = two*2
    two = tmp
    if tmp < N:
        print(tmp)