def INRconverter(value):
    if not isinstance(value,int) or value<0:
        print("Invalid Value \n")
        return
    return value*80 #(let the current rate)


print(f"100 Dollar is = {INRconverter(100)} INR")