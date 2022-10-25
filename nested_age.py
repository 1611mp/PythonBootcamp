# Program to check the age limit for concert

age = input("How old are you?:  ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter the concert wearing a wristband!")
    elif age >=21:
        print("You can enter the concert and you're allowed to drink!")
    else:
        print("You are too young to enter the concert!")
else:
    print("You need to enter your age!")