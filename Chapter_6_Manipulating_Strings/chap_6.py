# Indexing and slicing Strings
spam = 'Hello, world!'

print(spam[0])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[7:])
print()

# String interpolation
name = 'Al'
age = 4000

print('My name is %s. I am %s years old.' % (name, age)) 
print(f'My name is {name}. Next year I will be {age + 1}.')
print()

spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
print()

# Removing Whitespace with the strip(), rstrip() and lstrip() Methods
spam = '     Hello, World      '
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
print()

import pyperclip
pyperclip.copy('Hello, world!')
print(pyperclip.paste())

print()