def isPalindrome(strng):
    if strng is None:
        return True
    if len(strng) == 1:
        return True    
    
    if strng[0] != strng[len(strng)-1]:
        return False

    return isPalindrome(strng[1:len(strng)-1])    

print(isPalindrome('cuttack'))