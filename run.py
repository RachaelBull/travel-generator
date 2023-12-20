# Essential Imports
import time
import os

def clear_terminal():
    """
    Function to clear the terminal after some inputs
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """
    Main function containing the questions and mostly used variables
    """

    # Choices options and tally
    CARRIBEAN = False
    CANADA = False
    MEXICO_USA= False


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
                clear_terminal()
                print(f"Hello {user_name}, please take time to think about your preferences to the questions,")
                print("as your destination generation will depend heavily on this.\n \n")
                break
    introduction_message()

    # Question No.1

    while True:
        user_selection_one = input("Picture your dream getaway in your head for a moment..\n \n"
          "Now first things first, do you want a relaxing holiday?\n \n"
          "Please answer with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_one == 'Y':
            clear_terminal()
            print("Great choice! Now for the next preference...\n \n")
            break
            CARRIBEAN = True
            
        elif user_selection_one == 'N':
            clear_terminal()
            print("Not a problem, that preference isn't for everyone! Now for the next preference... \n \n")
            break
            CANADA = True
        else:
            print('Invalid input, please try again.\n')

    # Question No.2

    while True:
        user_selection_two = input("Now picture some local walking distance feautures...\n \n"
        "Is a nearby beach within walking distance important to you?\n \n"
        "Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_two == 'Y':
            clear_terminal()
            print("Who doesn't love a beach? Good choice! On to the next question...")
            CARRIBEAN = True
            break
        elif user_selection_two == 'N':
            clear_terminal()
            print("More of get up and explore kind of person, I like it! On to the next question...")
            CANADA = True
            break
        else:
            print('Invalid input, please try again.\n')

    # Question No.3

    while True:
        user_selection_three = input("Now take a few seconds to think of the amazing meals you'll experience there...\n \n"
        "Is it important to you to indulge in local, traditional dishes of the culture?\n \n"
        "Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_three == 'Y':
            clear_terminal()
            print("Open to trying new things, an amazing way to get the locals experience, amazing choice!"
            "And for the next preference...")
            break
            CARRIBEAN = True
            MEXICO_USA = True
        elif user_selection_three == 'N':
            clear_terminal()
            print("Trying new things is risky, why not stick with what you know?! Let's move on...")
            break
            CANADA = True


main()