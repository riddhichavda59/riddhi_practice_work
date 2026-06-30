# loop in python

'''
1. While loop
2. For loop
'''
# a while loop runs as long as the condition is true.

'''
while condition:
 #code block
'''
'''
# print number 1 to 5
print("1")
print("2")
print("3")
print("4")
print("5")

i=1
while i<=5:
 print(i)
 i+=1
print("="*20)

i=5
while i>=1:
 print(i)
 i-=1
'''
# for loop

'''
rage
lists
strings
truples
dictionaries
'''

'''
for variable in sequence:
#code block
'''
# print number 1 to 5
'''
print("======for loop=====")
for i in range(1,6):
 print(i)

 
print("===== string loop ====")

name="pyhon"

for i in name:
    print(i)

print("=== loop through list ====")
fruits=["apple","orange","banana","mango"]
for item in fruits:
    print (item)
'''
# range() function
#rang(start,stop,step)

for i in range(5):
    print(i)
    print("="*20)

for i in range(1,6):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)

# nested loops in python

'''
tables
patterns
matrices
grids
'''
'''
for i in range():
for j in range():
 # block of code

'''
print("===")
for i in range(1,5):
    for j in range(1,4):
        print(j, end ="")
        print()

print("========= breack statement===========")

# stops the loop immediately

for i in range(1,7):
    if i ==4:
        break
    print(i)

print("===== continue statement======")

# skips current iterations

for i in range(1,7):
    if i ==4:
        continue
    print(i)

print("===pass statement====")

for i in range(1,7):
     if i ==5:
         pass




























    

