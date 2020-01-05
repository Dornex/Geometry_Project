import math
import numpy as np
import time as time
import matplotlib.pyplot as plt
delay = 1.5
filename = 'date.in'
myList = []

with open(filename) as f:
    line = f.readline().split()
    n = int(line[0])
    while line:
        line = f.readline().split()
        if line:
            line[0] = int(line[0])
            line[1] = int(line[1])
            plt.plot(line[0], line[1], 'o', color='black')
            myList.append(line)

plt.draw()

firstPoint = myList[0]
for list in myList:
    if list[1] < firstPoint[1]:
        firstPoint = list
    elif list[1] == firstPoint[1]:
        if list[0] < firstPoint[0]:
            firstPoint = list

plt.pause(delay)
plt.plot(firstPoint[0], firstPoint[1], 'o', color='red')      
plt.draw() 

myList.remove(firstPoint)
cnt = 0

for list in myList:
    a = list[0] - firstPoint[0]
    b = math.sqrt((firstPoint[0] - list[0]) ** 2 + (firstPoint[1] - list[1]) ** 2)
    alfa = math.acos(a/b)
    list.append(round(alfa, 4))
    list.append(round(b, 4))
    myList[cnt] = list
    cnt += 1

myList.sort(key = lambda x: (x[2], x[3]) )
firstPoint.append(0)
firstPoint.append(0)
myStack = [firstPoint, myList[0], myList[1]]

plt.pause(delay)
plt.plot([firstPoint[0], myList[0][0]], [firstPoint[1], myList[0][1]], 'r-')
plt.draw()
plt.pause(delay)
plt.plot([myList[0][0], myList[1][0]], [myList[0][1], myList[1][1]], 'r-')
plt.draw()

myList.remove(myList[0])
myList.remove(myList[0])
i = 2

for list in myList:
    i += 1
    myStack.append(list)
    det =  myStack[i-2][0] * myStack[i-1][1] + myStack[i-1][0] * myStack[i][1] + myStack[i-2][1] * myStack[i][0] - myStack[i][0] * myStack[i-1][1] - myStack[i-2][1] * myStack[i-1][0] - myStack[i][1] * myStack[i-2][0]
    while det < 0 and i > 2:
        plt.pause(delay)
        plt.plot([myStack[i-2][0], myStack[i][0]], [myStack[i-2][1], myStack[i][1]], 'r')
        plt.plot([myStack[i][0], myStack[i-1][0]], [myStack[i][1], myStack[i-1][1]], 'b--')
        plt.plot([myStack[i-2][0], myStack[i-1][0]], [myStack[i-2][1], myStack[i-1][1]], 'b--')
        plt.draw()

        myStack.pop(i-1)
        i -= 1
        det =  myStack[i-2][0] * myStack[i-1][1] + myStack[i-1][0] * myStack[i][1] + myStack[i-2][1] * myStack[i][0] - myStack[i][0] * myStack[i-1][1] - myStack[i-2][1] * myStack[i-1][0] - myStack[i][1] * myStack[i-2][0]

    plt.pause(delay)
    plt.plot([myStack[i][0], myStack[i-1][0]], [myStack[i][1], myStack[i-1][1]], 'r')
    plt.draw()

plt.pause(delay)
plt.draw()
reversedMyList = reversed(myList)

plt.plot([myList[len(myList) - 1][0], myStack[len(myStack) - 1][0]], [myList[len(myList) - 1][1], myStack[len(myStack) - 1][1]], 'r-')
plt.draw()

for list in reversedMyList:
    if list[2] == myStack[i][2]:
        det = myStack[0][0] * myStack[i][1] + myStack[i][0] * list[1] + myStack[0][1] * list[0] - list[0] * myStack[i][1] - list[1] * myStack[0][0] - myStack[0][1] * myStack[i][0]
        if det == 0 and list not in myStack:
            plt.pause(delay)
            plt.plot([list[0], myStack[i][0]], [list[1], myStack[i][1]], 'r-')
            plt.draw()
            myStack.append(list)
            plt.pause(delay)
            plt.plot([list[0], myStack[i][0]], [list[1], myStack[i][1]], 'r-')
            plt.draw()

ax = plt.gca()

def removeLines():
    i = 0
    for line in ax.lines:
        lineData = line.get_data()
        remove1 = True
        remove2 = True
        if(len(lineData[0]) > 1):
            x1 = lineData[0][0]
            x2 = lineData[0][1]
            y1 = lineData[1][0]
            y2 = lineData[1][1]
            for item in myStack:
                if x1 == item[0] and y1 == item[1]:
                    remove1 = False
                if x2 == item[0] and y2 == item[1]:
                    remove2 = False

            if remove1 == True or remove2 == True:
                line.remove()
        i += 1

removeLines()
removeLines()
removeLines()
removeLines()
removeLines()

plt.plot([firstPoint[0], myStack[len(myStack) - 1][0]], [firstPoint[1], myStack[len(myStack) - 1][1]], 'r-')
plt.draw()         
plt.show()
