# variable assignment
name = "Guhan"
# String to Integer

stringCount = "10"
intCount = int(stringCount)
print(intCount)
print(type(intCount))

# Integer to String
number1 = "10"
string1 = str(number1)
print(string1)
print(type(string1))

# Basic Input and Output

# input
name1=input("Enter your Name:")
age=input("Enter your Age:")

# output
print("My Name is {} and my Age is {}".format(name1,age))

# To get multiple inputs in one input command

numbers = input("Enter Multiple Inputs Using comma Separation: ")
commaSeparatedValues = numbers.split(",")
print(commaSeparatedValues)