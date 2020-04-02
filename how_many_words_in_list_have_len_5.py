words = ["Ali", "Alege", "abcde", "kledf", "abd"]

counter = 0
for word in words:
    if len(word) == 5:
        counter += 1
        continue
print(counter)
