problems = 'broke, pale, short, nerdy'
print(problems)

li = problems.split(", ")
print(li)
print(problems.split('short'))

joined = ' and '.join(li)
print(joined)

csv = ', ' .join(li)
print(csv)