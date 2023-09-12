def minimum_number(a,b,c):
    if a<b and b<c:
        print(a)
    elif b<c:
        print(b)
    else:
        print(c)
        
a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
minimum_number(a,b,c)
            