def thesaurus(*args):
    list_names = {}
    for i in sorted(args):
        letter = i[0]
        if letter in list_names:
            list_names[letter] += [i]
        else:
            list_names[letter] = [i]
    return list_names


print(thesaurus("Иван", "Мария", "Петр", "Марина", "Илья", "Павел"))
