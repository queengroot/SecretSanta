def main ():

    #Title of program
    print()
    print("     Secret Santa Program")
    print("     *******************")
    print()

    #declare variables
    import random
    names = ["Donna", "Aunt Jana", "Uncle Lee", "Randy", "Lori", "Phil", "Cindy", "Steve", "Dylan", "Liz", "Rachael", "Joe", "Kate", "Autumn", "Robyn", "Harley", "Ronnie", "Mary", "Matt", "Ryan", "Ethan"]
    counter = 0
    nameOne = ""
    nameOneP = 0
    nameTwo = 0
    nameTwoP = 0
    nameThree = 0
    nameThreeP = 0
    nameFour = 0
    nameFourP = 0
    nameFive = 0
    nameFiveP = 0
    nameSix = 0
    nameSixP = 0
    nameSeven = 0
    nameSevenP = 0
    nameEight = 0
    nameEightP = 0
    nameNine = 0
    nameNineP = 0
    nameTen = 0
    nameTenP = 0
    nameEleven = 0
    nameElevenP = 0
    nameTwelve = 0
    nameTwelveP = 0
    nameThirteen = 0
    nameThirteenP = 0
    nameFourteen = 0
    nameFourteenP = 0
    nameFifteen = 0
    nameFifteenP = 0
    nameSixteen = 0
    nameSixteenP = 0
    nameSeventeen = 0
    nameSeventeenP = 0
    nameEighteen = 0
    nameEighteenP = 0
    nameNineteen = 0
    nameNineteenP = 0
    nameTwenty = 0
    nameTwentyP = 0
    
    nameTwentyOne = 0
    
    while counter < 21:
        
        nameOne = random.choice(names)
        while nameOne == "Donna" or nameOne == "Randy":
            
            nameOne = random.choice(names)
           
      
        nameOneP = nameOne
        names.remove(nameOne)
        counter+=1
        
        nameTwo = random.choice(names)
        while nameTwo == "Aunt Jana" or nameTwo == "Cindy":
            
            nameTwo = random.choice(names)
           
        
        nameTwoP = nameTwo
        names.remove(nameTwo)
        counter+=1

        nameThree = random.choice(names)
        while nameThree == "Uncle Lee" or nameThree == "Dylan":
            nameThree = random.choice(names)
           
        
        nameThreeP = nameThree
        names.remove(nameThree)
        counter+=1

        #additions
        nameFour = random.choice(names)
        while nameFour == "Randy" or  nameFour =="Kate":
            nameFour = random.choice(names)
            

        
        nameFourP = nameFour
        names.remove(nameFour)
        counter+=1

        nameFive = random.choice(names)
        while nameFive == "Lori" or nameFive == "Rachael":
            nameFive = random.choice(names)
            
        
        nameFiveP = nameFive
        names.remove(nameFive)
        counter+=1

        nameSix = random.choice(names)
        while nameSix == "Phil" or nameSix == "Aunt Jana":
            nameSix = random.choice(names)
           
        
        nameSixP = nameSix
        names.remove(nameSix)
        counter+=1

        nameSeven = random.choice(names)
        while nameSeven == "Cindy" or  nameSeven == "Joe":
            nameSeven = random.choice(names)
           
        
        nameSevenP = nameSeven
        names.remove(nameSeven)
        counter+=1

        nameEight = random.choice(names)
        while nameEight == "Steve" or nameEight == "Uncle Lee":
            nameEight = random.choice(names)
            
        
        nameEightP = nameEight
        names.remove(nameEight)
        counter+=1

        nameNine = random.choice(names)
        while nameNine == "Dylan" or  nameNine == "Mary" or nameNine == "Liz":
            nameNine = random.choice(names)
           
        
        nameNineP = nameNine
        names.remove(nameNine)
        counter+=1

        nameTen = random.choice(names)
        while nameTen == "Liz" or  nameTen == "Phil" or nameTen == "Dylan":
            nameTen = random.choice(names)
           
        
        nameTenP = nameTen
        names.remove(nameTen)
        counter+=1

        nameEleven = random.choice(names)
        while nameEleven == "Rachael" or  nameEleven == "Liz":
            nameEleven = random.choice(names)
            
        
        nameElevenP = nameEleven
        names.remove(nameEleven)
        counter+=1

        nameTwelve = random.choice(names)
        while nameTwelve == "Joe" or  nameTwelve == "Harley" or nameTwelve == "Kate":
            nameTwelve = random.choice(names)
            
        
        nameTwelveP = nameTwelve
        names.remove(nameTwelve)
        counter+=1

        nameThirteen = random.choice(names)
        while nameThirteen == "Kate" or  nameThirteen == "Uncle Steve" or nameThirteen == "Joe":
            nameThirteen = random.choice(names)
            
        
        nameThirteenP = nameThirteen
        names.remove(nameThirteen)
        counter+=1

        nameFourteen = random.choice(names)
        while nameFourteen == "Autumn" or nameFourteen == "Lori":
            nameFourteen = random.choice(names)
            
        
        nameFourteenP = nameFourteen
        names.remove(nameFourteen)
        counter+=1

        nameFifteen = random.choice(names)
        while nameFifteen == "Robyn" or nameFifteen == "Donna":
            nameFifteen = random.choice(names)
            
        
        nameFifteenP = nameFifteen
        names.remove(nameFifteen)
        counter+=1

        nameSixteen = random.choice(names)
        while nameSixteen == "Harley" or nameSixteen == "Autumn":
            nameSixteen = random.choice(names)
            
        
        nameSixteenP = nameSixteen
        names.remove(nameSixteen)
        counter+=1

        nameSeventeen = random.choice(names)
        while nameSeventeen == "Ronnie" or nameSeventeen == "Robyn":
            nameSeventeen = random.choice(names)
            
        
        nameSeventeenP = nameSeventeen
        names.remove(nameSeventeen)
        counter+=1

        nameEighteen = random.choice(names)
        while nameEighteen == "Mary" or nameEighteen == "Ronnie":
            nameEighteen = random.choice(names)
            
        
        nameEighteenP = nameEighteen
        names.remove(nameEighteen)
        counter+=1

        nameNineteen = random.choice(names)
        while nameNineteen == "Matt":
            nameNineteen = random.choice(names)
            
        
        nameNineteenP = nameNineteen
        names.remove(nameNineteen)
        counter+=1

        nameTwenty = random.choice(names)
        while nameTwenty == "Ryan":
            nameTwenty = random.choice(names)
            
        
        nameTwentyP = nameTwenty
        names.remove(nameTwenty)
        counter+=1
        
        
       
        #if the last name left is Audrey, the names removed will be
        #appended and the program will start from the beginning
        nameTwentyOne = names[0]
        
        if nameEighteen != "Ethan":
            print("     Donna will be giving a gift to "  + nameOneP)
            print("     Aunt Jana will be giving a gift to "  + nameTwoP) 
            print("     Uncle Lee will be giving a gift to "  + nameThreeP)
            print("     Randy will be giving a gift to "  + nameFourP)
            print("     Lori will be giving a gift to "  + nameFiveP)
            print("     Phil will be giving a gift to "  + nameSixP)
            print("     Cindy will be giving a gift to "  + nameSevenP)
            print("     Steve will be giving a gift to "  + nameEightP)
            print("     Dylan will be giving a gift to "  + nameNineP)
            print("     Liz will be giving a gift to "  + nameTenP)
            print("     Rachael will be giving a gift to "  + nameElevenP)
            print("     Joe will be giving a gift to "  + nameTwelveP)
            print("     Kate will be giving a gift to "  + nameThirteenP)
            print("     Autumn will be giving a gift to "  + nameFourteenP)
            print("     Robyn will be giving a gift to "  + nameFifteenP)
            print("     Harley will be giving a gift to "  + nameSixteenP)
            print("     Ronnie will be giving a gift to "  + nameSeventeenP)
            print("     Mary will be giving a gift to " + nameEighteenP)
            print("     Matt will be giving a gift to " + nameNineteenP)
            print("     Ryan will be giving a gift to " + nameTwentyP)
            print("     Ethan will be giving a gift to " + nameTwentyOne)
            
            counter+=1
            
        else:
            names.append(nameOneP)
            names.append(nameTwoP)
            names.append(nameThreeP)
            names.append(nameFourP)
            names.append(nameFiveP)
            names.append(nameSixP)
            names.append(nameSevenP)
            names.append(nameEightP)
            names.append(nameNineP)
            names.append(nameTenP)
            names.append(nameElevenP)
            names.append(nameTwelveP)
            names.append(nameThirteenP)
            names.append(nameFourteenP)
            names.append(nameFifteenP)
            names.append(nameSixteenP)
            names.append(nameSeventeenP)
            counter = 0

            
    print()
    print("     *******************")
    print("     Happy Holidays 2020")
    input()
    
    
main()
