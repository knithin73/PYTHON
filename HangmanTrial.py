stages = ['''
  +---+
  |   |
  O   |
 /|\  |a
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

world_list=["ardvark","baboon","camel"]
import random
chosen_word=random.choices(world_list,k=1)[0]
lives=6
final_word=''
word=[]
for j in range(len(chosen_word)):
    word+="_"
while chosen_word != "".join(word) and lives!=0:
    guess=input("Enter your guess").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            word[i]=guess
    print(word)
    if guess not in chosen_word:
        print(stages[lives])
        lives-=1
    if lives==0:
        print(stages[0])
        print("Game Over!")
    if chosen_word=="".join(word):
        print("You won!")
            
    
    
 