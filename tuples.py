t = (1, 2, 3)
print(t[1])

credit_card1 = (98765437654, "John", '24/24', 123)
credit_card2 = (98765437654, "John", '24/24', 123)

credit_cards = [credit_card1, credit_card2]
print(credit_cards)

person = ('Nancy-pants', 25, "pizza")
print(person)

name, age, favoriteFood = person #Or you can add this parenthesis like : (name, age, favoriteFood)
print(name)
print(age)
print(favoriteFood)

man1 = ('Denial', 45, 'mutton')
man2 = ('Walker', 35, 'chickken')
people = [man1, man2]

for name, age, favoriteFood in people : 
    print(name)
    print(age)
    print(favoriteFood)
    print # It's run correctly for new line.
    
