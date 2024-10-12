def classify_age():
    age = int(input("Enter your Age:"))
    if(age<=0):
        print("Retry Again")
    elif(age<18):
        print("Minor")
    elif(age>18 and age<65):
        print("Adult")
    else:
        print("Senior Citizen")

classify_age()