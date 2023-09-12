#Write a Python program to sort a list of tuples using Lambda
name_age = [('mintu', 29), ('ayush',8), ('bhalu',25)]

name_age.sort(key= lambda a: a[-1])

print(name_age)