number = [200, 2, 12, 44, 1, 1, 4, 10, 8, 1, 78, 123, 55]

result = [number[i] for i in range(1, len(number)) if number[i] > number[i - 1]]

print(result)