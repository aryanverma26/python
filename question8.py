# Write a Python program to reverse a string
def string_reverse(str1):
    rstr1 = ''    
    a = len(str1)
    while a > 0:
        rstr1 += str1[ a - 1 ]
        a = a - 1
    return rstr1 
print (string_reverse('abc123')) 


