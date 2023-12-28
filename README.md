\# Travel Destination Generator

[Please visit the app here.](*link to be inserted*)

INSERT AN IMAGE HERE SHOWING THE GAME

This app was created to provide assistance to people looking for a new holiday destination or region. This app presents a series of questions to the user to that are 
quite general. The answers to these questions then tally up behind the scenes to general a conclusion once the series of questions come to an end, where the user will then be presented with a generated conclusion that would best fit their preferences.
My current full time job is a Flight Attendent for a long haul airline. The destinations that I have designed the questions around are the places that I travel to very frequently and know quite well. Personally, they are also my favourite destinations that I travel to and would love to share and recommend the experiences that I have here with other. However, although a little similar they do differ from eachother and dependant on whatever the user intends to do on their desired getaway.

## Introduction ##

In this project you will find the following:

1. An introduction message containing guidence to the application with a name input
2. A series of preference question with a yes or no answer option
3. A destination conclusion containing suggestions
4. An option to restart the questions if desired

**App owner goals**

* Create an engaging application that users would be inclined to come back to
* Allow the user to make their own choices
* Store and record user data and answer selections
* Make the app easy to use for users
* Create a clear understanding on the input required to users

**User Goals**

* As a first time user - I want to be able to start the application over if I wanted to
* As a first time user - I want to be given questions related to the application
* As a first time user - I want my destination generation to refect upon the preferences I have selected
* As a first time user - I want clear guidence on the type of input I am allowed to enter
* As a first time user - I want the application to be fast, easy and efficient to use


## UX/UI

### **Strategy** ###

One of the very first things I considered during the planning of this project website was who the audience would be and what they would expect/want.

**What I expect the user would be looking for:**

* Clear, concise instructions on how to use the application
* Displayed with general, interesting and relevent content
* The ability to submit input to the application
* A relevent outcome to the input given
* The option to easily try out and reset the application again

**Target Users:**

* 18 years plus
* People looking for a new destination to travel to
* People who look for multiple features when looking for a new destination to holiday
* People interested in travel
* People interested in learning a little more about other destinations

### **Scope** ###

The features added to ensure that the user gets the best and the most out of their experience are:

* An introduction message when first running the programme, containing clear and concise instructions - this contains information about what the application is for and what the purpose of the application is for.
* A user input feild where the user can enter their name - the terminal will then present a greeting message using the users inputted name to confirm that  the application has recieved the input from the user.
* A series of questions relating to destinations which the user can answer either yes or no to.
* A short conclusion is generated at the end of the questioning section where a broad destination is shown (depending on how the user answers detirmines the tally of destinations that are recorded and shown at the end). A random smaller destination within the generated country is pulled from a small list and a small overview is presented to the user.
* An option to start over and try again is located underneither the conclusion, if the user selects yes then the application will start over - if the user selects no then the user will be presented with a little thankyou message for using this application.

### **Surface** ###

As this application was made to be a text based project using the terminal, no decorative work needed to be done here. However, time has been taken to make sure that the text presents nicely into the terminal and new lines have been added where necessary and where pleasing to the eye.


## Features in more detail ##

**Instructions Section**
![Instructions Section](images/rules-feature.png)

Upon launching the application the above content is displayed to the user. This contains basic and easy instructions on how to use the application and what the expected outputs and inputs will be. The instructions clearly state to the user the need to use only Y for yes and N for no when it comes to answering the questions. After the short instructions and introduction message the user is asked to input their name in the feild below.

**Questions**
![User aknowledgement and start of the questions](images/welcome-feature.png)

Once the user has entered their name, inputting only letter characters, they are they given a little message using their name input that is displayed at the top of the terminal - this acts as a way to tell the user that the application is working and is recieving and recording their inputs properly. 

The start of the questions is then presented underneith in quite an informal but still friendly mannor - the works as a way to create ease and comfort to the user. There is then a short line of instructions reminding the user that they must only answer in the following ways.

**User answering yes:**
![User answering yes to a question](images/user-yes-feature.png)

A short message is displayed to the user depending on which question was answered yes to. This acts as a way to reassure the user still that their input is being recieved and recorded correctly.

**User answering no:**
![User answering no to a question](images/user-no-feature.png)

A short message is displayed to the user depending on which question was answered no to. This acts as a way to reassure the user still that their input is being recorded and recieved correctly.

**Conclusion**
![Generated conclusion](images/conclusion-feature.png)

Once the series of questions have been answered appropriatly by the user, a short conclusion will be displayed to the user which would have been generated depending on if the answers related to the destination or not. This conclusion will include a small message recommeding one or more destinations. An option is then presented at the bottom of this conclusion asking the user if they would like to reset the travel generator application and start again.

**No to restarting the application**
![No to the reset question](images/no-reset.png)

If the user was t0 answer no to the application reset question then this is the short and final message the user will be presented with. If the user then wanted to decide that they actually did want to reset the game then this can be achieved through pressing the run programme button with will restart the application up again.

**Yes to restarting the application**
![Yes to the reset question](images/yes-reset.png)

If the user was to answer yes to the application reset question then the application will be reset completely and the user will be brought right back to the start again. This does ask the user to input their name again, this is incase there is more people present who would like to generate their own destination and want a more personalised approach.

## Dependencies

**Import OS**

The import os module was used quite consistantly throughout my python based project. This allowed me to interact with the operating system which I needed to do when it came to clearing the terminal for a tidier looking terminal - opting for a better user experience overall.

**Import Random**

Import random was using during my project but not in huge amounts. I used this to be able to pull out a random smaller destination out of my lists to display to the user.

