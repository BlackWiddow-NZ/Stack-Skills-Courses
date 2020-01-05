someNumber = 10

def functionThatModifiesNumber(someNumber):
    print("Arguement (input) passed in = ", someNumber)
    someNumber = someNumber * 10
    print("Arguement after modification inside function is = ", someNumber)
    return


def functionThatReassignsNumber(someNumber):
    print("Arguement (input) passed in = ", someNumber)
    someNumber = 3.14
    print("Arguement after modification inside function is = ", someNumber)
    return

def calculateAreaOfACircle(radius):
    area = 3.14 * radius * radius
    return area

def printAreaOfACircle(radius):
    area = 3.14 * radius * radius
    print("Area = ", area)

def calculateAreaOfManyCircles(radiusList):
    resultList = []
    for oneRadius in radiusList:
        resultList.append(3.14*oneRadius*oneRadius)
    return resultList

def calculateAreaAndCircumfrence(radiusList):
    areaResultList = []
    circumfrenceResultList = [  ]
    resultHash = {'Areas':areaResultList, 'Circumfrences': circumfrenceResultList}
    for oneRadius in radiusList:
        areaResultList.append(3.14*oneRadius*oneRadius)
        circumfrenceResultList.append(3.14*2*oneRadius)

    return resultHash



functionThatModifiesNumber(10)
print("Arguement after modification outside function is = ", someNumber)
functionThatReassignsNumber(10)
print("Arguement after modification outside function is = ", someNumber)
radius = 5
area = calculateAreaOfACircle(radius)
print ("Radius = ", radius, "Area = ", area)
printAreaOfACircle(radius)
radiusList = [1, 2, 3, 4]
areaList = calculateAreaOfManyCircles(radiusList)
print("For all circles with radii = ", radiusList, "areas are = ", areaList)
resultMap = calculateAreaAndCircumfrence(radiusList)
print("fr circles with radii = ", radiusList, "\n the area is", resultMap['Areas'], "\n circumfrences are = ", resultMap['Circumfrences'])
