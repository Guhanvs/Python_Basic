name ={'abc','def','efg','abc'} #Duplicates will be removed
name1={1,2,3,4,5,'abc','de'}
print(type(name1))
print(name)
print(name.add('abc'))
print(name)#no duplicates
print(name1.remove(3))
print(name1)
print(name.union(name1))
print(name.intersection(name1))
print(name.difference(name1))
