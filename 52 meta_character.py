import re
ptrn = r"r..."  # "." is a meta character which helps in regular expression
if (re.match(ptrn,"rain is reading")):
    print("matched")
else:
    print("not matched")

import re
ptrn = r"^c.lo.r$"  #  "^__$" this character is to match first and last character of the string
if (re.match(ptrn,"colour")):
    print("matched")
else:
    print("not matched")

import re
ptrn = r"a{1,4}"  # "*"= 0 or more ,,, "+"= 1 or more ,,, "a+b"= ab ,,, "a*b"= a...b ,,, "?"= 0 or 1 ,,, "a{1,4}"= a must have among 1 to 4
if (re.search(ptrn,"rain")):
    print("matched")
else:
    print("not matched")

import re
ptrn = r"[A-Z]+[a-z]+[0-9]+"
if (re.match(ptrn,"Adda06")):
    print("matched")
else:
    print("not matched")