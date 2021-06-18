def values_greater_than_second():
    list = input("Enter a list of numbers here:").split()
    x = str(len(list))
    list = int(list)
    secondNum = list[1]
    secondList = []
    def newListFormation(list):
        counter = 0
        greaterCounter = 0
        global x
        while x != 0:
            counter = counter + 1
            if list[counter] > list[1]:
                secondList.append(list[counter])
                greaterCounter = greaterCounter + 1
        if counter < 2:
            return "False"
        print (greaterCounter)
        return secondList
values_greater_than_second()