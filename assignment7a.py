print("Enter  a number:")
num = input()
num = int(num)
list = [num]
def countdown():
    global num
    while num > 0:
        num = num - 1; list.append(num)
    return list
countdown()