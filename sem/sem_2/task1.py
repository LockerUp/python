n = int(input("Введите число N: "))

factorial = 1
while (n >= 1):
    factorial = factorial * n
    n = n-1
print(factorial)