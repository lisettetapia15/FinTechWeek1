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