lst = [1, 2, 3, 4, 6, 7]

print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
print(lst[5])


list_in_different_data_types = [1, "string", True, [1, 2, 3, ]] # It's a valid list.
print(list_in_different_data_types)
print(list_in_different_data_types[0])
print(list_in_different_data_types[1])
print(list_in_different_data_types[2])
print(list_in_different_data_types[3])

names = ["Joe", "John", "James"]
print(names)

#names.append("Doe")
names.insert(0, "insertElementAdded")
print(names)
names.remove(names[0]) # remove first element of the list
print(names)
names.remove("John") #remove the individual element of the list
print(names)

reverseCheck = [1, 2, 3, 4, 5]
reverseCheck.reverse()
print(reverseCheck)

numbers = [4, 2, 6, 8, 2, 7, 8]
numbers.sort()
print(numbers)

for number in numbers :
    print(number)