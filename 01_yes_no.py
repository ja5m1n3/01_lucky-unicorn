
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before 
    show_instructions = input ("Have you played this game before? ") .lower()

    # If they day yes, output 'program continues' 
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print ("program continues")

    elif show_instructions ==  "no" or show_instructions == "n":
        print ("display instructions")

    # If they say no, output 'display instructions'
    else :
        print ("Please answer yes / no")

    # print("Display instructions")
        
