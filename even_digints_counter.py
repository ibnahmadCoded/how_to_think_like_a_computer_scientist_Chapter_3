n = int(input("What is the number? "))

count = 0

if n < 0:
    n *= -1 #convert n to +ve integer

while n > 0:
    digit = n % 10
    if digit % 2 == 0: #digit is even?
        count += 1
    n = n // 10
print(count)
    
