import numpy as np
# creating numpy array
numbers = np.array([1,2,3,4,5])
print(numbers)
print(type(numbers))

# vectorized operations
doubled = numbers * 2 # will multiply each number with 2
# no need of loop
print(doubled)
print(numbers + 10) # add 10 to each index value
print(numbers - 1) 
print(numbers ** 2)

# comparing with list
numbers_list = [1,2,3,4,5]
doubled_list = numbers_list * 2 # it will duplicate all elements
print(doubled_list)
# so numpy arrays are preferred

# operations on multiple arrays
a1 = np.array([1,2,3])
a2 = np.array([10,20,30])

print(a1 + a2) # added position by position
print(a1 * a2) # multiplied position by position

# array indexing and slicing - same as list
num = np.array([10,20,30,40,50])
print(num[0]) # 10 
print(num[-1]) # 50
print(num[1:4]) # 20,30,40

# built-in functions
num1 = np.array([5,2,8,1,9])

print(f"Sum is: {num1.sum()}")
print(f"Minimun number is: {num1.min()}")
print(f"Maximum number is: {num1.max()}")
print(f"Mean is: {num1.mean()}")
print(f"Standard deviation is: {num1.std():.2f}")

# daily problem
scores = np.array([65, 72, 88, 91, 55, 78, 82])
scores = scores + 5
print(f"Average of scores after bonus is: {scores.mean():.2f}")
print(f"Students scores greater than 80: {scores[scores>80]}")

import numpy as np
numbers = np.array([1,2,3,4,5])
numbers = numbers + 5 
# to add 2 things, their shape must match
# numpy automatically created [5,5,5,5,5] on + 5
print(numbers)
# this is call broadcasting


# craeting 2D array
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(matrix.shape) # 3 rows, 3 columns

# broadcasting with a 2d-matrix
print(matrix + 10) # for each element

# adding row values to corresponding rows
row_addition = np.array([100,200,300])
print(matrix + row_addition) 
# added 100 to first column of each row
# added 200 to second column of each row
# added 300 to third column of each row


# Boolean indexing
scores = np.array([65, 72, 88, 91, 55, 78, 82])
print(scores[(scores>70) & (scores<90)])
# use & instead of AND, | instead of OR

# np.where() = change values according to condition
result = np.where(scores>= 70, "Pass","Fail")
print(result)

# aggregations on 2D-array : axis parameter
matrix1 = np.array([
    [1,2,3],
    [4,5,6]
])
print(matrix1.sum()) # sum of all elements
print(matrix1.sum(axis=0)) # sum of columns (3 columns)
print(matrix1.sum(axis=1)) # sum of rows (2 rows)

# daily problem
students_scores = np.array([
    [80,90,70], # student 1
    [60,85,95],
    [75,65,88]
])
# average
print(f"Average of Students: {students_scores.mean(axis=1)}")
print(f"Average of subjects: {students_scores.mean(axis=0)}")

new_arr = np.where(students_scores>75, "Good", "Needs Improvement")
print(new_arr)