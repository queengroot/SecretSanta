def main ():

    #Title of program
    print("Gift giving program")
    print("*******************")

    #declare variables
    import random
    names = ["Kate", "Joe", "Keith", "Audrey"]
    counter = 0
    nameOne = 0
    nameOneP = 0
    nameTwo = 0
    nameTwoP = 0
    nameThree = 0
    nameThreeP = 0
    nameFour = 0
    
    while counter < 4:
        
        nameOne = random.choice(names)
        while nameOne == "Kate":
            nameOne = random.choice(names)
        
        nameOneP = nameOne
        names.remove(nameOne)
        counter+=1
        
        nameTwo = random.choice(names)
        while nameTwo == "Joe":
            nameTwo = random.choice(names)
        
        nameTwoP = nameTwo
        names.remove(nameTwo)
        counter+=1

        nameThree = random.choice(names)
        while nameThree == "Keith":
            nameThree = random.choice(names)
        
        nameThreeP = nameThree
        names.remove(nameThree)
        counter+=1

       
        #if the last name left is Audrey, the names removed will be
        #appended and the program will start from the beginning
        nameFour = names[0]
        if nameFour != "Audrey":
            print("Kate will be giving a gift to "  + nameOneP)
            print("Joe will be giving a gift to "  + nameTwoP) 
            print("Keith will be giving a gift to "  + nameThreeP)
            print("Audrey will be giving a gift to " + nameFour)
            counter+=1
        else:
            names.append(nameOneP)
            names.append(nameTwoP)
            names.append(nameThreeP)
            counter = 0   
    print()
    print("*******************")
    print("Happy Holidays!")

    #pause for input so screen doesn't flash by
    input("")
main()
