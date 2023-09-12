#Write a Python function to check whether a number falls within a given range.
def test_range(number):
    if number in range(3,9):
        print(str(number))
    else :
        print("The number is given inside the range")
test_range(7)