import random
playing = True
number = str(random.randint(0, 9))
print("Guess a number from 0 to 9")
print("The game ends when you get it correct")
while playing:
    guess = input("\nCome on, give me your best guess")
    if number == guess:
        print("\nyou win the game!")
        print("the number is ", number)
        break
    else:
        print("nope, that's wrong hahahaha")