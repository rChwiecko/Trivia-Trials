# TriviaTrials 
### Group: 69
### Group Members: Ryan Chwiecko, Arjun Singh Atwal, Jin Zhao, Sonia Sharma, Sahej Chawla 
### Course: CS 2212
### Assignment Type: Implementation and Delivery Documentation
### Current Complete Build is on refactoring Branch


## Description of Software 
This game application seeks to encourage individuals to effectively apply previous knowledge to concepts in an interactive and immersive environment with an aesthetic user interface experience designed for 16-18 year old students. With a board-based design, competitive and time sensitive scoring system, and multiplayer dimension, players will be incentivised to challenge increasingly complex problems, as they progress across the board, to benefit their growth. Instructors will have the option to monitor students' learning achievements in real time to provide personalized supports for students. Alterations to the game will also be conveniently processed through a debug feature, available to future developers/maintainers. Through this game, students will develop fundamentals critical to success in an increasingly dynamic society.


## Required Libraries and Third Party Tools 
A list of the required libraries and third party tools required to run or build your software (include version numbers).

Ensure there is a working version of Python installed, with the earliest supported version for this game being Python 3.9

Navigate to the GROUP69 directory holding requirements.txt, then run pip install -r requirements.txt

If this results in an error, you can manually install the modules inside requirements.txt by running pip install [module]

If an error about unittesting pops up, please see this link. In almost all cases, it is included with an installation of Python 3.9 or higher
https://stackoverflow.com/questions/46133254/unittest-installation-error-could-not-find-a-version-that-satisfies-the-requirem


Installing MongoDB on Windows
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
Follow the instructions for a complete setup type after installing the wizard. Ensure that it is also installing MongoDB Compass.

IF MONGODB IS NOT INSTALLED, THE GAME WILL STILL FUNCTION BUT MANY FEATURES SUCH AS HIGH SCORES, DEV MODE, PLAYER INFORMATION AND SAVE FILES WILL NOT WORK.


## Step by Step Guide for Building the Software 
A detailed step by step guide for building your software (compiling it from source code). This should include details on how to obtain and install any third party libraries.

Running the software will automatically compile all necessary files, see the instructions below for the command and instructions to do so.

See above section for all specifications for the required libraries and third party tools.


## Step by Step Guide for Running the Software 
To run the software, navigate to the Board folder in terminal and run the following command:

```bash
python main_menu_2.py
```

Or from the Board folder in terminal, run the main_menu_2.exe


## User Guide 
1. The first screen displayed is the "Main Menu" Screen where user has a variety of options to navigate to; start game, quit game, go to a tutorial session, display high scores, resume a session
2. If user chooses "Tutorial", they will be navigated to a screen explaining the steps on how to play the game 
3. If user chooses "Load Save", they will be able to play a previous most recently saved session 
4. If user chooses " High Scores", the screen will display the high scores table 
5. If the user chooses "Quit", the application will simply terminate 
6. If the user chooses "Start", the user will be put into a new game 
7. The user will be asked questions and they have to answer it under a certain time limit 
8. There are 3 rows in each level; first row is basic math (addition and subtraction), second row is secondary math (multiplication and division), and third is intermediate math (integrals and quadratics)
9. The questions will be math based and the complexity of the questions increase by level 
10. Once all players are done answering the question/ the timer has run out, the software will provide a feedback screend displaying who got it correct 

To access Developer tools, from the main menu click on Developer Login. Input a password and if it is correct, users will be able to view player details, manipulate game elements as they would like, and change player attributes like scoring



## Account details 
In order to access Developer tools, you will need to input a 1234 in the password field.

To start a game, you will need to give each player a name and a password. 

## How to Access Instructor Mode 
Follow the same steps as accessing Developer tools.

## Additional Information
To access documentation, open the Documentation folder in file explorer and open the html files in your webpage