#Assignment 3 Part 2

#initialising modules
import math

#getting input from user
num=float(input("Enter the value which you want operations to be performed on:"))

#performing operations values
sqrt_result = math.sqrt(num)
log_result = math.log(num)
sine_result = math.sin(num)

#printing value of operations performed
print("Square root of",num,"is",sqrt_result)
print("Log",num,"is",log_result)
print("Sine of",num,"(in radians) is",sine_result)