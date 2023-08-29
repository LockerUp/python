# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random

numberOfCoins = int(input("Введите количество монет: "))
side1 = 0
side2 = 0

for i in range(numberOfCoins):
    side = random.randint(0,1)
    print(side, end=" ")
    if side == 0:
        side1 += 1
    elif side == 1:
        side2 += 1
if side1 > side2:
    print(f'\n{side2}')
else:
    print(f'\n{side1}')