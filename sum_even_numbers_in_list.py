numbers = [1, 2, 3, 4, 5, 6, 7]

sum = 0
for number in numbers:
    if number % 2 == 0:
        sum += number
        continue
print(sum)
