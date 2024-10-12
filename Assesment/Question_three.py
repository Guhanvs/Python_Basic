def calculate(nums: list=[],operator="sum"):
    if operator == "sum":
        return sum(nums)
    elif operator=="product":
        product=1
        for num in nums:
            product *=num
        return product
    else:
        print("operator not supported")

print(calculate([1,2,3],"sum"))
print(calculate([1,2,3],"product"))