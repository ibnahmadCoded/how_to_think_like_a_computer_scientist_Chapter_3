numbers = [1, 3, 5, 7, 9, 2, 5]

sum = 0
for number in numbers:
    if number % 2 == 0:
        break
    else:
        sum += number
print(sum)
