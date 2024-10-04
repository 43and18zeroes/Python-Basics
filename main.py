import random

def number_guessing_game():
    secret_number = random.randint(1, 20)
    guesses_taken = 0

    print('Ich habe mir eine Zahl zwischen 1 und 20 ausgedacht.')

    while guesses_taken < 6:
        guess = int(input('Rate mal: '))
        guesses_taken += 1

        if guess < secret_number:
            print('Deine Zahl ist zu klein.')
        elif guess > secret_number:
            print('Deine Zahl ist zu groß.')
        else:
            break

    if guess == secret_number:
        print('Gut gemacht! Du hast die Zahl in ' + str(guesses_taken) + ' Versuchen erraten!')
    else:
        print('Leider verloren. Die Zahl war ' + str(secret_number))

number_guessing_game()