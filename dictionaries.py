groceries = {'bananas' : 5, 'oranges' : 3} # here some key value pair
print(groceries['bananas']) # output = 5
print(groceries.get('bananas')) # output = 5
print(groceries.get('hello')) # output = None

contacts = {
    'john' : '4567-890',
    'jane' : '45678-80'
}

print(contacts['john'])