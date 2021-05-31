from itertools import islise, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = (i for i in zip_longest(tutors, klasses))

print(type(result))
print(*islice(result, 10))
print(list(islice(result, 3)))
