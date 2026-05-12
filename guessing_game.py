import random 
import os

guess = random.randint(1, 100)
while True:
        choose = input("Choose a difficulty level: 1.Easy, 2.Medium, 3.Hard: ").lower()

        if choose == "easy": 
                print("Great! You have selected Easy difficulty level.\n Let's start the game!")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You have 10 attempts to guess the number.")
                for attempt in range(10):
                        try:
                                user_guess = int(input("Guess a number between 1 and 100: "))
                                if user_guess < guess:
                                        print("Too Low! Try again.")
                                elif user_guess > guess:
                                        print("Too High! Try again.")
                                else:
                                        print("Congratulations! You Have Guessed the Number!")
                                        break
                        except ValueError:
                                print("Invalid input. Please enter a number between 1 and 100.")

                        attempt -=  1 
        elif choose == "medium":
                print("Great! You have selected Medium difficulty level.\n Let's start the game!")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You have 7 attempts to guess the number.")
                for attempt in range(7):
                        try:
                                user_guess = int(input("Guess a number between 1 and 100: "))
                                if user_guess < guess:
                                        print("Too Low! Try again.")
                                elif user_guess > guess:
                                        print("Too High! Try again.")
                                else:
                                        print("Congratulations! You Have Guessed the Number!")
                                        break
                        except ValueError:
                                print("Invalid input. Please enter a number between 1 and 100.")

                        attempt -=  1 
        elif choose == "hard": 
                print("Great! You have selected Hard difficulty level.\n Let's start the game!")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You have 5 attempts to guess the number.")
                for attempt in range(5):
                        try:
                                user_guess = int(input("Guess a number between 1 and 100: "))
                                if user_guess < guess:
                                        print("Too Low! Try again.")
                                elif user_guess > guess:
                                        print("Too High! Try again.")
                                else:
                                        print("Congratulations! You Have Guessed the Number!")
                                        break
                        except ValueError:
                                print("Invalid input. Please enter a number between 1 and 100.")

                        attempt -=  1 
        else:
                print("Invalid choice. Please choose a valid difficulty level.")