
def sum(x,y):
    result= x+y
    return(result)

def sub(x,y):
    result= x-y
    return(result)

def mul(x,y):
    result= x*y
    return(result)

def div(x,y):
    result= x/y
    return(result)

x= int(input("Enter first number:"))
y= int(input("Enter second number:"))

print("Sum of the given two numbers is:",sum(x,y))
print("sub of the given two numbers is:",sub(x,y))
print("mul of the given two numbers is:", mul(x,y))
print("Div of the given two numbers is:", div(x,y))