# Tuples are similar to lists
# BUT! Tuples are IMMUTABLE (you cannot change them after creation)

my_tuple = ("apple", "banana", "cherry")

print(my_tuple)

# ACCESSING ITEM
print(my_tuple[0])
print(my_tuple[-2])

# NESTED TUPLES
tuple1 = ("a" "b", "c")
tuple2 = (1, 2, 3)

combine = (tuple1, tuple2)
print(combine)
print(tuple1,tuple2)

# SINGLE item tuples
# you must add a comma at the end or PYTHON wont recognize it as a tuple
single = ("water",)
print(type(single)) # this is a tuple
not_tuple = ("air")
print(type(not_tuple))

# COUNT and INDEX
letter = ("a", "b", "a", "c", "a")
print(letter.count("a")) # COUNT how many times "a" appears -> 3
print(letter.index("c")) #

# TUPLE UNPACKING
# You can "unpack" a tuple items directly into separate variables

coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)

# TUPLE UNPACKING
# You can "unpack" a tuple items directly into separate variables
coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)

"""
-------------------------------
MINI CHALLENGE: CLASS QUIZ ANALYZER
-------------------------------
You are analyzing quiz scores stored in a tuple.
Create a tuple called "quiz_scores" with at least 6 integer scores.
Print the FIRST 3 scores and the LAST 3 scores using slicing.
Print the HIGHEST and LOWEST score using built-in functions.
Check if ANY score is below 70:
If yes, print "Warning: At least one failing score!"
Otherwise print "All students passed!"
Create a new tuple called "bonus_scores" where each score is increased by 5.
Combine "quiz_scores" and "bonus_scores" into a tuple called "final_scores".
Print the total number of scores in "final_scores".
Print the LAST score in "final_scores".
"""

quiz_scores = (90,100,19,54,38,77)
print (quiz_scores[0:3])
print (quiz_scores[-3:])
print (max(quiz_scores))
print (min(quiz_scores))

if (min(quiz_scores)) < 70: #if any(score < 70 for score in quiz_scores):
    print ("WARNING: At least one failing score!")
else:
    print ("All students passed!")
bonus_scores = tuple(5 + score for score in quiz_scores)
final_scores = quiz_scores + bonus_scores
print(len(final_scores))
print (final_scores[-1])




