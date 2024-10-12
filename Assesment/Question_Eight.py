def count_vowel_const(word):
    vowel_set=("aeiouAEIOU")
    vowel_count=0
    const_count=0
    for char in word:
        if char.isalpha():
            if char in vowel_set:
                vowel_count+=1
            else:
                const_count+=1
    return(vowel_count,const_count)
print(count_vowel_const("hello"))

