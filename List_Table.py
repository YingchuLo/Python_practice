"""
Chap 6 Project,'Automate the Boring Stuff with Python: Practical Programming for Total Beginners'

Goal of this code: Change a list with two loops into a table
Key words: ''.join(), rjust()
hint: First, calculate the length of longest words for each column.
Set the length as the value for rjust().
"""

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


def printTable(t):
    colWidths = [0] * len(t)
    for i in range(len(t)):
        colWidths[i] = len(max(t[i],key=len))

    sum=0
    for i in range(len(t)):
        sum=sum+colWidths[i]
        colWidths[i]=sum

    for i in range(len(t[0])):
        j=0
        print ''.join([tableData[j][i].rjust(colWidths[j]), tableData[j+1][i].rjust(colWidths[j+1]), tableData[j+2][i].rjust(colWidths[j+2])])

printTable(tableData)



