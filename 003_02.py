def num_translate_adv(p1):
    p2 = p1.lower()
    temp = dic.get(p2)
    if not p1[:1].islower():
        return temp.capitalize()
    else:
        return temp


dic = {'one': 'один', 'two': 'два', 'eight':'восемь'}
print(num_translate_adv("one"))
print(num_translate_adv("Eight"))
print(num_translate_adv("nine"))