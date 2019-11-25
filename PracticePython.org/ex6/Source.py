def palindrome(string):
    reverse_string = string [::-1]
    if reverse_string == string:
        return 1
    else:
        return 0


string = input("Give me text to check if it is a palindrome ")

if palindrome(string) == 1:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
