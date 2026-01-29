import sys

fullname=input("Enter your full name: ")
email=input("Enter your email: ")
mobile=input("Enter your mobile number: ")
age=int(input("Enter your age: "))

#Full name validation
if fullname[0]==" " or fullname[-1]==" ":
    print("user profile invalid")
    sys.exit(1)
list=fullname.split(" ")
if len(list)!=2:
    print("user profile invalid")
    sys.exit(1)
elif list[0].strip()==" " or list[1].strip() == " ":
    print("user profile invalid")
    sys.exit(1)

#email validation
dot_check=False
a_check=False
for i in email:
    if i==".":
        dot_check=True
    if i=="@":
        a_check=True

if email[0] == "@" or not dot_check or not a_check:
    print("user profile invalid")
    sys.exit(1)

#Mobile number validation

if len(mobile) != 10 or mobile[0] == '0' or not mobile.isdigit():
    print("user profile invalid")
    sys.exit(1)

#Age validatio

if age < 18 or age> 60 :
    print("user profile invalid")
    sys.exit(1)

print("user profile valid")
print("Login successful...")


