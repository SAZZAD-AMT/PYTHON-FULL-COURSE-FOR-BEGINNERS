import re
pattern =r"colour"

if re.match(pattern,"Colour is a dam"):
    print("Match")
else:
    print("Not Match")

redd=r"colour"
if re.search(redd,"red is a colour,i love red colour"):
    print("Match")

print(re.findall(redd,"red is a colour,i love red colour"))
text=r"red is a colour,i love red colour"


match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

