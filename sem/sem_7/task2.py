# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, 
# если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

import random

list_1 = list(random.randint(1,10) for _ in range(10))
# list_1 = [2,4,6,8]

print(list_1)

characteristik = list(filter(lambda x: x % 2 == 0, list_1))

print(characteristik)

if len(list_1) != len(characteristik):
    print("False")
else:
    print("True")

# def same_by(cha):
#     if cha != True:
#         return True
#     return False

# print(same_by(characteristik))