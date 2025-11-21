def Print_Sum(val):
    if val==0:
        return 0
    return val +Print_Sum(val-1)

n=int(input("Enter thr value"))
print(Print_Sum(n))