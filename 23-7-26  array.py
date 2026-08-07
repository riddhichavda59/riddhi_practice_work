# Create and Diaplay 2D Arrays
'''
matrix = []

for i in range(3):
    row = list(map(int , input(f" Enter Row {i + 1} :").split()))
    matrix.append(row)
    
for row in matrix:
    for value in row:
        print(value , end=", ")
    print()

for row in matrix:
    print(row , end=",\n")


for row in matrix:
    print("[" , end="")
    print(*row , sep=" , " , end="")
    print("]")
    
print(matrix)
'''

matrix = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

print(matrix[0][0])

print(matrix[1][1])
