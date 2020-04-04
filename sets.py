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