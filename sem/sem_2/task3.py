# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

import random

watermelon = int(input('Количество арбузов: '))
minimum = 30000
maximum = 1000

for i in range(watermelon):
    weight = random.randint(1000, 30000)
    print(weight, end = " ")
    if minimum > weight:
        minimum = weight
    elif maximum < weight:
        maximum = weight
print(f"\n{maximum} , {minimum}")