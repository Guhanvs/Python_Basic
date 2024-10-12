def is_Palindrome(word):
    normalized_word=word.replace(" "," ").lower()
    return normalized_word == normalized_word[::-1]
print(is_Palindrome("hello"))