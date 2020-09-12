def Fibonacci(num):
    if num <=1:
        return num
    else:
        return (Fibonacci(num-1) + Fibonacci(num-2))
       
Fnum = int(input("Enter the numbers you want to see in fibonnaci series:"))
for i in range(1,Fnum+1):
    print(Fibonacci(i))
