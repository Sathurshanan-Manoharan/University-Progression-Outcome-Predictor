# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1998810
# Date: 15/04/2023

#Creating variables 
creditsPass = 0 #variable created to store pass credits
creditsDefer = 0 #variable created to store defer credits
creditsFail = 0 #variable created to store fail credits
studentId = 0 #variable created to store the entered student ID
studentDict = {} #Dictionary created
studentIdList = [] #list creaed to store studnt IDs
outcome = [] 


#function to get the credits from the user and validate 
def userInput ():
    global creditsPass, creditsDefer, creditsFail
    while True:
        try: #To check wether the input is an integer 
            creditsPass = int(input("\nPlease enter your credits at pass : "))
        except ValueError:
            print("Integer required!")
            continue
        if creditsPass not in range (0,121,20): #checking the range 
            print("Out of range!")
            continue

        try: #To check wether the input is an integer 
            creditsDefer = int(input("\nPlease enter your credit at defer : "))
        except ValueError:
            print("Integer required!")
            continue
        if creditsDefer not in range (0,121,20): #checking the range 
            print("Out of range!")
            continue

        try: #To check wether the input is an integer 
            creditsFail = int(input("\nPlease enter your credit at fail : "))
        except ValueError:
            print("Integer required!")
            continue
        if creditsFail not in range (0,121,20): #checking the range 
            print("Out of range!")
            continue

        if creditsPass + creditsDefer + creditsFail != 120 : #Adding the credits and checking the total
            print ("\nTotal incorrect!")
        else:
            return resultsOutcome()

#function to check the progression       
def resultsOutcome():
    global creditsPass, creditsDefer, creditsFail, studentDict, studentId
    if creditsPass == 120 :
        print ("\nProgression Outcome : Progress")
        progress = ["Progress - ", creditsPass, creditsDefer, creditsFail]
        studentDict[studentId] = progress #updating the dictionary  #Reference www.w3schools.com 

    elif creditsPass == 100 :
        print("\nProgression Outcome : Progress (module trailer)")
        moduleTrailer = ["Progress (module trailer) - ", creditsPass, creditsDefer, creditsFail]
        studentDict[studentId] = moduleTrailer #updating the dictionary
    
    elif creditsPass == 40 and creditsDefer == 0 :
        print ("\nProgression Outcome - Exclude")
        exclude = ["Exclude - ", creditsPass, creditsDefer, creditsFail]
        studentDict[studentId] = exclude #updating the dictionary

    elif creditsPass == 20 and creditsDefer <= 20 :
        print ("\nProgression Outcome : Exclude")
        exclude = ["Exclude - ", creditsPass, creditsDefer, creditsFail]
        studentDict[studentId] = exclude #updating the dictionary

    elif creditsPass == 0 and creditsDefer <= 40 :
        print ("\nProgression Outcome : Exclude")
        exclude = ["Exclude - ", creditsPass, creditsDefer, creditsFail]
        studentDict[studentId] = exclude #updating the dictionary
    
    else:
        print("\nProgression Outcome : Do not progress – module retriever")
        retriever = ["Do not progress – module retriever - ",creditsPass, creditsDefer, creditsFail]
        studentDict[studentId] = retriever #updating the dictionary
        
    multipleOutcomes()

#function to ask the user for the student ID   
def stuId():
    global studentId, studentDict, outcomeList, studentIdList, idChoice
    while True :
        studentId = input("\nEnter the student ID : ")
        if studentId == "":
            print("\nInvalid ID! please add your ID agaian\n")
            continue
        elif studentId not in studentIdList :
            studentIdList.append(studentId)
            userInput()
        else:
            print("\nStudent ID already entered! \nPlease enter another student ID\n")
            continue

#function to ask the user whether he wants to conitnue or not        
def multipleOutcomes():
    global studentDict, studentIdList
    while True:
        userPrefer = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results : ")
        if (userPrefer == 'y') :
            stuId()
        elif (userPrefer == 'q') :
            print(*[str(k) + ':' + str(v) for k,v in studentDict.items()]) #printing the dictionary
            exit()
        else:
            print ("\nPlease select an option mentioned above!")
            continue

print("Part 4 - Dictionary (separate program)")
stuId()

