arr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

bigger_value = [arr[number] for number in range(1, len(arr)) if arr[number] > arr[number-1]]

print(bigger_value)