## Technologies Used 

* [Python](https://www.python.org/)
  This technology was used to create the entire project.
* [GitHub](https://github.com/)
  This technology was used to securely store all of my code in a resporitory.
* [Heroku](https://www.heroku.com/home?)
  This technology was used to easily and efficently deploy my application project.
* [Git](https://git-scm.com/)
  This technology was used to make changes to my code aswell as manage version control.
* [Codeanywhere](https://app.codeanywhere.com/)
  This technology was used as my coding development environment.
* [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
  This technology was used to validate my python code.
* [Slack](https://slack.com/intl/en-ie/)
  This technology was used a lot in order to easily find solutions from other students and the educational content provided within the channels.

  ## Testing

**Code Institute Python Code Validator**
![Errors List](images/validator-errors-list.png)

When I first passed my code through the validator it was displaying multiple errors and warnings which I worked through and then got into the habbit of writing the rest of the code on how it would be passed through the validator.

![Errors Resolved](images/passed-validator.png)

After working through the code and learning how to write the rest of the code in the type of format that the validator would accept I resolved all errors and warnings.

**User Name Input**

When I created the feature in my project to allow the user to enter their name into the terminal I wanted the application to only allow letter characters and not numbers. The length of the name isn't something that I saw to be a problem which I did add at first and then later look out incase some users wished to have a longer name than the average. For this input my code only allows users to procceed with letters and not numbers or special characters which I will show below: 

![Invalid Name](images/name-invalid.png)

Once the user name input is accepted by the application the following message is shown as clear indication:
![Valid Name](images/name-valid.png)

**User Questions Input**

When the questions feature was implimented into my project I intended to keep the accepted input to the questions easy and simple. The instuctions and appropriate ways to answer the questions are explained in the introduction section of the application just before the user is asked to enter their name. Reminders of how to answer are constantly being shown at every question throughout the project. The only accepted input for these questions are y or Y for yes and n or N for no. If the user was to input something that did not match the required, then the following error message would be displayed to the user:

![Invalid Questions Input](images/questions-invalid.png)

As shown above - a small error message is presented to the user with another reminder on how to answer the question. The question is then repeated for the user to try again. 

If the user was to answer with accepted and appropriate input, then the following will be displayed to the user:

![Valid Questions Input](images/questions-valid.png)

As shown above - a small acknowledgment message is shown to the user to let them know that their data has been successfully recorded. They are then presented with the next question.

**User Restart Input**

Since first planning and starting the project my intention for the user was always to have a restart option presented to them at the end of the question series. This makes it easier for the user to go back and rethink any questions they may have answered to try and get a new destination if they didn't quite agree with the one that had been generated for them. This again, is a y or Y for yes and a n or N for no. If anything else is inputted into this field by the user then an error message and an option to try again will be displayed to the user.

*Here is what the question will look like before any input is given*
![No Input Restart Question](images/restart-question.png)

*Once incorrect input is given the application will present the user with the following message:*
![Invalid Input Restart Question](images/invalid-restart.png)

*And once the user has selected a valid input, 1 of 2 outcomes will be presented to the user:*
![Restart Valid Outcome One](images/restart-valid-one.png)
![Restart Valid Outcome Two](images/restart-valid-two.png)

**Destination Answer Tally**

Here I will take the time to explain how my tally system works within my code and how I have tested all possible outcomes.

There are 3 destinations and categories that the questions are based around - USA/Mexico, Canada and Carribean. Everytime the user selects an answer, either yes or no, one or more destinations will increment their value by one, for example:

*Tally Example*
![Tally Example](images/tally-example.png)

One the questions have finished the values of each destination will be compared with eachother to detirmine if any values are the same - to which a message will display recommending two destinations. Or if theres one value that is bigger than the others - to which a message will display recommending only one destination. For example:

*Tally Comparison*
![Tally Comparison](images/comparison-example.png)

*Tally Testing*

* Using a pen and paper I have recorded the expected outcomes of certain answers and confirmed that all outcomes have a possiblily to show to the user based on their answer choices - making sure that no code is useless within my project.

**Destination Random List Pull**

To make things a little more detailed and personalised, I created 3 small lists containing different areas of the generated destination. So once a destination has been confirmed through the conclusion part of the application (the comparison code) then through a generated message a small part of the destination will be pulled out at random from the lists and places into the message. Here is an example of this:

*Random List Example*
![List Example](images/list-example.png)

## Bugs Known & Fixed

The first bug I had come across was when generating a destination to present the user with a little detailed conclusion. 

**Here is the error message that was being returned to me when the bug existed**
![Conclusion Bug Unfixed](images/conclusion-bug.png)

Here the error, from what I could make of it, was telling me that it couldn't accept me trying to access some variable data contained in another function into this one if I passed them as peramiters and arguments. I was stuck on this for a little while, I did try to change my variables to global variables which did also create another bug all together as my variable was then being called and changed in too many places. 

**Here is my fixed result to display the test destination message at the time of the initial development**
![[Fixed Bug Outcome](images/conclusion-bug-fix-two.png)

Here I was able to successfully display a test conclusion message at the time of the early stages of development. Here there are no errors and no loops occuring (which happened on a few occasions before finding the proper fix).

**Here is how I fixed the bug within the code**
![Fixed Bug Code](images/conclusion-bug-fix-two.png)

I created a loop within another funtion to check if all was true, then the other function could run. This did however, prevent this actual function to be called directly into the main function where I would have liked it - but with more practice and knowledge I intent to work towards this. However, this fix is still very stable and efficient. This allowed the function to have access to certain information that I was trying to access through passing arguments.