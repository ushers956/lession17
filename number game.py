import random
playing = True
number = random.randint(0,9)
print("i will generate a number from 0 to 9, and you have to guess the numbe one digit a time")
print("the game ends when you get one hero")

while playing:
    guess = int(input("give me your best guess \n"))
    if number == guess:
        print("you win the game")
        print("the number was",number) 
        break

    else:
        print("your guess isn't quite right, try again")