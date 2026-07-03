# Arithmetic oeprators -used with numeric values to preform
#math operations

x = 1
y = 2
res = 0

res = x + y
print (res)
res = x - y
print (res)
res = x * y
print (res)
res = x / y
print (res)
res = x ** y
print (res)
res = x // y
print (res)

# Assignment Operators -used to assign values to variables
# = means assignment
# +=, -=, *=, /= shortcuts

x = 5
x += 5
x -= 3
x *= 3
x /= 2
print(x)

# COMPARISON OPERATORS - used to compare two values
# == (equal to), !=(not equal), <=(less than) >=(greater than)

# LOGICAL OPERATORS - used to combine conditional statemants (booleans T/F)
# and -> both must be True
# or -> at least one must be True
# not -> flips True to False (vice versa)

x = 3
y = 10
z = 3

print(x == y and y == z)  # False, because both conditions are NOT true
print(x == y or y == z)   # True, because one condition is true
print(not x == y)         # True, because x != y

x = [1, 2, 3, 4, 5]

print (4 in x)
print (9 not in x)