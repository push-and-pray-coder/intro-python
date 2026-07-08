#List 
pets = ["dog", "cat", "hamster"] #pets list#
print(pets[0]) # print dog by index
pets[2] = "gerbil" #replace hamster with gerbil
pets.remove("gerbil") #remove gerbil by value
print(pets) #print the list
print(len(pets)) #print length of pets


#Dictionary
student = {"name" : "Bob", "age" : 20} #new dictionary
print(student["name"]) #access students name
print(student)
print (len(student))
student["GPA"] = 3.9 #add a key
print(student)
print (len(student))
student["attendance"] = "perfect"
print(student)
print (len(student))
student["name"] = "Chris"
print(student)
print (len(student))
del student["age"]
print(student)
print (len(student))

