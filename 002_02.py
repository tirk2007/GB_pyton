
def preffics(ch):
    if ch[0] in '+-':
        return ch[0]


arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(arr):
    pref = preffics(arr[i]) # Поймали знак (префикс)
    if arr[i].isdigit() or arr[i][1:].isdigit():
        if pref:
            arr[i] = '"' + pref + arr[i][1:].zfill(2) + '"'
        else:
            arr[i] = arr[i][1:].zfill(2)
    i += 1
print(arr)

print(' '.join(arr))











