print(f'''
Welcome to Treasure Island.
Your mission is to find the treasure
''')
selector = input("Left or Right? ('L' / 'R') :").lower()

if(selector != "l"):
    print("You fell into a hole. Game Over.")
else:
    selector = (input('''Swim or Wait?''')).lower()
    if(selector != "wait"):
        print("Attacked by trout. Game Over.")
    else:
        selector = (input('''Which door? (Red, Blue, Yellow)''')).lower()
        if(selector == "yellow"):
            print("You Win!")
        elif(selector == "red"):
            print("Burned by fire. Game Over.")
        elif(selector == "blue"):
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")