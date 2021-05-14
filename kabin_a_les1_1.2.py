list_cubes = []
sums = 0

for i in range(1, 1001, 2):
    list_cubes.append(i**3)
for index, value in enumerate(list_cubes):
    counts = 0
    while value > 0:
        counts += value % 10
        value //= 10
    if counts % 7 == 0:
        sums += list_cubes[index]
print(sums)