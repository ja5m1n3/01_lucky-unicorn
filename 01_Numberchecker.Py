# Funtions gp here

# Main routine goes here 

error = "Please emter a whole number between 1 and 10"

valid = False
while not valid:
    
    # Ask the question
    response = int(input("How much would you " "like to play with"))
    
    # if the amount is too low / too high give
    if 0 < response <= 10:
        pass
print("You have asked to play")