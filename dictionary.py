## Dictionaries store data in KEY : VALUE pairs
# writen using curley brackets {}

student = {
    "name": "Leo",
    "age": 24,
    "major": "Computer Science"
}

print(student)

# Accessing items
print(student["name"])  # accessing by key
print(student.get("age"))

# ADDING new items
student["graduation_year"] = 2025
print(student)

# CHANGING Values
student["age"] = 23
print(student)

# REMOVING items
student.pop("major")  # Removes key "major" and its value
print(student)

# CHECKING if key exists
if "name" in student:
    print("Key 'name' exists")

# NESTED dictionaries
students = {
    "student1": {"name": "Leo", "age": 22},
    "student2": {"name": "Alex", "age": 20}
}

print(students["student2"]["name"])  # Access nested value

# LOOPING through a dictionary
# .key()      -> just the keys
# .values()   -> just the values
# .items()    -> key/value pais together

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} : {value}")

student.update({"age" : 25, "gpa" : 3.8})

"""
-------------------------------
MINI CHALLENGE: STUDENT REPORT CARD 
-------------------------------
You need to store and analyze a student's grades.
1. Create a dictionary called "report_card" with keys:
    -"name"
    -"subject"
    -"grades" (use a tuple with 3 numbers)
Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above → print "Excellent!"
If between 70 and 89 → print "Good job!"
Otherwise → print "Needs improvement!"
6. Remove the "subject" key and print the updated dictionary.
"""

report_card = {"name" : "Leo", "subject" : "Math", "grades" : (90,85,88) }
print (report_card["name"], report_card["subject"])
report_card["average"] = sum(report_card["grades"]) / len(report_card["grades"])
print (report_card["average"])
if report_card["average"] >= 90:
    print("Excellent")
elif 70 <= report_card["average"]  < 89:
    print("Good Job!")
else:
    print("Needs improvement")
report_card.pop("subject")
print(report_card)