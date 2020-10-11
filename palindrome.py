def is_palindrome(name):
    if name == name[::-1]:
        return True
    return False
        
print(is_palindrome("amama"))