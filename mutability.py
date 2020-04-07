# mutability that means mutate ability or basically change ability 
# mutability = changeable 
# immutability = unchangeable
# lists is the best example for mutable
# on the otherhand tuples is for immutable

# immutate 
    # tuples
    # int, float, boolean
# least things are immutable
# this allow for secure data

# mutable
    # list 
    # dictionaries
    # orderedDict
# most things are mutable
# this allow for flexible data

t = (1, 2, [1, 2, 3])
print(t) # output = (1, 2, [1, 2, 3])

t[2][0] = 7
print(t) # output = (1, 2, [7, 2, 3])