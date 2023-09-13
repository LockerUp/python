# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# sum(2, 2)
# 4

def sum(a,b):
    if b <= -a:
        return 0
    b -= 1
    return 1 + sum(a,b)

print(sum(22,10))