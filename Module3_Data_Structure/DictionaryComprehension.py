# Dict comprehension
# simply a looping + condition
# used to filter data & convert List => Dictionary


# Dictionary comprehension Syntax

fruits = {
    "apple":7,
    "banana":20,
    "pineapple":6,
    "watermelon":3
}

orderCount = {fruitName:10-stockCount for fruitName,stockCount in fruits.items() if stockCount < 10}
print(orderCount)