a = float(input("What is the first side? "))
b = float(input("What is the second side? "))
c = float(input("What is the third side? "))

#find the hypotenause
if a > b and a > c:
    hypotenause = a
    adjascent = b
    opposite = c
elif b > a and b > c:
    hypotenause = b
    adjascent = a
    opposite = c
else:
    hypotenause = c
    adjascent = b
    opposite = a

#calculate with pythagoras' theorem
two_sides = adjascent ** 2 + opposite ** 2
third_side = hypotenause ** 2

threshold = 1e-7

if abs(two_sides - third_side) < threshold:        #approximate equality
    print("Triangle is right-angled")
else:
    print("Triangle is not right-angled")
