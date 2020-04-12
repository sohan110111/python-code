# Email Address Text Scraper

import re # re = Regular Expression

text = "A random string."

pattern = re.compile("A random string.")

result = pattern.search(text)
print(result) # output = <_sre.SRE_Match object at 0x0000000003475F10>

pattern2 = re.compile("[abc]")
result2 = pattern2.search(text)
print(result2) # output = <_sre.SRE_Match object at 0x00000000034765E0>

pattern3 = re.compile("[a-zA-Z0-9]+")
result3 = pattern3.search(text)
print(result3) # output = <_sre.SRE_Match object at 0x0000000003476570>

emailAddress = "sohan110111@gmail.com"
pattern4 = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result4 = pattern4.search(emailAddress)
print(result4) # output = <_sre.SRE_Match object at 0x0000000003476650>

text2 = "random string. MyName123@website.com . some more random text. Your-Name.8_8_8@company.net"
pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result5 = pattern.findall(text2)
print(result5) # output = ['MyName123@website.com', '8_8_8@company.net']
