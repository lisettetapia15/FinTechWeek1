school = ["locker" , "classroom"]
print (school)
print("You are the Class President of your school and you misplaced your bag after many meetings. Your job is to find your bag before the school closes!")
choice = input("Your beginning location is the School. You have the choice of looking at your locker or the classroom your meetings were in. Which one? \n")
choice = choice.lower()

if choice == "locker":
    locker = ["textbook", "gym clothes"]
    print("These are the items in your  " + str(choice) + str(locker))
    lockerChoice = input("You can check under the textbook or under the gym clothes. Which one? \n")
    lockerChoice = lockerChoice.lower()
    if lockerChoice == "textbook":
        print("You looked under your textbook but there was nothing! Try again!")
    elif lockerChoice == "gym clothes":
        print("Your gym clothes did not cover your bag! Try again!")
elif choice == "classroom":
    classroom = ["desk", "window sill"]
    print("These are the places where you usually place your bag down in the " + str(choice) + str(classroom))
    classroomChoice = input("Where would you like to look? \n")
    classroomChoice = classroomChoice.lower()
    if classroomChoice == "desk":
        print("Sorry, there was nothing on your desk! Try again!")
    elif classroomChoice == "window sill":
        print("You found your bag! Congrats!")
        
    