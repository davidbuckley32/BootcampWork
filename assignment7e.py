def this_length_that_value():
    listA = (input("Enter the number of times you would like an integer to be repeated. Then, please put a space followed by the integer that you would like to be repeated. ").split())
    listA = [int(i) for i in listA]
    length = listA[1]
    value = listA[2]
    listB = []
    while length != 0:
        listB.append(listA[value])
        length = length - 1
this_length_that_value()