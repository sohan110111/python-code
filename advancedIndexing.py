# indexing, slicing, striding

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[0]) # output = 0; here call any element of the index like this line of code
print(digits[-0]) # output = 0; It's show output 0
print(digits[-1]) # output = 9; here show the last element of the list
print(digits[-2]) # output = 8; here show output last indexing output of the index number decreasing 
print(digits[-3]) # output = 7;
# and so on decreasing the indexing number and show output last to first 
print(digits[-len(digits)]) # output = 0;
print(digits[:]) # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; here show output all element of the lest 
print(digits[0:]) # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
print(digits[:3]) # output = [0, 1, 2]; here show the parts of the array
print(digits[2:4]) # output = [2, 3]; here 2 is inclusive and 4 is exclusive
print(digits[0:9]) # output = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(digits[0:-1]) # output = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(digits[0:10:3]) # output = ; slicing element
print(digits[::]) # output = ; here show output everything
print(digits[::1]) # output = ; here show output everything
print(digits[::2]) # output = ; here show element first index and also show third element expect to first element.
print(digits[::-1]) # output = ; It go from the end of the list
print(digits[::-2])  #output = ;
print(digits[::-3])  #output = ;
name = ["first last"]
print(name[:5]) # output = ; here output first 
