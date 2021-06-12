def values_greater_than_second():
    global x
    listA = (input("Enter a list of numbers here:").split()
    secondNum = listA[1]
    secondList = []
    x = len(listA)
    def newListFormation(listA):
        global x
        counter = 0
        greaterCounter = 0
        while x != 0:
            if x < 2:
                return "False"
            elif listA[counter] > listA[1]:
                secondList.append(listA[counter])
                greaterCounter = greaterCounter + 1
                counter = counter + 1
                x = x - 1
        print (greaterCounter)
        return secondList
    newListFormation(listA)
values_greater_than_second()