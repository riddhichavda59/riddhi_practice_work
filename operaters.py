# Python Operaters,Variables and Data Types

'''
1.Arithmetic Operator
2.Assignment Operator
3.Comparison Operator
4.Logical Operator
5.Bitwise Operator
6.Type Conversion Operator
'''
a = 10
b = 20

print('addition:',a+b)
print('substraction:',a-b)
print('multiplication:',a*b)
print('division:',a/b)
print('modulus:',a%b)
print('exponentiation:',a**b)
print('floor division:',a//b)

# Assignment Operator

x=5 #simple assignment
y=3

x+=y #x=x+y

print(x)
print(y)

x-=y
print(x)
print(y)

x/=y
print(x)
print(y)

x%=y
print(x)
print(y)

x**=y
print(x)
print(y)

x//=y
print(x)
print(y)

# comparison operator

x = 10
y = 10

print(x==y)
print(x!=y)
print(x<y)
print(x<=y)
print(x>y)
print(x>=y)

# Logical Operators(and,or,not)

x=True
y=False
z=False

print(x and y)
print(y and z)
print(x or y)
print(y or z)
print(not x)
print(not y)

# Type conversion

'''
int()
float()
str()
tuple()
list()
set()
dict()
'''
num_str = "123"
print(type(num_str))
num_int = int(num_str)
print(type (num_int))
print(num_int + 7)

# multiple assignment

x,y,z = 10,20,30
print(x,y,z)

a=20
b=21
print(id(a))
print(id(b))



