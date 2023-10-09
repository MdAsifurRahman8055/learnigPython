subjects=["physich","chemistry","math","biology"]# for list we use third bracket
#here subject is the main list
print(subjects[0])
print(subjects[-2])
print(subjects[2])
print(subjects[2:])
print(subjects*2)
print(subjects+['bangla'])

print('\n')

subjects=["physich","chemistry","math","biology"]
print(len(subjects))# length used to show how many subjects are in there
subjects=["physich","chemistry","math","biology"]
subjects.append('english')# append is to add extra subject on list
print(subjects)
subjects=["physich","chemistry","math","biology"]
subjects.insert(2,'bangla')# insert is to add subject on list on a specific place
print(subjects)
subjects=["physich","chemistry","math","biology"]
subjects.remove('math')#remove is to remove any subject
print(subjects)
subjects=["physich","chemistry","math","biology"]
subjects.sort()# sort is to sort subject in order//also we can't use anything inside sort bracket
print(subjects)
subjects=["physich","chemistry","math","biology"]
subjects.reverse()# it's opposite of sort//also we can't use anything inside sort bracket
print(subjects)
subjects=["physich","chemistry","math","biology"]
subjects.pop()#pop is to remove the last subject from list//also we can't use anything inside sort bracket
print(subjects)
subjects=["physich","chemistry","math","biology"]
subjects.clear()#to clear everything from list//also we can't use anything inside sort bracket
print(subjects)
subjects=["physich","chemistry","math","biology"]
sub2=subjects.copy()# to copy the list to another list//also we can't use anything inside sort bracket
print(sub2)
subjects=["physich","chemistry","math","biology"]
pos= subjects.index('math')# to find the position of any subject// also have to add on another variable
print(pos)
subjects=["physich","chemistry","math","biology",'biology','biology','biology']
count=subjects.count('biology')#to count how many times a subject in the list// also have to add on another variable
print(count)