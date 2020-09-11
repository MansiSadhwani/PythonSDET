MyTuple = tuple(input("Enter the numbers:").split(","))
print(MyTuple)
print("Numbers divisible by 5 are:")
for num in MyTuple:
    if(int(num)%5 == 0):
        print(num)
 
