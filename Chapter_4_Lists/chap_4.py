# Lists

spam = ['cat', 'bat', 'rat', 'elephant']

print(spam)
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

print('Hello, ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

print(spam[-1])
print(spam[-3])

print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

print(spam[0:4])

print(len(spam))

del spam[3]

print(spam)

print(len(spam))

# bad way to write a code:

#catName1 = input("Enter the name of cat 1: ")
#catName2 = input("Enter the name of cat 2: ")
#catName3 = input("Enter the name of cat 3: ")
#catName4 = input("Enter the name of cat 4: ")

#print("The cat names are:")
#print(catName1 + " " + catName2 + " " + catName3 + " " + catName4)

# good way to write a code:

#catNames = []
#while True:
#    print("Enter the name of cat " + str(len(catNames) + 1) + " (Or enter nothing to stop.):")
#    name = input()
#    if name == "":
#        break
#    catNames = catNames + [name] # list concatenation
#print("The cat names are: ")
#for name in catNames:
#    print("   " + name)
    

# Loop with list:
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

# The in and not in Operators
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)

#myPets = ['Zophie', 'Pooka', 'Fat-tail']
#print('Enter a pet name:')
#name = input()
#if name not in myPets:
#    print("I do not have a pet named " + name + ".")
#else:
#   print(name + " is my pet.")

# Finding a Value in a List

print(spam.index('hello'))
print(spam.index('heyas'))

# Sequence Data Types:

name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' not in name)
for i in name:
    print('* * * ' + i + ' * * *')


name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)