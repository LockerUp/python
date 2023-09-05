# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

sizeFirstList = int(input("Введите размер первого набора чисел: "))
sizeSecondList = int(input("Введите размер второго набора чисел: "))

firstList = []
secondList = []

# заполняем первый список рандомными, целыми числами
for i in range(sizeFirstList):
    firstList.append(random.randint(1,100))

# заполняем второй список рандомными, целыми числами
for i in range(sizeSecondList):
   secondList.append(random.randint(1,100))

# показываем результат заполнения
print(firstList)
print(secondList)

# формируем список из уникальных элементов множеств первого и второго набора чисел
resultList = list(set(firstList).intersection(set(secondList)))

# сортируем в порядке возрастания полученный список
resultList.sort()
print(resultList)