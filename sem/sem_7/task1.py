import random
import math

list_1 = list(tuple(random.randint(1,10) for i in range(10)))
print(list_1)
list_2 = list(tuple(random.randint(1,10) for i in range(10)))
print(list_2)

list_3 = set(filter(lambda x: x[0] != x[1], zip(list_1, list_2)))
print(list_3)

print(max(list_3, key=lambda x: x[0] * x[1]))