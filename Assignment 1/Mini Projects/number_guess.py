import random

number = int(input("Enter the top of range: "))
guesses = 0

random_number = random.randint(0, number)

while True:
    guess = int(input("Make a guess: "))
    guesses += 1

    if guess == random_number:
        print("You got it!!!")
        break
    elif guess > random_number:
        print("You are above the Number")
    else:
        print("You are below the Number")

print("You got it in guesses: ", guesses)