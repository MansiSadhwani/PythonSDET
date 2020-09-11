Mylist = list(input("Enter the numbers:").split(","))
print(Mylist)

first = Mylist[0]
last = Mylist[-1]

if (first == last):
    print("first and last numbers are same")
else:
    print("First and last numbers are different")
