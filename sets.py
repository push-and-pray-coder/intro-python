# SETS are UNORDERED, UNINDEXED, and have no DUPLICATES
# Created using {}

fruits = {"apple", "banana", "cherry"}
print(fruits)

# NO DUPLICATES ALLOWED
fruits = {"apple", "banana", "apple"}
print(fruits)

# checking if item exists
print("apple" in fruits)

# Adding Items
fruits.add("orange")
print(fruits)

# ADDING MULTIPLE items
fruits.update(["kiwi", "water"]) #any iterable will work
print(fruits)

# REMOVING items
fruits.remove("banana")
print(fruits)

# if you're not sure an item exists, use discard() to avoid errors
fruits.discard("water")
print(fruits)

set1 ={1,2,3}
set2 = {3,4,5}

print(set1.union(set2))              # combine both (no duplicates)
print(set1.intersection(set2))       # common elements (duplicates only)
print(set1.difference(set2))         # whats only in set 1
print(set1.symmetric_difference(set2)) # EVERYTHING except whats shared

# FROZENSET (a "locked" set)
locked_set = frozenset(["a", "b", "c"])
print(locked_set)
# locked_set.add("d") - Proof its now immutable

"""
-------------------------------
MINI CHALLENGE: PARTY GUEST LIST
-------------------------------
You’re organizing a party! You have two sets of guests.
1. Create two sets:
    invited_friends = {"Alex", "Sam", "Leo", "Nina"}
    rsvped = {"Nina", "Sam", "Jordan"}
2. Print:
    Everyone who was invited (union)
    Everyone who said they’re coming (rsvped)
    Who hasn’t replied yet (difference)
3. Add two new names to invited_friends.
4. One of the people canceled — remove them from rsvped.
5. Print how many total confirmed guests are attending.
6.Check if "Leo" is still coming — print a message depending on the result.
"""

invited_friends = {"Alex", "Sam", "Leo", "Nina"}
rsvped = {"Nina", "Sam", "Jordan"}

print(invited_friends.union(rsvped))
print(rsvped)
print(invited_friends.difference(rsvped))
invited_friends.update({"bob", "chuck"})
rsvped.discard("Leo")
print(len(rsvped))
if "Leo" in rsvped:
    print("Leo is still coming")
else:
    print("Leo is not coming")