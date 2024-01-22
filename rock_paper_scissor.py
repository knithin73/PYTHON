import os
os.system('clear')
rock = '''rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
rps_choise=int(input("Enter for Rock - 0 , Paper - 1 , Scissor - 2\n"))

if rps_choise==0:
    against=random.randint(0,2)
    if against==1:
        print(paper)
        print("You lost")
    elif against==2:
        print(scissors)
        print("You win!")
    elif against==0:
        print(rock)
        print("Its a draw")


elif rps_choise==1:
    against=random.randint(0,2)
    if against==1:
        print(rock)
        print("You won!")
    elif against==2:
        print(scissors)
        print("You lost!")
    elif against==0:
        print(paper)
        print("Its a draw")

elif rps_choise==1:
    against=random.randint(0,2)
    if against==1:
        print(rock)
        print("You lost")
    elif against==2:
        print(paper)
        print("You won!")
    elif against==0:
        print(scissors)
        print("Its a draw")



# if rps_choise==0:
#     list1=[paper,scissors]
#     com_rps=random.sample(list1,1)
#     print(com_rps)
#     if com_rps==scissors:
#         print("You Won!")
#     elif com_rps==paper:
#         print("You Loose!")
    
# elif rps_choise==1:
#     list1=[rock,scissors]
#     com_rps=random.sample(list1,1)
#     print(com_rps)
#     if com_rps==rock:
#         print("You Won!")
#     elif com_rps==scissors:
#         print("You Loose!")
    

# elif rps_choise==2:
#     list1=[paper,rock]
#     com_rps=random.sample(list1,1)
#     print(com_rps)
#     if com_rps==paper:
#         print("You Won!")
#     elif com_rps==rock:
#         print("You Loose!")



    

