import re
pattern =r"colour"
text= r"my favorit colour is red and i love red colour"
text2=re.sub(pattern,"color",text,count=1)
print(text2)
