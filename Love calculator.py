name1=input("\n\nEnter the first name\n")
name2=input("\n\nEnter the second name")
full_name=name1+name2
comb_names=full_name.lower()
count_true=0
for i in comb_names:
    if i == 't':
        count_true += 1

for i in comb_names:
    if i == 'r':
        count_true += 1

for i in comb_names:
    if i == 'u':
        count_true += 1

for i in comb_names:
    if i == 'e':
        count_true += 1

count_love=0
for i in comb_names:
    if i == 'l':
        count_love += 1

for i in comb_names:
    if i == 'o':
        count_love+=1

for i in comb_names:
    if i == 'v':
        count_love+= 1

for i in comb_names:
    if i == 'e':
        count_love+= 1

total=str(count_true)+str(count_love))
total_score=int(total)

if 10>total_score>90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40<total_score<50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}")


 #   ------------------------------------------------------------------------------------
#     print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# # Your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")