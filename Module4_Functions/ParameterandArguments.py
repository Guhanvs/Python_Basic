def addition(num1,num2):
    sum1 = num1 + num2
    return sum1
print(addition(10,20))


def addition(num2=10,num1=20):
    sum1 = num1 + num2
    return sum1
print(addition())

# Method Arbitrary Arguments(*args)
def addition(*nums):

    return sum(nums)
print(addition(10,20,4,5,6,7,8,8,))



# Keyword and Arbitrary Arguments(**kwargs)
# laptop ={
#     "dell":10,
#     "lenovo":20,
#     "asus":15,
#     "apple":35
# }



def laptopCount(**Values):
    print(Values)
laptopCount (name1="dell",count1=10,
              name2="asus",count2=20,
              name3="mac",count3=40)

# DefaultValue
def defaultValues(x,y="Ednue"):
    print(y)
defaultValues(10)
