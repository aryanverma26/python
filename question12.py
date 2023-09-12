#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique_list(l):
  a = []
  for x in l:
    if a not in a:
      a.append(x)
  return a

print(unique_list([1,2,3,3,3,3,4,5])) 
