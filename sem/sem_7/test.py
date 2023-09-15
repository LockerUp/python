# Лямбды из лекции




# def calk1(a,b):
#     return a + b

# def math(op, x, y):
#     print(op(x,y))

# math(lambda a,b: a+b, 5, 45)



# list_1 = [1,2,3,5,8,15,23,38]
# list_2 = list()

# for i in list_1:
#     if i % 2 == 0:
#         list_2.append((i, i**2))

# print(list_2)


# list_1 = [1,2,3,5,8,15,23,38]

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# res = select(int, list_1)
# print(res)
# res = where(lambda x: x%2==0, res)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# теория из семинара

lst = list('1234567890')
print(lst)

# for i in range(len(lst)):
#     lst[i] = int(lst[i])

lst = list(map(int,lst))

print(lst) 