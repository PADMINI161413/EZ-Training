'''
l=[11,22,'k','v',"pup",True,65.77]
print(l)
print(type(l))
print(l[0])
print(l[2])
print(l[-1])
print(l[-2])
ls=[11,22,33,[444,55,66],77,88]
print(ls[-3])
'''

'''
print(len(l))
print(min(l))
print(sum(l))
print(any(l))
print(all(l))
lst=sorted(l)
print(lst)
r=list(reversed(l))
print(r)
'''
'''
l=[11,22,33,66,0]
l.append(77)
print(l)
'''
'''
l=[11,22,33,66,0]
l.insert(25,'k')
print(l)
'''
'''
l=[11,22,33,66,0]
l.pop(30)
print(l)
'''
'''
l=[11,22,33,66,0]
l.reverse()
print(l)
'''
'''
k=[11,22]
v=[33,44]
v.extend(k)
print(v)
'''
'''
l=[11,22,33,66,0]
l.remove(11)
print(l)
'''
'''
l=[11,22,33,66,0]
l.reverse()
print(l)
'''
'''
l=[11,22,33,66,0]
l.clear()
print(l)
'''
#gives all the methods and attributes of list
'''
print(dir(list))
'''
'''
k=[]
print(help(k.append))
'''
#
'''
l=[11,22,33,66,0]
for i in l:
    print(i,end=" " )
'''
'''
l=[11,22,33,66,0]
i=0
while i<len(l):
    print(l[i],end=" ")
    i=i+1
'''
'''
l=[11,22,33,66,0]
for i in range(len(l)):
    print(l[i],end=" " )
'''
'''
l=[11,22,33,66,0]
for i,j in enumerate(l):
    print(i ,j )
'''
'''
l=[11,22,33,66,0]
d=[i**2 for i in l]
print(d)
'''
'''
l=[-11,22,-33,66,0]
d=[i for i in l if i>0]
print(d)
'''
'''
l=[11,22,33,66,0]
d=[i for i in l if i%2!=0]
print(d)
'''
'''
k=[]
n=int(input("enter the size of list "))
for i in range(n):
    l=int(input("enter the %i element"%(i+1)))
    k.append(l)
print(k)
 '''
'''
k=[]
n=int(input("enter the size of list "))
for i in range(n):
    l=int(input("enter the %i element"%(i+1)))
    k.append(l)
print(k)
pos=int(input("enter the position"))
rs=k[-pos:]+k[:-pos]
print(f"right rotated list:{rs}")
ls=k[pos:]+k[:pos]
print(f"left rotated list:{ls}")
'''
'''
k=[11,22,11,33,11,44,11,55]
unq=[]
for i in k:
    if i not in unq:
        unq.append(i)
print(k)
print(unq)
 '''


