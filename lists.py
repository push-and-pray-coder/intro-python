"""
Lists are used to store MULTIPLE items in a single variable.
Think of them like a "BOX" that can hold many items at once
Lists are created with squared brackets []
"""

my_list = [10, 20, 30, 40, 50]
print (my_list)

# Mixed List
mixed_list = [1, "apple", 3.5, True]
print (mixed_list)

#Accessing items by INDEX
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

#you can also use a NEGATIVE index to count in reverse
print(fruits[-1]) #prints cherry

# SLICING in a list
# Slicing lets you grab a RANGE of items using [start:stop]
# it includes "start" but stops BEFORE "stop"

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(numbers[2:5])
print(numbers[:4])
print(numbers[6:])
print(numbers[-3:])
print(numbers[::2]) # START:STOP:STEP

#Moodifying list items
fruits[1] = "mango"
print(fruits)

#Adding items
fruits.append("orange") # Adds One item to the END of list
print(fruits)

fruits.insert(1, "kiwi") # adds at specific position (before index 1)
print(fruits)

fruits.extend (["grape","pear"])  # adds multiple items to the end of the list

print (fruits)

# removing items
fruits.remove("apple") #removes by value
print(fruits)

fruits.pop(3) #remove last item from last, or by index if supplied

#fruits.clear() clears entire list

print(fruits)

for fruit in fruits:
    print(fruit)

# CHECK if item exists
if "mango" in fruits:
    print("mango is in the list")

# List Length
print(len(fruits)) # Number if items in list

groceries = ["chocolate", "bread", "cookies", "meat", "veges"]
print(groceries[0], (groceries[-1]))
print(groceries[0:3])
groceries.append("eggs")
groceries.insert(0, "milk")
groceries.remove("veges")
if "bread" in groceries:
    print("There be bread")
print(len(groceries))
