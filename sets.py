# list represent : []
# tuple represent : ()
# set represent : {}

s = {'Bluberry', 'Resberry'}
print(s) # set(['Bluberry', 'Resberry'])
s.add("Strawberry") 
print(s) # set(['Bluberry', 'Resberry', 'Strawberry'])
s.add(4)
print(s) # set(['Bluberry', 'Resberry', 4, 'Strawberry'])
s.add("banana")
print(s)

numberSet = {1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9, 0, 0, 'a', 'c', 'b', "abc", 'abc'}
no_duplicate_set = set(numberSet)
print(no_duplicate_set) #output : set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'c', 'abc', 'a', 'b'])
no_duplicate_list = list(numberSet)
print(no_duplicate_list) # output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'c', 'abc', 'b', 'a']

library1= {"Harry Porter", 'Hunger Games', 'Lord of the rings'}
library2= {'Harry Porter', 'Romeo and Juliet'}

all_books_in_town = library1.union(library2)
print(all_books_in_town) # output = set(['Romeo and Juliet', 'Hunger Games', 'Lord of the rings', 'Harry Porter'])

all_both_libraries = library1.intersection(library2)
print(all_both_libraries) # output = set(['Harry Porter'])

diff = library1.difference(library2)
print(diff) # output =  set(['Hunger Games', 'Lord of the rings'])

diff2 = library2.difference(library1)
print(diff2) # output = set(['Romeo and Juliet'])

test1 = {2, 3, 3}
test2 = {1, 7}
print(test1.difference(test2)) # output : set([2, 3])