# Email Address Text Scraper

import re # re = Regular Expression

text = "A random string."

pattern = re.compile("A random string.")

result = pattern.search(text)
print(result)

pattern2 = re.compile("[abc]")
result2 = pattern2.search(text)
print(result2)

pattern3 = re.compile("[a-zA-Z0-9]+")
result3 = pattern3.search(text)
print(result3)

emailAddress = "sohan110111@gmail.com"
pattern4 = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result4 = pattern4.search(emailAddress)
print(result4)

