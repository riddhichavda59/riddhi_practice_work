# Print your name
'''
print("My name is riddhi.")

# User Input

name= input("Enter your  name:")
print("my name is", name)

a = int(input("Enter first value :"))
b = int(input("Enter second value :"))


print("a+b:",a+b)

# Swapping Variables (Using Third Variable)

a = 20
b = 40
temp = a
a = b
b = temp

print("value of a:",a)
print(" value of b:",b)
'''
# Chek Positive, Nagative and Zero.

valu = int(input("Enter a number:"))

if valu > 0:
     print("Positive")
elif valu <0:
     print("Nagative")
else:
     print("zero")

# Simple Interrest Calculate

p = float(input("Enter principal amount:"))
r = float(input("Enter rate of interest :"))
t = float(input("Enter time in years :"))

si = (p * r * t)/100

print(" Simple Interest :", si)
