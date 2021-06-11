def print_and_return():
    var1, var2 = input("Enter two numbers here:").split()
    var1, var2 = [int(var1), int(var2)]
    print(var1)
    return var2
print_and_return()