Mylist1 = list(input("Enter the numbers:").split(","))
Mylist2 = list(input("Enter the numbers:").split(","))
print(Mylist1)
print(Mylist2)

Mylist3 = []

for num in Mylist1:
    if(int(num)%2 != 0):
        Mylist3.append(num)
    
for num1 in Mylist2:
    if(int(num1)%2 == 0):
        Mylist3.append(num1)

print(Mylist3)
