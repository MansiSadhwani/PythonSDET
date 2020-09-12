def CalcSum(num):
    if num:
        #print(num+CalcSum(num-1))
        return num+CalcSum(num-1)
    else:
        #print(0)
        return 0

result = CalcSum(10)

print(result)
