import os
from higher_lower_game_data import data
from higher_lower_game_data import vs
from higher_lower_game_data import logo
import random
os.system('clear')
print(logo)

def compare(a,b):
    if (a>b):
        return "a"
    elif (a<b):
        return "b"
    else:
        return "equal"
count=0   
# global follower_countA
its_true=True
compareA=(random.choice(data))
while its_true:
    print(f"Compare A: {compareA.get('name')} , a {compareA.get('description')}, from {compareA.get('country')}")
    follower_countA=compareA.get('follower_count')
    print(follower_countA)

    print(vs)

    compareB=random.choice(data)
    if compareB==compareA:
        compareB=random.choice(data)
    print(f"Compare B: {compareB.get('name')} , a {compareB.get('description')}, from {compareB.get('country')}")
    follower_countB=compareB.get('follower_count')
    print(follower_countB)
    


    A_or_B =input("Who has more followers? Type 'A' or 'B':").lower
    greater_value=compare(follower_countA,follower_countB)
    if greater_value==A_or_B:
        print("\nCorrect")
        compareA=compareB
        its_true=True
        count+=1
        os.system("clear")
        print(f"You Score is {count} \nNow compare this \n")
    else:
        print("You loose")
        its_true=False