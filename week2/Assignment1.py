#Assignment for Week 2

#Assingment I: Objects
""" print ("Assingment I: An Array of My Objects")
print ("\n")

myObjects = [
	{
	"objectType" : "Extension Cord", 
	"color" : "Turquoise and red",
	"shape" : "Square with round cable",
	"function" : "Plugging in cables",
	"material" : "Metal, fabric and Plastic"
	},

	{
	"objectType" : "Guitar", 
	"color" : "Light wood",
	"shape" : "Curvy with a handle",
	"function" : "Making music",
	"material" : "Wood and metal strings"
	},

	{
	"objectType" : "Hammock and stand", 
	"color" : "Red and black",
	"shape" : "Stretched U shape",
	"function" : "Sitting, rocking, relaxing",
	"material" : "Fabric hammock and steel stand"
	},

	{
	"objectType" : "Dog bowl", 
	"color" : "Red and white",
	"shape" : "Cylindrical",
	"function" : "Holding food or water",
	"material" : "Ceramic"
	},
]

print (myObjects[0])
print ("\n")
print (myObjects[1])
print ("\n")
print (myObjects[2])
print ("\n")
print (myObjects[3])
"""

#Assingment III: Story
#Assingment III: Story
print ("\n")
print ("Hello!")
name1 = raw_input("What is your name?" + "\n")
print ("Nice to meet you, " + name1 + "\n")
answer1 = raw_input("Would you like to find out your stripper name? (yes or no) \n")

def myStory():

	print ("Welcome to MadLibs, " + stripperName + "\n")
	print ("To play, you must answer the questions below.")
	print ("---------------------------------------------")
	print ("\n")

	location1 = raw_input("Enter a place (For example, beach):\n")
	animal1 = raw_input("What is your favorite animal?: \n")
	food1 = raw_input("What is your favorite food?: \n")
	profession1 = raw_input("Enter a profession: \n")
	city1 = raw_input("Enter your favorite city: \n")
	adjective1 = raw_input("Enter an adjective: \n")


	print("Once upon a time, deep in an ancient " + location1 + ", there lived a " + animal1 +  "." + "\n" + "This " + animal1 +
	" liked to eat " + food1 +", but the jungle had very little " + food1 + " to offer." + "\n" + "One day, a " + profession1 + 
	" found the " + animal1 + " and discovered it liked "  + food1 + "." + "\n" + "The " + profession1 + " took the " + animal1 + 
	" back to " + city1 + ", where it could eat as much " + food1 + " as it wanted." + "\n" + "However, the " + animal1 + " became " 
	+ adjective1 +", so the " + profession1 + " brought it back to the " + location1 + ", leaving a large supply of " + food1 + ".")


	return 

if answer1 == "yes":
	print ("Excellent!")
	firstName = raw_input("What is the name of your first pet? \n")
	lastName = raw_input("What is the name of the first street you lived on? \n")
	stripperName = firstName + " " + lastName + "\n"
	print ("Your stripper name is: " + stripperName + "\n")
	print ("Hahahaha! Anyway... \n")
	myStory()
	






