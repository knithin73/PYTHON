height = float(input("enter www "))
# Enter your weight in kilograms e.g., 72
weight = int(input("enyerdfvwdfv "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=(weight/height**2)

if BMI <18.5:
    print(f"Your BMI is {BMI}, you are underweight. ")
elif BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI< 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI< 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif:
    print(f"Your BMI is {BMI}, you are clinically obese.")

