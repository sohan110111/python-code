from collections import OrderedDict # From collection package to import OrderedDict (and also search on google from and import in python)

groceries = {'bananas' : 5, 'oranges' : 3} # here some key value pair
print(groceries['bananas']) # output = 5
print(groceries.get('bananas')) # output = 5
print(groceries.get('hello')) # output = None

contacts = {
    'john' : ['4567-890', 'example@email.com'],  #'phone' : 'email' : 
    'jane' : ['45678-80', 'em@web.com']
}

print(contacts['john']) # output = ['4567-890', 'example@email.com']

sentence = "I like the name Aron because the name aron is the best"

word_counts = {
    'I' : 1,
    'like' : 2, 
    'the' : 3
}

#word_counts['the'] = word_counts['the'] + 1

#dict.items()
print(word_counts.items()) # output = [('I', 1), ('the', 3), ('like', 2)]
print(list(word_counts.items())) # output = [('I', 1), ('the', 3), ('like', 2)]

#dict.keys()
print(word_counts.keys()) # output = ['I', 'the', 'like']
print(list(word_counts.keys())) # output = ['I', 'the', 'like']

#dict.values()
print(word_counts.values()) # output = word_counts.values()
print(list(word_counts.values())) # output = word_counts.values()

print(word_counts) # output = {'I': 1, 'the': 3, 'like': 2}

print(word_counts.pop('the')) # output = 3
# or, word_counts.pop('the') then the next line execute of result. 
print(word_counts) # output = {'I': 1, 'like': 2}

word_counts['Aron'] = 2 # that's have added a dictionary
print(word_counts) # {'I': 1, 'like': 2, 'Aron': 2}
print(list(word_counts.values())) # output = [1, 2, 2]
print(sorted(list(word_counts.values()))) # output = [1, 2, 2] it can be sorted any key value pair of value in a ascending order. (Here list casting by sorted)
# print(word_counts.clear()) output = None
word_counts.clear()
print(word_counts) # output = {}
numbers = {
    1 : 'one',
    2 : 'two',
    3 : 'three', 
    4 : 'four',
    5 : "five", 
    6 : 'six'
}
print(numbers) # output = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
numbers.popitem()
print(numbers) # output = {2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

# more popItem check
choice = {
    'car' : 1,
    'bike' : 2,
    'cycle' : 0
}

print(choice)  # output = {'car': 9, 'bike': 2, 'cycle': 0}
choice.popitem()
print(choice) # output = {'bike': 2, 'cycle': 0}

# dict.clear()