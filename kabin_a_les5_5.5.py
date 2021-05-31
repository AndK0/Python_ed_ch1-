arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(arr)

new_arr = {i: 0 for i in arr}
print(new_arr)

for i in arr:
    if i in new_arr:
        new_arr[i] += 1

print(new_arr)
print([i for i in new_arr if new_arr[i] == 1])

# print([i for i in arr if arr.count(i) == 1])
