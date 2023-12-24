# Essential Imports
import os  # To interact with the underlying operating system
import random  # To grab a random destination out of the lists


def clear_terminal():
    """
    Function to clear the terminal after the user
    answers a question or unputs some data.
    Prevents the terminal from looking too crowded.
    Code for this is from stack overflow -
    clearly credited in the README file.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def introduction_message():
    """
    Displays an introduction message to the user to indicate what this
    application is for.
    Provides the user with rules on how to enter input and what the
    application will accept as valid input.
    """
    clear_terminal()
    print("Welcome to this destination suggestions application.\n")
    print("You will be asked multiple general questions about your destination"
          " preferences which you will answer yes or no -"
          " Y for yes and N for no.\n")
    print("After all questions have been answered you will then be displayed "
          "with a destination recommendation tailored to your preferences.\n")
    print("The option to reset the travel generator will be presented at the "
          "end of the series of questions. Enjoy!")

    # Username validation to only allow letters and no empty entries.
    while True:
        user_name = input("\nPlease enter your name here:\n")
        if not (user_name).isalpha() or (user_name == ''):
            clear_terminal()
            print("Invalid name, please try again.. "
                  "using only letter characters.")
        else:
            clear_terminal()
            print(f"Hello {user_name}, please take time to think about your "
                  "preferences to the questions,")
            print("as your destination generation will depend on this.\n \n")
            break


def user_questions():
    """
    Displays the questions and answer options to the user.
    A brief response is given back to the user to confirm
    that the users response has been succesfully recorded.
    """
    # To keep a tally of destinations depending on the users selected answer
    carribean = 0
    usa_mexico = 0
    canada = 0

    # Question No,1

    while True:
        user_choice_one = input("Picture your dream getaway for a moment..\n"
                                "\nNow first thing, do you want to relax?\n"
                                "\nPlease answer with Y/N:\n")
        if user_choice_one.lower() == 'y':
            clear_terminal()
            carribean += 1  # Increment destination tally
            usa_mexico += 1
            print("Great choice! Now for the next preference...\n \n")
            break
        elif user_choice_one.lower() == 'n':
            clear_terminal()
            canada += 1  # Increment destination tally
            print("Not a problem, that preference isn't for everyone! "
                  "Now for the next preference... \n \n")
            break
        else:
            clear_terminal()
            print("Invalid input, please try again.\n"
                  "Using Y for yes and N for no.\n\n")

    # Question No.2

    while True:
        user_selection_two = input("Now picture some local feautures...\n \n"
                                   "Is a nearby beach within walking distance "
                                   "important to you?\n \n"
                                   "Please answer this with Y/N:\n")
        if user_selection_two.lower() == 'y':
            clear_terminal()
            carribean += 1
            print("Who doesn't love a beach?"
                  " On to the next question...\n\n")
            break
        elif user_selection_two.lower() == 'n':
            clear_terminal()
            usa_mexico += 1
            print("More of get up and explore kind of person, I like it! "
                  "On to the next question...\n\n")
            break
        else:
            clear_terminal()
            print("Invalid input, please try again.\n"
                  "Using Y for yes and N for no.\n\n")

    # Question No.3

    while True:
        user_selection_three = input("Now take a few seconds to think of the "
                                     "amazing meals you'll experience there..."
                                     "\n \n"
                                     "Is it important to you to indulge in "
                                     "local, traditional and cultural dishes?"
                                     "\n \n"
                                     "Please answer this with Y/N:\n")
        if user_selection_three.lower() == 'y':
            clear_terminal()
            carribean += 1
            usa_mexico += 1
            print("Open to trying new things, an amazing way to get the "
                  "locals experience, amazing choice!"
                  " And for the next preference...\n\n")
            break
        elif user_selection_three.lower() == 'n':
            clear_terminal()
            canada += 1
            print("Trying new things is risky, why not stick with what you "
                  "know?! Let's move on...\n\n")
            break
        else:
            clear_terminal()
            print("Invalid input, please try again.\n"
                  "Using Y for yes and N for no.\n\n")

    # Question No.4

    while True:
        user_selection_four = input("Your days should have started to mould "
                                    "inside your imagination by now, "
                                    "if not, we're not finished yet!\n\n"
                                    "Would you say that you are an adventurous"
                                    " individual that loves to explore?\n \n"
                                    "Please answer this with Y/N:\n")
        if user_selection_four.lower() == 'y':
            clear_terminal()
            canada += 1
            print("What better way to see the most of the destination! "
                  "Just a few more questions...\n\n")
            break
        elif user_selection_four.lower() == 'n':
            clear_terminal()
            carribean += 1
            print("Holidays are for relaxing right? Relaxing is just the way "
                  "to do it. Just a few more questions...\n\n")
            break
        else:
            clear_terminal()
            print("Invalid input, please try again.\n"
                  "Using Y for yes and N for no.\n\n")

    # Question No.5
    while True:
        user_selection_five = input("We're almost reaching the end! Now we "
                                    "need to think about the hole that wallet"
                                    " will burn if not careful..\n \n"
                                    "Do you wish to go somewhere on the "
                                    "cheaper range of the currency exchange "
                                    "rate?\n \n"
                                    "Please answer this with Y/N:\n")
        if user_selection_five.lower() == 'y':
            clear_terminal()
            canada += 1
            print("The cheaper the holiday the higher the class we fly, right?"
                  " And for the final question...\n\n")
            break
        elif user_selection_five.lower() == 'n':
            clear_terminal()
            usa_mexico += 1
            print("Holidays aren't often enough, why not splash out?! "
                  "And for the final question...\n\n")
            break
        else:
            clear_terminal()
            print("Invalid input, please try again.\n"
                  "Using Y for yes and N for no.\n\n")
    # Question No.6

    while True:
        user_selection_six = input("The final question... It's no secret that "
                                   "everyone has varied opinions when it "
                                   "comes to children when on holday.\n \n"
                                   "Would you like your destination to be a "
                                   "childrens destination aswell as an adults?"
                                   "\n \n"
                                   "Please answer this with Y/N:\n")
        if user_selection_six.lower() == 'y':
            clear_terminal()
            usa_mexico += 1
            canada += 1
            print("The more the merrier! Who doesn't love sharing amazing "
                  "moments with our little ones?")
            break
        elif user_selection_six.lower() == 'n':
            clear_terminal()
            carribean += 1
            print("Everyone needs a break sometimes! They can come next "
                  "time.. right?")
            break
        else:
            clear_terminal()
            print("Invalid input, please try again.\n"
                  "Using Y for yes and N for no.\n\n")

    while True:
        destination_conclusion(carribean, usa_mexico, canada)
        break


def destination_conclusion(carribean, usa_mexico, canada):
    """
    Function to determine which destination would be best for the user
    based on what they have answered to the questions.
    The tally gets recorded throughout each answer that is selected
    and a random region of that specific country is then pulled from
    the destinations list using the random() method.
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
            print("Based on your preferences, a Carribean getaway would be "
                  "perfect for what you are looking for.")
            print(f"{carribean_selection} would be a great place for you to "
                  "try out.")
            print("Pristine waters, bright sandy beaches,"
                  " amazing food.. what more could you want?")
            break
        elif carribean < usa_mexico:
            print("Based on your preferences, a USA or Mexican getaway would "
                  "be the perfect choice for you!")
            print(f"{usa_mexico_selection} is a great destination to"
                  " consider.")
            print("Great traditional cuisine, great weather at the "
                  "right time of year, a home away from home.. right?")
            break
        elif carribean > canada:
            print("Based on your preferences, a Carribean getaway would be "
                  "perfect for what you are looking for.")
            print(f"{carribean_selection} would be a great place for you to "
                  "try out.")
            print("Pristine waters, bright sandy beaches,"
                  " amazing food.. what more could you want?")
            break
        elif carribean < canada:
            print("Based on your preferences, a Canadian getaway would be the "
                  "perfect choice for you!")
            print(f"{canada_selection} is where you can only dream of.")
            print("Why not try it out?\n"
                  "Adventures around every corner, great atmospheres and so "
                  "much to explore!")
            break
        elif canada > usa_mexico:
            print("Based on your preferences, a Canadian getaway would be the "
                  "perfect choice for you!")
            print(f"{canada_selection} is where you can only dream of.")
            print("Why not try it out?\n"
                  "Adventures around every corner, great atmospheres and so "
                  "much to explore!")
            break
        elif canada < usa_mexico:
            print("Based on your preferences, a USA or Mexican getaway would "
                  "be the perfect choice for you!")
            print(f"{usa_mexico_selection} is a great destination to"
                  " consider.")
            print("Great traditional cuisine, great weather at the "
                  "right time of year, a home away from home.. right?")
            break
        elif carribean == usa_mexico:
            print("Based on your preferences, a Carribean, USA or Mexican "
                  "getaway would be perfect for you!")
            print("If you are swaying towards a USA or Mexican holiday .."
                  f" then defintely consider {usa_mexico_selection}.")
            print("And if you are doting more towards a Carribean escape..")
            print(f"{carribean_selection} would be the best time!")
            print("Both are amazing but it comes down to one question... "
                  "To beach or not to beach?")
            break
        elif carribean == canada:
            print("Based on your preferences, a Carribean or Canadian "
                  "getaway would be perfect for you!")
            print("If you are swaying towards a Canadian holiday .."
                  f" then defintely consider {canada_selection}.")
            print("And if you are doting more towards a Carribean escape..")
            print(f"{carribean_selection} would be the best time!")
            print("Both are amazing but it comes down to one question... "
                  "To beach or not to beach?")
            break
        elif usa_mexico == canada:
            print("Based on your preferences, a Canadian, USA or Mexican "
                  "getaway would be perfect for you!")
            print("If you are swaying towards a USA or Mexican holiday .."
                  f" then defintely consider {usa_mexico_selection}.")
            print("And if you are doting more towards a Canadian escape..")
            print(f"{canada_selection} would be the best time!")
            print("Both are amazing but it comes down to one question... "
                  "To explore or not to explore?")
            break
    while True:
        request_start_again()
        break


def request_start_again():
    """
    Function to ask the user whether they would like to try the questions
    again for a different destination or if they are happy with the
    generation that was given.
    """

    while True:
        user_restart = input("\n \nWould you like to generate a new "
                             "destination and start the questions over?"
                             "Please answer Y/N:\n")
        if user_restart.lower() == "y":
            clear_terminal()
            main()
            break
        elif user_restart.lower() == "n":
            clear_terminal()
            print("Perfect pick, right? Thankyou for using this travel "
                  "destination generator.")
            break
        else:
            clear_terminal()
            print("Please answer this with Y/N:\n")


def main():

    """
    Function to call all main functions in order to try and
    keep the code tidy and readable.
    """

    introduction_message()
    user_questions()


main()
