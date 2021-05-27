my_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': ' четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
           'nine': 'девять', 'ten': 'десять'}


def num_translate(num):
    return my_dict.get(num)


print(num_translate(input('write any number from 1 to 10 (word): ', )))

#   for k, v in my_dict.values():
#       if k == num:
#           print(v)
