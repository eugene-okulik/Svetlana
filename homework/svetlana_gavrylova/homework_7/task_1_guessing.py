number = 6

while True:
    guess = int(input('Please guess a number between 1 and 10: '))
    if guess == number:
        print('Congratulations! You guessed the number!')
        break
    else:
        print('Try again!')
