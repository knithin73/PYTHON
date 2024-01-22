import random
import os
os.system('clear')
deck=[2,3,4,5,6,7,8,9,10,10,10,10,1,11]
def draw_card():
    draw=random.choice(deck)
    return draw
def sumup_cards(card1,card2):
    if card2==11:
        if card1+card2>21:
            card2=1
    sum_cards=card1+card2
    return sum_cards
def who_won(user_deck,dealer_deck):
    if (user_deck>21 and dealer_deck<=21) or (user_deck<dealer_deck):
        print(f"User Sum = {user_deck}, Dealer Sum = {dealer_deck}\n Dealer won")
    elif dealer_deck>21 and user_deck<=21 or (user_deck>dealer_deck):
        print(f"User Sum = {user_deck}, Dealer Sum = {dealer_deck}\n user won")
    elif user_deck==dealer_deck:
        print(f"User Sum = {user_deck}, Dealer Sum = {dealer_deck}\n draw")
want_to_play=input("do you want to play black jack game: y for yes")
user_deck=[]
user_wants_continue = 'y'
if want_to_play=='y' and user_wants_continue == 'y':
    user_card1=draw_card()
    user_deck.append(user_card1)
    sum_user_deck=user_card1
    dealer_card1=draw_card()
    # dealer_card2=draw_card()
    sum_dealer_deck=dealer_card1
    want_to_continue=True
    while want_to_continue==True and sum_dealer_deck<22 and sum_user_deck<22:
        user_card_n=draw_card()
        user_deck.append(user_card_n)
        sum_user_deck=sumup_cards(sum_user_deck,user_card_n)
        dealer_cardn=draw_card()
        # dealer_deck.append(dealer_cardn)    
        sum_dealer_deck=sumup_cards(sum_dealer_deck,dealer_cardn)
        print(user_deck)
        print(f"Currect deck : {user_deck} \ncurrect value of deck {sum_user_deck}\n Dealer card is {sum_dealer_deck}")
        if sum_dealer_deck>21 or sum_user_deck>=21:
            who_won(sum_dealer_deck,sum_user_deck)
        else:    
            user_wants_continue=input("Press y to continue and n to hit:")
            if user_wants_continue=='n':
                want_to_continue=False
                print(f"Currect deck : {user_deck} \ncurrect value of deck {sum_user_deck}")
            