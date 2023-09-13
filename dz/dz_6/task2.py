# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

size = int(input("Укажите длину списка: "))
min_border = int(input("Минимальное число диапазона: "))
max_border = int(input("Максимальное число диапазона: "))

lst = [random.randint(1,20) for _ in range(size)]
print(lst)

counter = []
for i in range(len(lst)):
    if lst[i] <= max_border and lst[i] >= min_border:
        counter.append(i)
print(counter)