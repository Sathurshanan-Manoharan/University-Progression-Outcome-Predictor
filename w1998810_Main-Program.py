# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1998810
# Date: 12/04/2023

from w1998810_Modules import * #importing the module

#function to get the user's preffered option
def userChoice ():
    systemName = "University Progression Outcome Calculator"
    nameDesign = "-----------------------------------------"
    print(systemName.center(100))
    print(nameDesign.center(100))
    
    print("\n\t 1. Student \n \t 2. Teacher")
    while True:
        options = ["1","2"] 
        c = input("\nChoose an option : ")
        if c in options:
            break
        else:
            print("\nPlease select an option mentioned above!")
            continue

    if (c == '1') :
        studentVersion()
    else:
        staffVersion()

#function to ask the user whether he wants to conitnue or not
def multipleOutcomes():
    while True:
        userPrefer = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results : ")
        if (userPrefer == 'y') :
            staffVersion()
        elif (userPrefer == 'q') :
            break
        else:
            print ("\nPlease select an option mentioned above!")
            continue

#function to ask the student whether he wants to exit or renter credits
def studVersionRepeat():
    while True:
        print("\nDo you want exit or re-enter your credits?")
        choice = input("Enter 'e' to exit or 'r' to re-enter credits : ")
        opt = ['e','r']
        if choice in opt:
            break
        else:
            print("\nPlease select an option mentioned above!")
    
    if (choice == 'r'):
        studentVersion()
    else:
        exit()

#function for the student version
def studentVersion():
    userInput()
    resultsOutcome()
    studVersionRepeat()

#function to run the staff version
def staffVersion():
    userInput()
    resultsOutcome()
    multipleOutcomes()
    histogram()
    extendedList()
    textFile()
    exit()
        


userChoice()
