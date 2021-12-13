from random import randrange

def get_jokes(n):
    arr = []
    while n > 0:
        p1 = nouns[randrange(len(nouns))]
        p2 = adverbs[randrange(len(adverbs))]
        p3 = adjectives[randrange(len(adjectives))]
        arr.append(p1 +' '+ p2 + ' ' + p3)
        #print(p1,p2,p3)
        n -= 1
    return arr


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(2))

