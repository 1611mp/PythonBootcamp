# Logical Exercise

weight = int(input("Please enter your weight in kilograms:  "))
if weight >= 50 and weight <=60:
    print("You should avoid cardio. But weight training is good for you!")
elif weight > 60 and weight <= 80:
    print("30 mins cardio for you and then 30 mins weight training.")
elif weight > 80 and weight <=100:
    print("You need to do more cardio and some HIIT sessions.")
else:
    print("We do not have a program for you!")