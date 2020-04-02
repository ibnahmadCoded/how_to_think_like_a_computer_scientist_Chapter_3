n = int(input("What is the number? "))

count = 0

if n < 0:
    n *= -1 #convert n to +ve integer

while n != 0:
    count += 1
    n = n // 10
print(count)
    
    
