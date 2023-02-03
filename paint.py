def paint_calculator(length, width, height): #Takes length, width and height as a parameter 
    wall_area = 2 * (length * height + width * height) #calculates the walls area 
    gallons_needed = wall_area / 350 #Works out how many gallons of paint are needed based off of the assumption that one gallon covers 350 square feet
    return gallons_needed

length = int(input("Enter the length of the room: ")) #Asks the user to enter the rooms length
width = int(input("Enter the width of the room: ")) #Asks the user to enter the rooms width
height = int(input("Enter the height of the room: ")) #Asks the user to enter the rooms height
#The length, width and height are then inputed into the function through the parameters
#Calculates the volume of the room 
volume = length*width*height
area = 4*(length*height)

#Then the total amount of paint is outputted to the user as well as the area and volume of the room
print("The area of the room is: " + str(area))
print("The volume of the room is: " + str(volume)) 
print("You need", paint_calculator(length, width, height), "gallons of paint.")
