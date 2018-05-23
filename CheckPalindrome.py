# Check the given word is a palindrome


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


word = input('\nEnter a word that to be checked whether palindrome: ')
if (is_palindrome(word)) is True:
    print('\nYes! the word given is Palindrome!!')
else:
    print('\nNo! the word given is not a Palindrome!!')
