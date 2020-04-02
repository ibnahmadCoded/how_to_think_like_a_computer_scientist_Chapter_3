import random
joe = random.Random()

tot = 0
for _ in range(10000000):
    num = joe.randrange(1000)
    tot += num
    
print(tot)
    
    
