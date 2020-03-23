def printTable(stringList):
    colWidths = [0] * len(stringList)

    for i in range(len(stringList)):
        for j in range(len(stringList[i])):
            if len(stringList[i][j]) > colWidths[i]:
                colWidths[i] = len(stringList[i][j])

    for x in range(len(stringList[0])):
        for y in range(len(stringList)):
            print(stringList[y][x].rjust(colWidths[y]), end=' ')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
