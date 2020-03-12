# The Dictionary Data Type

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])
print('My cat hast ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print()

# Vs Lists
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

"""
# Birthdays
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


while True:
    print('Enter the name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of ' + name)
        
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()

        birthdays[name] = bday
        print('Birthday database updated.')
"""

print()
print()

# Dictionary methods: keys(), values() and items()
spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v)

print()

for k in spam.keys():
    print(k)

print()

for i in spam.items():
    print(i)

print()

# get() method
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# setdefault() method
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(str(spam.get('color', 0)))

print()

# charecter Counter + prety print
import pprint

message = 'It was a bright cold day in April, and the clocks were stricking \
thirteen.'

count = {}

for charecter in message:
    count.setdefault(charecter, 0)
    count[charecter] = count[charecter] + 1

pprint.pprint(count)