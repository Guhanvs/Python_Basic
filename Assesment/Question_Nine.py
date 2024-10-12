def merged(dict1,dict2):
    merged_dict=dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
merged=merged({'a':1,'b':2},{'b':1,'c':3})
print(merged)