#Assignment 3 Part 1

#getting input from user
n=int(input("Enter the value which you want a factorial of(whole num):"))

#calculating value of n!
def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
facval2= factorial(n)

#printing value of n!
print("Factorial of",n,"is=",facval2)