#Rating of Difficulty: 4/10 
#Q1 ISBN Number 

isbn = input()

def computeISBN(isbnNum):
    value = 0
    missingIndex = 0
    for x in range(len(str(isbnNum)), 0, -1):
        if isbnNum[len(isbnNum)-x] == "?":
            missingIndex = x
            continue
        if isbnNum[len(isbn)-x] == "X":
           value += 1 * 10
           continue
        value += int(isbnNum[len(isbnNum)-x])* x
    counter = 1
    while True:
       missingValue = counter*11 - (value % 11)
       if missingValue % missingIndex == 0:
           break
       counter += 1
    if missingIndex == 1 and missingValue == 10:
        return "X"
    return missingValue // missingIndex

def validateISBN(isbnNum):
    value = 0
    for x in range(len(str(isbnNum)), 0, -1):
        if isbnNum[len(isbn)-x] == "X":
           value += 1 * 10
           continue
        value += int(isbnNum[len(isbnNum)-x])* x
    if value % 11 == 0:
        return True
    else:
        return False

def c(isbnNum):
    validISBNs = []
    for x in range(0, len(str(isbnNum))):
        for y in range(0, len(str(isbnNum))):
            if x == y:
                continue
            isbnNumList = list(isbn)
            temp = isbnNumList[x]
            isbnNumList[x] = isbnNumList[y]
            isbnNumList[y] = temp
            res = "".join(isbnNumList)
            if validateISBN(res) == True and res not in validISBNs:
                validISBNs.append(res)
    return  validISBNs

"""
to run part a
print(computeISBN(isbn))
"""
"""
to run part b
print(validateISBN(isbn))
"""
"""
to run part c
print(c(isbn))
"""
