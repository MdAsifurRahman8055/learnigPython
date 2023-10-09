#TUPLES ARE ALMOST LIKE LIST BUT THE CATCH IS WE CAN'T CHANGE INSIDE TUPLES
#for triples we use first bracket
num=(
    "one",
    "two",
    "three",
    "four",
)
print(num[1])

#we can also add tuples into tuples

num=(
    ("one",1),
    ("two",2),
    ("three",3),
    ("four",4),
)
print(num[1][1])