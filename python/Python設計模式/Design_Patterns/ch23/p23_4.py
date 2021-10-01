# p23_4.py
def isEvenNumber(num):
    return num % 2 == 0
def isGreaterThanTen(num):
    return num > 10
def getResultNumbers(fun, elements):
    newList = []
    for item in elements:
        if (fun(item)):
            newList.append(item)
    return newList

def testCallback():
    elements = [2, 3, 6, 9, 12, 15, 18]
    list1 = getResultNumbers(isEvenNumber, elements)
    list2 = getResultNumbers(isGreaterThanTen, elements)
    print("所有的偶數：", list1)
    print("大於10的數：", list2)

testCallback()
