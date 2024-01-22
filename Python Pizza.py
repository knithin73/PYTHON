print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
bill=0
# pepperoni=input("would you like to have pepperoni ? type Y or N \n")
# extra_cheese=input("would you like to have extra cheese ? type Y or N \n")
if size=='S':
    bill=15
    if add_pepperoni=='Y':
        bill+=2
    if extra_cheese=='Y':
        bill+=1
        print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is:${bill}")
    else :
        print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is:${bill}")     
    
if size=='M':
    bill=20
    if add_pepperoni=='Y':
        bill+=3
    if extra_cheese=='Y':
        bill+=1
        print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is:${bill}")   
    else :
        print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is:${bill}") 
    
if size=='L':
    bill=25
    if add_pepperoni=='Y':
        bill+=3
    if extra_cheese=='Y':
        bill+=1
        print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is:${bill}")   
    else :
        print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is:${bill}") 
    