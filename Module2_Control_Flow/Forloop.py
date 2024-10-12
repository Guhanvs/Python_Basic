# Syntax
# for item in range/iterable:
#     Statements

names = ["Ajay","Boomer","Hari"]
for name in names:
    print(name,end=" ")
print("")
# Looping a String

companyName = "Ednue"
for letter in companyName:
    print(letter)

# Looping a dictionary
fruits ={
    "apple":50,
    "grapes":60,
    "orange":70
}
for fruit in fruits.items():
    print(fruit)

# Method 2

for key,value in fruits.items():
    print("key is "+ fruit[0])
    print("Value is "+ str(fruit[1]))

# Method3

    for key ,value in fruits.items():
        print(f"Count of {key} is {value}")

# Count
total = 0
for count in fruits.values():
    total +=count
print(total)