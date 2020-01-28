#Write a Python function that takes a list and 
# returns a new list with unique elements of the first list.

def unique_list(l):
# Provide empty list    
  new_list = []
  for a in l:
    if a not in new_list:
      new_list.append(a)
  return new_list

l=[1,2,3,4,4,5,5,6,6,7,7,7,8,8,9,9,9,9]
print(l)
new_list= unique_list(l)
print ("Unique_list:")
print(new_list)
