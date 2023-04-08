# many times, applications do things under certain conditions
# such as checking if a score is high enough to win a game

number = 3
guessed_successfully = False
while not guessed_successfully: # the `while` code runs until the condition is false
    guess = int(input("Guess my number: "))

    if guess == number: # the `if` code only runs when the condition is true
        print("You got it!")
        guessed_successfully = True

    if guess < number:
        print("Too low!")

    if guess > number:
        print("Too high!")