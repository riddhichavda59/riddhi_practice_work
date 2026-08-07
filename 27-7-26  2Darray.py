# minimum and maximum value find Element....
'''
rows=  int(input("rows : "))
cols = int(input("cols : "))

matrix = []

for i in range(rows):

    row = list(map(int , input(f"Enter row {i + 1} : ").split()))

    matrix.append(row)

max_value = matrix[0][0]
min_value = matrix[0][0]

for row in matrix:

    for value in row:

        if value > max_value:

            max_value = value

        if value < min_value:

            min_value = value

print("Max-Value : " , max_value)
print("Min-Value : " , min_value)
'''

# Sorting in Integer list

'''
number = list(map(int , input(f"Enter Numbers:").split()))

number.sort()

number.sort(reverse=True)

print(number)
'''

# Sort List of Tuples by second Element
'''
students = [
    ("Raj" , 80),
    ("Rahul" , 65),
    ("Rajesh" , 47),
    ("Rohan" , 32),
    ("Rakesh" , 74)
]

sorted_std = sorted(students , key = lambda x : x[1])

print(sorted_std)

'''
# Sort Dictionary List by key

employees = [
    {"name" : "Raj" , "salary" : 45000},
    {"name" : "Amit" , "salary" : 30000},
    {"name" : "Neha" , "salary" : 55000},
    {"name" : "Priya" , "salary" : 40000}
]

result = sorted(employees , key = lambda x : x["salary"])

print(result)





    
