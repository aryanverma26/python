#Write a Python function to find the minimum of three numbers. 
def minimum_number(a,b,c):
    if a<b and a<c: 
        print(a)
    elif b<c:
        print(b)
    else:
        print(c)
minimum_number(4,5,6)

     