# print("Hello World")
# print("What's up?")

# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")

# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)

# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16

# print(23%4) #3

# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)

# print("Hello" + str(4))
# print(int("4"))

#inputs
# firstName = "Lisette"
# lastName = input("What is your last name?\n")
# print("Welcome " +  firstName.capitalize() + lastName.capitalize())

# age=input("How old are you?\n")
# age = int(age)+3
# print("In three years, you will be " + str(age))

# age = int(input("Please enter your age: "))
# if age >= 18: 
#     print("You are able to vote in the United States!")
# else:
#     print("You are not able to vote in the United States.")

        

#Control Flow
# while True:
#     try:
#         number = int(input("What's your favorite number?\n"))
#     except ValueError:
#         print("Sorry, it is not a valid number")
#         continue
#     if number%2 == 0:
#         print("Your number is even!\n")
#         exit
#     else:
#         print("Your number is odd!\n")
#         exit
   
   
# #For Loops
# favAnimal = "Ostriches"
# print(favAnimal[4])
# print("The first letter is " + favAnimal[0])
# print("The second letter is " + favAnimal[1])
# print("The third letter is " + favAnimal[2])
        
# for i in range(0,len(favAnimal)):
#     if str(i) == 0:
 
# numBottles = int(input("How many bottles of milk are on the wall?\n"))
# for i in range(numBottles, 0, -1):
#     if (i!=1):
#         print(str(i) + "bottles of milk on the wall!\n")
#     else:
#         print(str(i) + "bottle of milk on the wall!\n")

# import random 
# print("We're gonna play a game! Let's roll the first dice!")
# reachedGoal = False
# count = 0
# while(reachedGoal):
#     firstRoll = random.randint(1,7)
#     secondRoll = random.randint(1,7)
#     print("You rolled a\n" + str())
        
#Functions# Define the function!
def personalized_age_check(name, age):
  if age >= 18:
    return "Congratulations " + name + "! You're old enough to vote."
  else:
    time_left = 18 - age
    return "Sorry, " + name + ". You can't vote for another " + str(time_left) + " years."

# Call the function
print(personalized_age_check("Jeff", 28))
print(personalized_age_check("Zara", 14))
