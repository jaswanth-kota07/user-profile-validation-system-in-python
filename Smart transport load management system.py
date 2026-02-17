weights=input("enter your list: ").split()
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]
for i in weights:
    i=int(i)
    if i<0:
        invalid_entries.append(i)
    elif 0<=i<=5:
        very_light.append(i)
    elif 5<i<=25:
        normal_load.append(i)
    elif 26<=i<=60:
        heavy_load.append(i)
    else:
        overload.append(i)
name="Jashu"
l=len(name)
pli=l%3
total_valid=len(very_light)+len(normal_load)+len(heavy_load)+len(overload)
total_affected=0
if pli==0:
    invalid_entries+=overload
    total_affected+=len(overload)
    overload=[]
elif pli==1:
    total_affected+=len(very_light)
    very_light=[]
else:
    total_affected+=len(overload)+len(very_light)+len(invalid_entries)
    overload=[]
    very_light=[]
    invalid_entries=[]

print("total valid entries:",total_valid)
print("total affected:",total_affected)
print("L=",l)
print("PLI=",pli)
print("invalid entries:",invalid_entries)
print("very_light:",very_light)
print("normal:",normal_load)
print("heavy:",heavy_load)
print("overload:",overload)


