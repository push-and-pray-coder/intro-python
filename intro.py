print("Hello World from Python!")
print (2)
print (5+3)
print(True)

# SHORTCUTS
# ctrl + s  save
# up arrow key in terminal window
#ctrl and +/- to zoom in our out (adjusts the entire vscode UI)

'''
This is a multi line comment
triple quotes around your comment
'''

name = "Fluffy"
age = 1000
print (name, age)

print("My name is " + name + "and I am " + str(age))

"""
Mini Challenge 1
write a story using variables
1. Declare and initialize 5 variables (strings and numbers)
"""

name = "Bob"
location = "office"
hours_worked = 8
job = "clerk"
time_left = 2

print ("Hello my name is " + name + ". I am a " + job + ". I have been at work for " + str(hours_worked) + " hours in the " + location + " and will be off in " + str(time_left) + " hours.")

print(f"""Hello my name is  {name} . I am a  {job} + . I have been at work for  {hours_worked}  
    hours in the  {location}  and will be off in   {time_left}  hours.""")

# TYPE FUNCTIONS
print(type(name))
print(type(age))
print(type(True))


# Casting 
print (20 + int("20"))
print (20+ age)

user_name = int(input("Enter your age: "))
print(f"Hello, {user_name}!")

#Always returns a string
#print(type(input("Enter your age: ")))

# converting input to int
new_age = int(input("Enter your age: "))
print (user_name + new_age)

'''
Pizza Calculator
1. Ask how many slices of pizza and the number of people
2. Use math operators to calculate the slice per person
3. Show the result with an f-string
'''

people = int(input("Enter the number of people: "))
slices = int(input("Enter number of pizza slices: "))
print(f"There are {slices/people} slices per person")