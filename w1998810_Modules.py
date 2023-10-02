# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1998810
# Date: 12/04/2023

#Creating variables 
creditsPass = 0 #variable created to store pass credits
creditsDefer = 0 #variable created to store defer credits
creditsFail = 0 #variable created to store fail credits
progress = 0 #variable created to get the count of progress
exclude = 0 #variable created to get the count of exclude
moduleTrailer = 0 #variable created to get the count of moduletrailer
moduleRetriever = 0 ##variable created to get the count of moduleretriever
totalOutcomes = 0 #variable created to add pass, defer fail
outcomeList = [] #list created to store the outcomes

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
            break

#function to check the progression     
def resultsOutcome():
    global creditsPass, creditsDefer, creditsFail, progress, exclude, moduleRetriever, moduleTrailer
    if creditsPass == 120 :
        print ("\nProgression Outcome : Progress")
        progress += 1
        outcomeList.append(["Progress - ", creditsPass, creditsDefer, creditsFail])

    elif creditsPass == 100 :
        print("\nProgression Outcome : Progress (module trailer)")
        moduleTrailer += 1
        outcomeList.append(["Progress (module trailer) - ", creditsPass, creditsDefer, creditsFail])
    
    elif creditsPass == 40 and creditsDefer == 0 :
        print ("\nProgression Outcome - Exclude")
        exclude += 1
        outcomeList.append(["Exclude : ", creditsPass, creditsDefer, creditsFail])

    elif creditsPass == 20 and creditsDefer <= 20 :
        print ("\nProgression Outcome : Exclude")
        exclude += 1
        outcomeList.append(["Exclude - ", creditsPass, creditsDefer, creditsFail])

    elif creditsPass == 0 and creditsDefer <= 40 :
        print ("\nProgression Outcome : Exclude")
        exclude += 1
        outcomeList.append(["Exclude - ", creditsPass, creditsDefer, creditsFail])
    
    else:
        print("\nProgression Outcome : Do not progress – module retriever")
        moduleRetriever += 1
        outcomeList.append(["Module retriever - ", creditsPass, creditsDefer, creditsFail])

#function to create the histogram
def histogram():
    global progress, exclude, moduleRetriever, moduleTrailer, totalOutcomes
    print ("\n","_" * 60, "\n" )
    print ("Histogram \n")
    print("Progress",progress,"\t:","*" * progress)
    print("Trailer",moduleTrailer,"\t:","*" * moduleTrailer)
    print("Retriever",moduleRetriever,"\t:","*" * moduleRetriever)
    print("Excluded",exclude,"\t:","*" * exclude )

    totalOutcomes = (progress + exclude + moduleRetriever + moduleTrailer)
    print(totalOutcomes,"outcomes in total.")
    print ("\n","_" * 60, "\n" )

#function to get the extended list 
def extendedList():
    global outcomeList
    print("Part 2 - List (extension) \n")
    for outcome in outcomeList:
        print (*outcome)

#function to get the text file
def textFile(): #Reference www.w3schools.com 
    global outcomeList, file 
    print("\nPart 3 - Text File (extension) \n")
    file = open("Progression_Outcome.txt", "w")
    for outcome in outcomeList:
        file.write(str(outcome[0]) + str(outcome[1]) + str(" ") + str(outcome[2]) + str(" ") + str(outcome[3]) + str("\n"))
    file.close()

    file = open("Progression_Outcome.txt", "r")
    print(file.read())