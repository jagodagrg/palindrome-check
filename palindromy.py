def palindrome_check(word):
    reversed_word = word[::-1]
    return reversed_word == word

print(palindrome_check('kajak'))
print(palindrome_check('kajaki'))