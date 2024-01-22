print("\n\n\n")
left_right=input("\n\nwelcome to the treasure island \n do you want to go left 'l' or right 'r' ")
if left_right=='r':
    print("Game Over")
elif left_right=='l':
    swim_wait=input("do you want to swim s or wait for boat b")
    if swim_wait=='s':
        print("Game Over")
    elif swim_wait=='b':
        door=input("which door you would like to choose Blue B , Red R, Yello Y ")
        if door=='r' or door=='b':
            print("Game Over")
        
        elif door=='y':
            print("You Won!")
            print(r'''\n 
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
               ''')
