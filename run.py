# Essential Imports
import time

def introduction_message():
    """
    Displays an introduction message to the user to indicate what this application is for
    """
    print("Welcome to this destination suggestions application.\n")
    print("You will be asked multiple general questions about your destination preferences which you will answer yes or no.\n")
    print("After all questions have been answered you will then be displayed with a destination recommendation tailored to your preferences.\n")
    print("An optional prices average for the month of travel can also be displayed after this conclusion.")

    # Username validation to only allow letters
    while True:
        user_name = input("Please enter your name here: \n")
        if not (user_name).isalpha() or (user_name == ''):
            print('Invalid name, please try again.\n')
        else:
            print(f"Hello {user_name}, please take time to think about your preferences to the questions,")
            print("as your destination generation will depend heavily on this.")
            break


def main():
    """
    To call all functions in one main area, in an orderly form
    """

    introduction_message()

main()