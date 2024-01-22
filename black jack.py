import random
deck=[2,3,4,5,6,7,8,9,10,10,10,10,1,11]
user_sum=random.choice(deck)
user_sum=random.choice(deck)+user_sum
dealer_sum=random.choice(deck)
dealer_sum=random.choice(deck)+dealer_sum


#function down
def user_continue():
        while dealer_sum <21 and user_sum <21:
            if dealer_sum>17:
                x_dealer_card1=random.choice(deck)
                if x_dealer_card1+dealer_sum>21:
                    x_dealer_card2=random.choice(deck)
                    dealer_sum+=x_dealer_card2
                    
                else:
                    dealer_sum+=x_dealer_card1
            if dealer_sum>=21:
                break
                

            user_sum=random.choice(deck)+user_sum
            if user_sum>21:
                break

            dealer_sum=random.choice(deck)+dealer_sum
            if dealer_sum>=21:
                break
            

        if user_sum==21 and dealer_sum==21:
            print("tie")

        elif dealer_sum>user_sum and dealer_sum<=21:
            print(f"{dealer_sum},{user_sum},4Dealer win")
        elif dealer_sum<user_sum and user_sum <=21:
            print(f"{dealer_sum},{user_sum},5User win")
        elif dealer_sum>user_sum and dealer_sum>21:
            print(f"{dealer_sum}, {user_sum} ,user win")

        elif dealer_sum<user_sum and user_sum>21:

            print(f"{dealer_sum}, {user_sum},dealer win")

#function up

user_input=input(f"sum={user_sum} \n would you like to continue y or n")
if user_input=='y':
    user_wish_continue=True
    user_continue()
else:
    user_wish_continue=False
    if user_sum <=21 and user_sum>dealer_sum:
        print("User Win")
    elif dealer_sum<=21 and dealer_sum>user_sum:
        print(f"{dealer_sum},{user_sum},Dealer wins")
    elif dealer_sum>21 and user_sum<=21:
        print(f"{dealer_sum},{user_sum},User wins")
    elif user_sum>21 and dealer_sum<=21:
        print(f"{dealer_sum},{user_sum},Dealer_sum")

