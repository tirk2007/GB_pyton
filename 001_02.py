# Задание 2
from typing import Any

arr = []
sum7 = 0
for i in range(1,1001,2):
    v = (i**3)
    arr.append(v)
    sumstr = 0
    #print("Число в кубе: ",v)
    for f in str(v):
        sumstr = sumstr + int(f)
        #print("Сумма строки: ", sumstr)

    if sumstr/7 == sumstr // 7:
        #print("Делится нацело на 7 ", v)
        sum7 = sum7 + v


print("Сумма чисел, которые делятся на 7: ", sum7)
# print(len(arr))

sum7 = 0
for v in arr:
    v = v + 17
    sumstr = 0
    # print("Число в кубе: ",v)
    for f in str(v):
        sumstr = sumstr + int(f)
        # print("Сумма строки: ", sumstr)

    if sumstr / 7 == sumstr // 7:
        # print("Делится нацело на 7 ", v)
        sum7 = sum7 + v

print("Новая сумма: ", sum7)
