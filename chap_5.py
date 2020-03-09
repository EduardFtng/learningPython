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