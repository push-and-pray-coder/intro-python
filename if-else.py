"""
An if-else statement in Python is a conditional control structure that lets
you decide which block of code to run depending on wheather a condition
is True or False

if condition:
|   -Code block runs if condition is True
elif another_condition:
|   -Code block runs if first condition is False
|   -and this condition is True
else:
|   -Code block runs if none of the above conditions are True

if - checks a condition
elif (else if) - checks another condition
else -runs if all other conditions are False
"""

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short hand If statements
# you can write it all in one line

if x > 5: print ("x is greater than 5")

#Short hand if...else
print("even") if x % 2 == 0 else print("odd")

x = 21

# Nested if statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining conditions

age = 22

if age >= 18 and age <= 21:
    print ("You are between 18 and 21 years old")

"""
MINI CHALLENGE
1. Ask the user to enter their age and store it in a variable called age
2. Ask the user if they have a valid ID
3. Determine admission rules:
    If age is 21 or older and has_is is yes:
    print "Access Granted"
    if age is 21 or older but has_id is no:
    print Access denied - ID required
    if age is between 18 and 20 inclusive:
    print Access Limited
    Otherwise
    print Access denied too young
4. Create a variable called can_enter:
    Set it to True only if the user is 21 or older AND has_id is "yes".
    Otherwise set it to False.
5. BONUS:
    If can_enter is True:
    Print "Welcome Inside!"
    Otherwise:
    Print "Please see the front desk."
6. EXTRA BONUS:
    If the user enters a negative age,
    Print "Invalid age entered."
"""
age = int(input("Enter Your Age: "))
has_id = input("Do you have a valid ID? ")
can_enter = False
if  age < 0:
    print ("Invalid age entered")
elif age >= 21: 
    if has_id == "yes":
        print("Access Granted")
        can_enter = True
    elif has_id == "no":
        print("Acces denied ID required")
elif age >= 18 and age <= 20:
    print ("Limited access")
else:
    print ("Access dendied too young")

if can_enter:
    print ("Welcome inside")
else:
    print ("See the front desk")