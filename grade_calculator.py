#mark = float(input("What is your mark? "))

numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]

for mark in numbers:
    if mark >= 75: 
        print("Your Grade is First")
    elif mark >= 70 and mark < 75:
        print("Your Grade is Upper Second")
    elif mark >= 60 and mark < 70:
        print("Your Grade is Second")
    elif mark >= 50 and mark < 60:
        print("Your Grade is Third")
    elif mark >= 45 and mark < 50:
        print("Your Grade is F1 Supp")
    elif mark >= 40 and mark < 45:
        print("Your Grade is F2")
    else:
        print("Your Grade is F3")



    
