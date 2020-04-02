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
print(digits[0:10:3]) # output = [0, 3, 6, 9]; slicing element
print(digits[::]) # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; here show output everything
print(digits[::1]) # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; here show output everything
print(digits[::2]) # output = [0, 2, 4, 6, 8]; here show element first index and also show third element expect to first element.
print(digits[::-1]) # output = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; It go from the end of the list (backward=decending of the list of the element)
print(digits[::-2])  #output = [9, 7, 5, 3, 1];
print(digits[::-3])  #output = [9, 6, 3, 0];
print(digits[0:5:-2]) #output = [5, 4, 3, 2, 0]
for i in range(len(digits)) :
    print(digits[0:i])
for i in range(len(digits)) :
    print(digits[i:i+3])
for i in range(len(digits)-2) :
    print(digits[i:i+3])
window_size = 3
for i in range(len(digits)-2) :
    print(digits[i:i+window_size])
window_size1 = 7
for i in range(len(digits)-(window_size1-1)) : #Such math notation: 10 - (5 - 1) = 6; 10 - 5 - 1 = 4
    print(digits[i:i+window_size1])
window_size2 = 1
for i in range(len(digits)-(window_size2-1)) :
    print(digits[i:i+window_size2])
name = "first last"
print(name[0:5]) # output = first ;
