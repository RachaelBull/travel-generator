# Essential Imports
import time
import os
import random

def clear_terminal():
    """
    Function to clear the terminal after some inputs
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Destinations list

carribean_destinations = ['St.Lucia', 'Barbados', 'Antigua', 'Bahamas']
usa_mexico_destinations = ['Las Vegas', 'Cancun', 'New York', 'Chicago']
canada_destinations = ['Vancouver', 'Calgary']

def introduction_message():
    """
    Displays an introduction message to the user to indicate what this application is for
    """
    clear_terminal()
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


def user_questions():
    """
    Displays the questions and answer options to the user
    """
    # To keep a tally of destinations depending on the users selected answer
    carribean = 0
    usa_mexico = 0
    canada = 0
    # Question No,1

    while True:
        user_selection_one = input("Picture your dream getaway in your head for a moment..\n \n"
          "Now first things first, do you want a relaxing holiday?\n \n"
          "Please answer with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_one == 'Y':
            clear_terminal()
            carribean += 1 #Increment destination tally
            usa_mexico += 1
            print("Great choice! Now for the next preference...\n \n")
            break
        elif user_selection_one == 'N':
            clear_terminal()
            canada += 1 #Increment destination tally
            print("Not a problem, that preference isn't for everyone! Now for the next preference... \n \n")
            break
        else:
            clear_terminal()
            print('Invalid input, please try again.\n')

    # Question No.2

    while True:
        user_selection_two = input("Now picture some local walking distance feautures...\n \n"
        "Is a nearby beach within walking distance important to you?\n \n"
        "Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_two == 'Y':
            clear_terminal()
            carribean += 1
            print("Who doesn't love a beach? Good choice! On to the next question...")
            break
        elif user_selection_two == 'N':
            clear_terminal()
            usa_mexico += 1
            print("More of get up and explore kind of person, I like it! On to the next question...")
            break
        else:
            clear_terminal()
            print('Invalid input, please try again.\n')

    # Question No.3

    while True:
        user_selection_three = input("Now take a few seconds to think of the amazing meals you'll experience there...\n \n"
        "Is it important to you to indulge in local, traditional dishes of the culture?\n \n"
        "Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_three == 'Y':
            clear_terminal()
            carribean += 1
            usa_mexico += 1
            print("Open to trying new things, an amazing way to get the locals experience, amazing choice!"
            "And for the next preference...")
            break
        elif user_selection_three == 'N':
            clear_terminal()
            canada += 1
            print("Trying new things is risky, why not stick with what you know?! Let's move on...")
            break
        else:
            clear_terminal()
            print('Invalid input, please try again.\n')

    # Question No.4

    while True:
        user_selection_four = input("Your days should have started to mould inside your imagination by now,"
        "but if not that's fine, we're not quite finished yet!\n \n"
        "Would you say that you are an adventurous individual that loves to explore?\n \n"
        "Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_four == 'Y':
            clear_terminal()
            canada += 1
            print("What better way to see the most of the destination! Just a few more questions...")
            break
        elif user_selection_four == 'N':
            clear_terminal()
            carribean += 1
            print("Holidays are for relaxing right? Relaxing is just the way to do it. Just a few more questions...")
            break
        else:
            clear_terminal()
            print('Invalid input, please try again.\n')

    # Question No.5
    while True:
        user_selection_five = input("We're almost reaching the end! Now we need to think about that hole in the pocket that"
        "wallet will burn if not careful..\n \n"
        "Do you wish to go somewhere on the cheaper range of the currency exchange rate?\n \n"
        "Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_five == 'Y':
            clear_terminal()
            canada += 1
            print("The cheaper the holiday the higher the class we fly, right?! And for the final question...")
            break
        elif user_selection_five == 'N':
            clear_terminal()
            usa_mexico += 1
            print("Holidays aren't often enough, why not splash out?! And for the final question...")
            break
        else:
            clear_terminal()
            print("Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")

    # Question No.6
    while True:
        user_selection_six = input("The final question... It's no secret that everyone has varied opinions when it"
        "comes to children when on holday.\n \n"
        "Would you like your destination to be a childrens destination aswell as an adults?\n \n"
        "Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")
        if user_selection_six == 'Y':
            clear_terminal()
            usa_mexico += 1
            print("The more the merrier! Who doesn't love sharing unforgettable moments with our little ones?")
            break
        elif user_selection_six == 'N':
            clear_terminal()
            carribean += 1
            print("Everyone needs a break sometimes! They can come next time.. right?")
            break
        else:
            clear_terminal()
            print("Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")  

    while True:
        destination_conclusion(carribean, usa_mexico, canada)
        break

def destination_conclusion(carribean, usa_mexico, canada):
    """
    Function to determine which destination would be best for the user
    """

    # Destinations Lists

    carribean_destinations = ['St.Lucia', 'Barbados', 'Antigua', 'The Bahamas']
    usa_mexico_destinations = ['Las Vegas', 'Cancun', 'New York', 'Chicago']
    canada_destinations = ['Vancouver', 'Calgary']

    # Variables for random list item selection

    carribean_selection = random.choice(carribean_destinations)
    usa_mexico_selection = random.choice(usa_mexico_destinations)
    canada_selection = random.choice(canada_destinations)


    clear_terminal()
    while True:
        if carribean > usa_mexico:
            print("Based on your preferences, a Carribean getaway would be perfect for what you are looking for."
            f"{carribean_selection} would be a great place for you to try out. Pristine waters, bright sandy beaches,"
            "amazing food.. what's more could you want?")
            break
        elif carribean < usa_mexico:
            print("Based on your preferences, a USA or Mexican getaway would be the perfect choice for you!"
            f"{usa_mexico_selection} is a great destination to consider. Great traditional cuisine, great weather at the right"
            "time of year, a home away from home.. right?")
            break
        elif carribean > canada:
            print("Based on your preferences, a Carribean getaway would be perfect for what you are looking for."
            f"{carribean_selection} would be a great place for you to try out. Pristine waters, bright sandy beaches,"
            "amazing food.. what's more could you want?")
            break
        elif carribean < canada:
            print("Canada for you!")
            break
        elif canada > usa_mexico:
            print("Canada for you!")
            break
        elif canada < usa_mexico:
            print("Based on your preferences, a USA or Mexican getaway would be the perfect choice for you!"
            f"{usa_mexico_selection} is a great destination to consider. Great traditional cuisine, great weather at the right"
            "time of year, a home away from home.. right?")
            break
        elif carribean == usa_mexico:
            print("Carribean or USA/Mexico for you!")
            break
        elif carribean == canada:
            print("Carribean or Canada for you!")
            break
        elif usa_mexico == canada:
            print("USA/Mexico or Canada for you!")
            break
    request_start_again()

def request_start_again():
    """
    Function to ask the user whether they would like to try and questions again for a different output
    """

    user_restart = input("Would you like to generate a new destination and start the questions over? Please answer Y/N: \n")

    while True:
        if user_restart == "Y":
            main()
        elif user_restart == "N":
            clear_terminal()
            print("Perfect destination, right?! Thankyou for using this travel destination generator.")
        else:
            print("Please answer this with 'Y' for yes or 'N' for no, be sure to use capitals for this: ")


def main():
    """
    Function to call other functions in order
    """

    introduction_message()
    user_questions()

main()