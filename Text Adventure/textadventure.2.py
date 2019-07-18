school = ["locker" , "classroom"]
print (school)
print("You are the Class President of your school and you misplaced your bag after many meetings. Your job is to find your bag before the school closes!")
choice = input("Your beginning location is the School. You have the choice of looking at your locker or the classroom your meetings were in. Which one? \n")
choice = choice.lower()

def playAgain():
    playAgain = input("Would you like to play again? Yes or no?")
    if playAgain.lower() == "yes":
        game()
    elif playAgain.lower() == "no":
        print("Okay! Bye!")
    else:
        print("That isn't a yes or no!")

def game():
    guessTrials = 3
    while guessTrials > 0:
        if choice == "locker":
            locker = ["textbook", "gym clothes"]
            print(locker)
            print("These are the items in your  " + str(choice) + str(locker))
            lockerChoice = input("You can check under the textbook or under the gym clothes. Which one? \n")
            lockerChoice = lockerChoice.lower()
            if lockerChoice == "textbook":
                print("You looked under your textbook but there was nothing! Try again!" + str(guessTrials))
                print(lockerChoice)
            elif lockerChoice == "gym clothes":
                print("Your gym clothes did not cover your bag! Try again!")
                print(lockerChoice)
        elif choice == "classroom":
            classroom = ["desk", "window sill"]
            print("These are the places where you usually place your bag down in the " + str(choice) + str(classroom))
            print(classroom)
            classroomChoice = input("Where would you like to look? \n")
            classroomChoice = classroomChoice.lower()
            if classroomChoice == "desk":
                print("Sorry, there was nothing on your desk! Try again!")
                print(classroomChoice)
            elif classroomChoice == "window sill":
                print("You found your bag! Congrats!")
                print(classroomChoice)
            if guessTrials == 0:
                print("Your bag was in the classroom in the window sill")
            else:
                guessTrials -= 1
                print("You have " + str(guessTrials) + " tries left!")
game()   