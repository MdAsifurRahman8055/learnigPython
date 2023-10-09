books=[]  #blank list

#to add on list
books.append('bangla')
books.append('english')
books.append('physics')
books.append('chemestry')

print(books)

#to remove from list
books.pop()  #here last to enter first to out
print(books)

books.pop()
print("books left:",books)

print("the top book is;",books[-1])
if not books:
    print('no books left')
