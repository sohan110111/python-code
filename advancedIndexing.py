# indexing, slicing, striding

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[0]) # here call any element of the index like this line of code
print(digits[-0]) # It's show output 0
print(digits[-1]) # here show the last element of the list
print(digits[-2]) # here show output last indexing output of the index number decreasing 
print(digits[-3])
# and so on decreasing the indexing number and show output last to first 
print(digits[-len(digits)])
print(digits[:]) # here show output all element of the lest 
print(digits[:3]) # here show the parts of the array
print(digits[2:4]) # here 2 is inclusive and 4 is exclusive
print(digits[0:9]) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(digits[0:-1]) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(digits[0:])

name = ["first last"]
print(name[:5]) # here output first 