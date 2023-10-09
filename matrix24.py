matrix= [
    [1,2,3],
    [4,5,6],
]
'''              here the column and row is like   [0,1,2]=0  #rows arw horizontal
                                                   [0,1,2]=1  #columns are vertical
                                                   [0,1,2]=2 '''

print(matrix[1][1])


matrix[1][1]=10 # to change any index from matrix
print(matrix[1][1])

#to print all matrix index of the matrix
for row in matrix:
    for col in row:
     print(col)