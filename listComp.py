names = ['Jenifer', 'Susan', 'Jane', 'Sophie']

l = []

for person in names:
    l.append(person)

print(l) # output = ['Jenifer', 'Susan', 'Jane', 'Sophie']

print([person for person in names]) # output = ['Jenifer', 'Susan', 'Jane', 'Sophie']

l = []
for person in names:
    l.append(person + ' dumped me. ')
print(l) # output = ['Jenifer dumped me. ', 'Susan dumped me. ', 'Jane dumped me. ', 'Sophie dumped me. ']


print([person + ' dumped me. 'for person in names]) # output = ['Jenifer dumped me. ', 'Susan dumped me. ', 'Jane dumped me. ', 'Sophie dumped me. ']

movie_and_ratings = {'Interstellar' : 9, "Dark Knight" : 8, "50 shades" : 3, "50 shades Darker" : 2, "50 shades Darkest" : 1}

l2 = []
for movie in movie_and_ratings:
    if movie_and_ratings[movie] > 6:
        l2.append(movie)
print(l2) # output : ['Dark Knight', 'Interstellar']

print([movie for movie in movie_and_ratings if movie_and_ratings[movie] > 6]) # output : ['Dark Knight', 'Interstellar']
