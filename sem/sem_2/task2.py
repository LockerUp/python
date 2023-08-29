# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

a = int(input("Введите число A: "))

fib_sum = 0
fib1 = 0
fib2 = 1
i = 0

while (fib_sum <= a):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i+= 1
    print(fib_sum)
if (fib1 == a):
    print(i)
else:
    print(-1)  