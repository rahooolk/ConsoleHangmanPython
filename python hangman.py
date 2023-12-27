import random

#Infinite loop to restart the game untill user says no: 
while True:
    #Function 
    def hangman():
        list_of_words = ["nettech", "microsoft", "google", "amazon", "chicken", "shawarma", "vadapav", "keyboard", "rocket", "pigeon", "monkey"]
        word = random.choice(list_of_words)
        turns = 10
        guessmade = ""
        valid_entry = set("abcdefghijklmnopqrstuvwxyz")


        #Using while loop to check the guessed alphabet is in the word again and again
        while len(word)>0:
            #1)
            main_word = ""   # very imp -- main word resets after every guess

            #lets consider: "nettech"
            for letter in word:              #loping through each alphabet in "nettech"
                if letter in guessmade:            #checking if the alphabet is correctly guessed    
                    main_word = main_word + letter      
                else:
                    main_word = main_word + "_ "       


            #If the word is correctly guessed....user wins
            if main_word == word:
                print("Congrats! You won")
                break

            #after the for loop exhausts for a guess it should again ask the user to guess the word
            print("Guess the words ", main_word)   #this is the mainword that comes out when the for loop exhausts 
            guess = input()                                                                                            

            #Checking if user enters valid entries and only considering those entries in the guessmade string
            #2)
            if guess in valid_entry:
                guessmade = guessmade + guess            #valid entries will be stored in the empty string guessmade
            else:
                print("Enter valid characters! ")
                guess = input()

            print(main_word)

            #If the guess is wrong decreasing the turns and displaying the hangman
            #3)
            if guess not in word:
                turns = turns - 1

                if turns == 9:
                    print("You have 9 turns to guess")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")

                if turns == 8:
                    print("Okay 8 turns now")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")

                if turns == 7:
                    print("Now 7 turns left")
                    print(" |------------")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")

                if turns == 6:
                    print("Only 6 turns left")
                    print(" |____________")
                    print(" |/       |   ")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")


                if turns == 5:
                    print("5 more turns left ")
                    print(" |____________")
                    print(" |/       |   ")
                    print(" |      (☉.☉)")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")


                if turns == 4:
                    print("Only 4 turns left :]")
                    print(" |____________")
                    print(" |/       |   ")
                    print(" |      (☉.☉)")
                    print(" |        |   ")
                    print(" |        |   ")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")


                if turns == 3:
                    print("Only 3 turns left now. Try better!")
                    print(" |____________")
                    print(" |/       |   ")
                    print(" |      (ಠ_ಠ)")
                    print(" |       /|   ")
                    print(" |        |   ")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")


                if turns == 2:
                    print("Only 2 turns left now. Come on!")
                    print(" |____________")
                    print(" |/       |   ")
                    print(" |      (ಠ_ಠ)")
                    print(" |       /|\  ")
                    print(" |        |   ")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")

            
                if turns == 1:
                    print("Last turn left now! Wishing for a miracle")
                    print(" |____________")
                    print(" |/       |   ")
                    print(" |     (꒦ິ﹏꒦ິ) ")
                    print(" |       /|\  ")
                    print(" |       /|\  ")
                    print(" |")
                    print(" |")
                    print(" |")
                    print("_|_____")

                if turns == 0:
                    print("Sorry! You lost")
                    print("Hangman Died! :(")
                    print("     ______")
                    print("    /-----/")
                    print("   / RIP / ")
                    print(" _/_____/__")
                    break   #goes to #1)


    name = input("Enter your name: ")
    print("Welcome", name, ":)")
    print("========================")
    print("The game is to try and guess the word within 10 attempts")
    print("Dont let the man hang!")
    hangman()

    user = input("Do you want to try saving his life again? (y/n) ")
    if user == "n":
        break
