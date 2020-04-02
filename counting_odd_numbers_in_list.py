numbers = [1, 2, 3, 4, 5, 6, 7]

counter = 0
for number in numbers:
    if number % 2 == 1:
        counter += 1
        continue
print(counter)
