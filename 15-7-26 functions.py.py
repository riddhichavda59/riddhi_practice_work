#python Functions
#Built in functions
'''
print("="*20)
print("Eunctions with python")
print("="*20)

number=[1,45,85,22,66,34]
print(number)
print(len(number))
print(max(number))
print(min(number))
print(sorted(number))
print(sum(number))

print("="*20)
print("UDF Functions")
print("="*20)
'''
'''
def add(a,b):
    print(a+b)

add(10,20)
add(20,20)    
'''
'''
1.Reusability
2.Cleaner code
3.Better Orgaization
4.Reduce repetition
'''
print("="*20)
print("Recursion")
print("="*20)

# A function calling itself:
'''
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(10))

#sum of numbers.

def total(n):
    if n==0:
        return 0
    return+total(n-2)
    
print(total(10))
'''
print("="*20)
print("Anonymous Function / Lambda Functions")
print("="*20)

squre=lambda x : x*x
print(square(5))
add= lambda a,b:a+b
print(add(10,20))









