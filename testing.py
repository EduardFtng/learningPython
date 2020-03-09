import random

aList = []
i = 0
while i < 100:
    v = random.randint(0, 1)
    if v == 0:
        aList += 'H'
    else:
        aList += 'T'
    i+=1

print(len(aList))