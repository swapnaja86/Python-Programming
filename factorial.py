#Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
def calc_factorial(no):
    fact=1
    while(no>1):
        fact*=no
        no-=1
       
    return fact
no= int(input('Enter no:'))
fact=calc_factorial(no)
print("Factorial of {}:{}".format(no,fact))
