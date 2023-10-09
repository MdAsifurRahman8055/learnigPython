file= open("roll-name.txt","r+")  # w- writtimg , r- reading ,r+ - reading+writting
#print(file.readable())
text=file.readlines()

print(text)
print(len(text))

for line in text:
    print(line)
file.close()