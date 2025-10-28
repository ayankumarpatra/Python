def Factorial (value):
    if not isinstance(value,int) or value<0:
        print("Invalid value to calculate factorial\n")
        return
    if value==0 or value==1:
        return 1
    return value*Factorial(value-1)

print(Factorial(5))