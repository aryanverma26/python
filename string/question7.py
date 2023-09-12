#Write a Python function to multiply all the numbers in a list
def multiply(number):
    total = 1
    for i in number:
        total *= i
    return total 
print(multiply([4,8,16,]))
    