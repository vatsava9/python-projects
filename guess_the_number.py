# add limitations to human guess

import random

# human guess is where we guess the number that computer thinks
def human_guess(high):
    low = 1
    random_number = random.randint(low,high)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a random number between {low} and {high} : '))
        if guess < random_number and low < guess:
            print('Sorry, too low, guess again')
            low = guess
        elif guess > random_number and high > guess:
            print("Sorry, guess againm Too high")
            high = guess
        else:
            print(f'Select a number between {low} and {high}')


    print(f"You guessed correctly. The number is {random_number}")

# computer guess is where computer guess the number which we think
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        # randint throws an error when low and high are equal
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # high = low, so anything can be used
        feedback = input(f'Is {guess} too high(H) or too low(L), or correct(C)').lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print(f'Comuter guessed the number correctly as {guess}') 
    
print('What game do you want to play human guess (1) or computer guess(2)')
value = int(input(f'Enter the value here : '))

if value == 1:
    human_guess(1000)
elif value == 2:
    computer_guess(1000)
