def palindrome_check(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False