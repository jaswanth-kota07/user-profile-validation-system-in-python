#personilisation(if length of name is even first element from filtered lists is removed,else last element is removed)
name=input("Enter your name: ")
#taking input from user
n=int(input("Enter no of inputs:"))
data=[]
for i in range(n):
    scan=input("Enter input :")
    if scan.isdigit():
        data.append(int(scan))
    else:
        data.append(scan)
#applying filter to separate
numbers=[]
strings=[]
for item in data:
    if type(item)==int:
        numbers.append(item)
    else:
        strings.append(item)
if len(name)%2 == 0:
    numbers.pop(0)
    strings.pop(0)
else:
    numbers.pop()
    strings.pop()
#Output
print("Numbers list :",numbers)
print("Strings list :",strings)
print("Total numbers : ",len(numbers)+1)
print("Total strings : ",len(strings)+1)


