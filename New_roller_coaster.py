print("\n \n \n\n\nWelcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height > 120:
  age=int(input("what is your age "))
  if age <12:
    bill=5
    print("children tickets are $5")
  elif age <=18 :
    bill=7
    print("Youth tickets are $7")
  elif age>=45 and age <=55:
    bill=0
    print("Free tickets")
  else :
    bill=12
    print("Adult tickets are $12")
    
  photo=input("Do you want your photo to be taken - Y or N \n")
  if photo=='y' or photo=='Y':
    bill+=3
    print(f"Your total Bill is {bill}")

else:
  print("You should be above 120cm in height to ride the rollercoaster!")
  
