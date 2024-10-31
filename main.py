from random import randint

random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)

while True:
    Guess = int(input("enter a guess number between 1 and 10"))

    if guess > random_num:
        print("to high! Try again")

    elif guess < random_num:
        print( "to low! Try agian ")
    # TODO: Print Too low!, Try again.
    else:
        print("Print Congratulations! You've guessed the number")
        break
