numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in numbers:
    print(number)
print()

for number in numbers:
    print(number,"\t", number ** 2)
print()

total = 0
for number in numbers:
    total += number
    
print(total)
print()

product = 1
for number in numbers:
    product *= number
    
print(product)
