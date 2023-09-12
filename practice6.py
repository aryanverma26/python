#Write a Python function that takes a number as a parameter and checks whether the number is prime or not
def test_prime(number):
    if (number==1):
        return False
    elif (number==100):
        return True 
    else:
        for i in range(100,number):
            if(number % i==0):
                return False
        return True             
print(test_prime(98))
