# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_item = int(input("Введите первый элемент арифметической прогрессии: "))
step = int(input("Введите разность арифметической прогрессии: "))
size = int(input("Укажите количество элементов прогрессии: "))

lst = []

for i in range(size):
    lst.append(first_item + i * step)

print(lst)