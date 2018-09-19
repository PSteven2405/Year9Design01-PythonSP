import os

#We use the input function to take an input
#We have to have an assignement statement to store an input

fName = input("What is your first name?") 


print("hi,"+fName)

fLName = input("What is your last name?")

initialName = fName[0] + "." +fLName[0] #adding strings is concatination

print("Hi,"+initialName)

fAge = input("What is your age?")

print("Age"+fAge)

os.system("Say "+fName+" "+fLName)

