import re
ptrn = r"rain"
if (re.search(ptrn,"rain is reading")):
    print("match")
else:
    print("not matched")

if (re.match(ptrn,"rain is reading")): #match is only matching first word
    print("match")
else:
    print("not matched")

print(re.findall(ptrn,"rain is reading, rain is a good girl"))

text= "rain is reading, rain is a good girl"
match=re.search(ptrn,text)
if match:
    print(match.start())  #starting matching point
    print(match.end())    # ending matching point
    print(match.span())   # both starting and ending matching point

text2=re.sub(ptrn,"moon",text)
print(text2)