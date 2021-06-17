def values_greater_than_second():
    global x
    listA = (input("Enter a list of numbers here:").split())
    listA = [int(i) for i in listA]
    secondNum = listA[1]
    secondList = []
    x = len(listA)
    def newListFormation(secondList):
        global x
        counter = 0
        greaterCounter = 0
        while x != 1:
            if x < 2:
                return "False"
            elif listA[counter] > listA[1]:
                secondList.append(listA[counter])
                greaterCounter = greaterCounter + 1
                counter = counter + 1
                x = x - 1
            else:
                counter = counter + 1
                x = x - 1
        print (greaterCounter)
        return secondList
    newListFormation(secondList)
    return secondList
values_greater_than_second()