def sum():
    Num = list(input("Enter the Number:").split(","))
    Result = 0
    for Number in Num:
        Result+=int(Number)
    return Result
    

print(sum())

