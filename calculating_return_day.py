days = ["Sunday", "Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday"]

day_number = int(input("What is the day number? "))

stay_lenght = int(input("What is your lenght of stay? "))

return_day = (stay_lenght % 7) + day_number

if return_day > 6:
    return_day = return_day % 7


print("The day of the week is", days[return_day])
