def start():                                                                #ask the user if he want to play or not
    global gchoice_1                                                          #if the input is improper ask him to input again
    print("This is the guessing game of 4-digit numbers. ")
    print("Please choose a 4-digit secret number with no repeated digits. ")
    print("Please press 'X' if you want to end the program.")
    while True:
        gchoice_1 = input("Do you want to play the game or not N/Y: ")
        if gchoice_1 == "Y" or gchoice_1 == "N":
            break
        else:
            print("Please enter 'N' or 'Y' ")
    return gchoice_1

def preparation():                                                         #make a list with all 4-digit numbers which have no repeated digits
    global glst
    global glst_prepare
    global ghistory
    glst = []
    glst_prepare = []
    for i in range (1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        number = str(i) + str(j) + str(k) + str(l)
                        glst.append(number)
    for i in range (1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        number = str(i) + str(j) + str(k) + str(l)
                        glst_prepare.append(number)
    ghistory = []
    return glst, glst_prepare

def run():                                                            #ask the user to input the correct and exact numbers
    global ghistory
    global gcorrect
    global gexact
    global ginitial_number
    ginitial_number = glst_prepare[0]
    recover = []
    judge = None
    gexact = None
    print("Guess ", gcnt, "/40 : ", ginitial_number)
    while True:
        gcorrect = input("How many correct digits?")
        if gcorrect.isdigit():                                       #check if the input of correct and exact numbers are proper or not
            gcorrect = int(gcorrect)
            if gcorrect == 0:                                        #if correct is 0 skip the step of input exact number                       
                gexact = 0                                           #and remove the numbers in list which don't satisfy the description given by user
                recover = []
                for i in glst:                                        
                    exact_real = 0                                    
                    correct_real = 0
                    number_to_contrast = []
                    initialNumber_to_contrast = []
                    for j in range(0, 4):
                        number_to_contrast.append(i[j])
                        initialNumber_to_contrast.append(ginitial_number[j])
                    for m in range(0, 4):
                        if number_to_contrast[m] == initialNumber_to_contrast[m]:
                            exact_real = exact_real + 1
                        else:
                            pass
                    for a in range(0, 4):
                        for b in range(0, 4):
                            if number_to_contrast[a] == initialNumber_to_contrast[b]:
                                correct_real = correct_real + 1
                                break
                            else:
                                pass
                    if exact_real != gexact or correct_real != gcorrect:
                        try:
                            glst_prepare.remove(i)
                            recover.append(i)                                          #if the number does not satisfied with the description of player remove it
                        except:
                            pass
                    else:
                        pass
                if glst_prepare == []:                                                          #check if the input numbers are inconsistent response
                    for c in recover:
                        glst_prepare.append(c)
                    print("Inconsistent response")
                    print("")
                else:
                    break
            elif gcorrect > 4:                                                         #check if the correct number is improper
                print("The number should no more than 4")
                print("")
            elif gcorrect < 0:
                print("The number should be no less than 0")
                print("")
            else:                                                                      #if the input is proper
                while True: 
                    recover = []                                                           #remove the numbers in list which don't satisfy the description given by user
                    gexact = input("How many exact digits?")
                    if gexact.isdigit():
                        gexact = int(gexact)
                        if gexact > gcorrect:
                            print("Exact digits should be no more than ", gcorrect)
                            print("")
                        elif gexact < 0:
                            print("Exact digits should be no less than 0")
                            print("")
                        else:
                            for i in glst:
                                exact_real = 0
                                correct_real = 0
                                number_to_contrast = []
                                initialNumber_to_contrast = []
                                for j in range(0, 4):
                                    number_to_contrast.append(i[j])
                                    initialNumber_to_contrast.append(ginitial_number[j])
                                for m in range(0, 4):
                                    if number_to_contrast[m] == initialNumber_to_contrast[m]:
                                        exact_real = exact_real+1
                                    else:
                                        pass
                                for a in range(0,4):
                                    for b in range(0,4):
                                        if number_to_contrast[a] == initialNumber_to_contrast[b]:
                                            correct_real = correct_real + 1
                                            break
                                        else:
                                            pass
                                if exact_real != gexact or correct_real != gcorrect:
                                    try:
                                        glst_prepare.remove(i)
                                        recover.append(i)
                                    except:
                                        pass
                                else:
                                    pass
                            if glst_prepare == []:                                           #check if it is inconsistent responce
                                print("Inconsistent response")
                                print("")
                                for c in recover:
                                    glst_prepare.append(c)
                            else:
                                judge="correct number"
                            break
                    elif gexact == "X":
                        print("The game is over")
                        break
                    else:
                        print("It must be a positive integer")
                        print("")
        elif gcorrect == "X":
            print("The game is over")
            break
        else:                                                                        #save result in a history list
            print("It must be a positive integer")
            print("")
        if judge == "correct number"  or gexact == "X" or gcorrect == "X":
            break
        else:
            pass
    history = ["Guess ", gcnt, "/40 : ", ginitial_number[0], "correct : ", gcorrect, "exact : ", gexact]
    ghistory.append(history)
    return glst_prepare, gexact, gcorrect

def main():                                                                          
    global gchoice
    global gcnt 
    start()
    print("")
    if gchoice_1 == "Y":
        preparation()
        gcnt=1
        while True:
            run()
            print("")
            if gexact == 4 and gcorrect == 4:
                while True:                                    #if player succeed ask him if he want another game
                    gchoice=input("Congratulations!!Start a new game (y/n)?")
                    if gchoice == 'n' or gchoice == 'y':
                        break
                    else:
                        print("Please enter 'n' or 'y' ")
                break
            elif gcorrect == "X" or gexact == "X":
                while True:
                    gchoice=input("Start a new game (y/n)?")
                    if gchoice == 'n' or gchoice == 'y':
                        break
                    else:
                        print("Please enter 'n' or 'y' ")
                break
            elif gcnt == 40:
                while True:                                                      #if player failed ask him if he want another game
                    gchoice = input("Game Over!!Exceeded ax. attempts!Start a new game(y/n)?")
                    if gchoice == 'n' or gchoice == 'y':
                        break
                    else:
                        print("Please enter 'n' or 'y' ")                        #ask him to enter again if the input is improper
                break
            gcnt = gcnt+1
            for i in ghistory:
                for j in i:
                    print(j,end=" ")
                print(end="\n")                                                  #print the history
    else:
        print("The game is over")
    
def loop():
    while True:
        main()
        if gchoice_1 == "N":                                                           #if he want to play start the game
            break                                                                   #if he does not want to play stop the program
        if gchoice_1 == "Y":
            if gchoice == 'n':  
                print("The game is over")                                                    #if he does not want to play again stop the program
                break

loop()

     