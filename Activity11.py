Fruits = {"mango" : 100,
          "apple" : 50,
          "banana": 10,
          "coconut":30}

CheckAvailability = input("Enter the fruit you want: ").lower()

if(CheckAvailability in Fruits):
    print(CheckAvailability, 'is available')
else:
    print(CheckAvailability, 'is not available')
