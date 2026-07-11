"""
A while loop repeats a block of code as long as a condition is True.
be careful - if the condition never becomes False, you'll get an INFINITE loop!

while condition:
    # Code block runs as long as condition is True
"""

count = 1

while count <= 5:
    print("Count is: ", count) # infinite loop since it never counts to 5
    count += 1 # adds a count of 1 every time it loops

print("---------------------------------------")

number = 0

while True: #infinite loop
    print(number)
    number +=1
    if number ==3:
        break #stops the loop when it reaches 3

# using CONTINUE to SKIP iteration
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # skips 3
    print(count)

#ELSE with while
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop finished!")

"""
Mini Challenge: Password Checker 
1. Ask the user to enter a password
2. Check if it's correct (password: "secret123")
3. If it's wrong, print "Wrong! Try again." and ask again
4. When they enter the correct password, print "Access granted!"
"""

while True:
    password = input("Enter a password: ")
    if password == "secret123":
        print ("Access Granted")
        break
    else:
        print("Wrong Try again")
