import random

runs = 10000
numberOfStreaks = 0
counter = 0


for experimentNumber in range(runs):
    # Code that creates a list of 100 'heads' and 'tails' values.
    aList = []   
    i = 0

    while i < 100:
        v = random.randint(0, 1)
        if v == 0:
            aList += 'H'
        else:
            aList += 'T'
        i += 1

    # Code that checks if there is a streak of 6 heads or tails in a row.
    
    for c in range(len(aList)):
        
        if aList[c] == aList[c - 1]:
            counter += 1
            if counter == 6:
                numberOfStreaks += 1
                counter = 0
        else:
            counter = 0


print('Chance of streak: %s%%' % (numberOfStreaks / 100))

percentage_with_streaks = numberOfStreaks / runs        
print(
    f'Percentage of runs with a streak of 6: '
    f'{percentage_with_streaks*100}%'
)
# Percentage of runs with a streak of 6: 53.60%