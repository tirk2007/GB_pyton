print('**************')
arr = [57.8, 46.51, 97, 27.5, 415, 1023.53, 5.07]
mess = ""
for i in arr:
    price = f'Цена: {i:.2f}'.split('.')
    r = price[0]
    kk = price[1]
    mess += r + ' руб ' + kk + ' коп, '
print (mess)

print('**************')

print('Новый ',id(arr))
arr.sort()
mess = ""
for i in arr:
    price = f'Цена: {i:.2f}'.split('.')
    r = price[0]
    kk = price[1]
    mess += r + ' руб ' + kk + ' коп, '
print (mess)
print('Старый ',id(arr))

print('**************')


print('Старый ',id(arr))
arr2 = arr.copy()
arr2.sort(reverse=True)
mess = ""
for i in arr2:
    price = f'Цена: {i:.2f}'.split('.')
    r = price[0]
    kk = price[1]
    mess += r + ' руб ' + kk + ' коп, '
print (mess)
print('Новый ',id(arr2))

print(arr2[0:5])
