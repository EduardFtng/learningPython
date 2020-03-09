spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = []
def commaCode(aList):
    i = 0
    aString = ''
    
    while i < len(aList)-1:
        
        aString += aList[i] + ', '
        i += 1

    return aString + 'and ' + aList[-1]

def commaCode2(aList):
    try:
        return ', '.join(aList[:-1]) + ' and ' + aList[-1]
    except IndexError:
        return 'The list is emtpy.'

print(commaCode(spam))
print(commaCode2(spam))
print(commaCode2(spam2))