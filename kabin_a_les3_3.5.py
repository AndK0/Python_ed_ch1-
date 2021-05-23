from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def some_jokes(i, repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes_arr = []
    min_arr = min(no, adv, adj)

    while i and len(min_arr):
        num = randrange(len(min_arr))
        if repeat:
            jokes_arr.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            jokes_arr.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        i -= 1
    return jokes_arr


print(some_jokes(10))
