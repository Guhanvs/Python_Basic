# Method 1 -Concatenation using + operator
companyName = "Ednue Technologies"
suffix = "Pvt Ltd"
print(companyName + suffix)


# Method 2 - '%' or C-Style String Format
# %s for Strings
# %d for Integer
# %f for Float

name ="Arun" # String
age = 10 # Integer
score = 99.12345
# print(name + age) # TypeError: can only concatenate str (not "int") to str
print("%s age is %d . He Scored %.2f"%(name,age,score))


# Method 3 - .format() method
print("{} age is {} and has Scored {}".format(name,age,score))

# Method 4 - f'String
personName= "Guhan"
collegeName = "AIHT"
print(f"{personName} is Studying in {collegeName}")