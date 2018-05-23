# Content of Test Palindrome program

# Check whether given word is a palindrome


def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


word = str(input("Enter string:"))

if is_palindrome(word):
    print("\nYes! the string given is a palindrome!")
else:
    print("\nNo! teh string given isn't a palindrome!")