# print formatting using sep and end

'''
# using sep with end

print("Apple" , "Banana" , "Charry", sep="|" , end="<--- End of List\n")
    
# Fomatted Message for input

name = input("Enter your name:")
age = input("Enter your age:")
hobby = input("Enter your favorite hobby:")

print(f"Hello ,{name}! At{age}, enjoing{hobby} sound fun!")

'''
'''
# Basic arithmetic operations

a = float(input(" Enter first number:"))
b = float(input("Enter second number:"))


print("Addition :",a+b)
print("Subtraction:",a-b)
print("Multiplication:", a*b)
print("Divison:",a/b)
print("Floor Devision:", a//b)
print("Modulus:", a%b)
print("Expontiations :",a**b)
'''

# Decalre variable of diffrent data types and show their types


a = 10
b = 3.14
c = "Career X"
d = False

print("a =",a,"type:", type(a))
print("b =", b, "Type:", type(b))
print("c =",c, "type:", type(c))
print("d =",d,"type:", type(d))
                    
# type() function and id() function

a = 10
b = 20

print(id(a))
print(id(b))
