#Write a Python function to find the maximum of three numbers.
def maximum_number(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c:
        print(b)
    else: 
        print(c) 
maximum_number(1,3,5)