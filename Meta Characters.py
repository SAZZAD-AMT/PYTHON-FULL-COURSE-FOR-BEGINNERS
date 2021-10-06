import re
pattern =r"^col..r$"

if re.match(pattern,"colwwr"):
    print("Match")

pattern=r"a*"
if re.match(pattern,"colwwr"):
    print("Match")

pattern=r"a+" #a+b,a*b,a(1,3)$
if re.match(pattern,"colwwr"):
    print("Match")
else:
    print("Not match")

pattern=r"col(-)?our"
if re.match(pattern,"colour"):
    print("Match")
