while(True):
    try:
        print("Welcome!!! Try to guess the Secrect Number and Win!!!")
        secret_number = 25
        guess = int(input("Guess the Hidden Number: "))
        if guess == secret_number:
            print("You have WON!!!! Congratulation!!!")
            break
        else:
            print("Keep trying. Maybe next time you win!")
    except ValueError:
            print("Please just Numbers.")