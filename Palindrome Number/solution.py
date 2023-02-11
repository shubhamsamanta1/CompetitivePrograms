def palindrome(s) -> bool:
    input = s
    reverse = 0
    while (input >0):
        get = input%10
        reverse = reverse*10 + get
        input = input//10
    
    if(s == reverse):
        return True
    else:
        return False


s = 121
print(palindrome(s)) 