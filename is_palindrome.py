def is_palindrome(word):
    word = word.lower()
    reverse = ''.join(reversed(word))
    return reverse == word


