#read () function to read a file without paramenter
'''
f=open('bio.txt','r')
data=f.read()
print(data)
print("file read successfully")
f.close
'''
#read() with parameter
'''
f=open('bio.txt','r')
data=f.read(21)
print(data)
print("file read successfully")
f.close
'''
#readlines()
'''
f=open('bio.txt','r')
data=f.readlines()
print(data)
print("file read successfully")
f.close
'''
#readline()
'''
f=open('bio.txt','r')
data=f.readline()
print(data)
print("file read successfully")
f.close
'''
#write method
'''
f=open('fun2.txt','w')
data=f.write('manasaa na mata vinavaa,anju naku biryani petava')
f.close()
f=open('fun2.txt','r')
data=f.read()
print(data)
print("file read successfully")
f.close()
'''
#writelines() method
'''
f=open('fun1.txt','w')
lst=("manasaa na mata vinavaa \n","anju naku biryani petava")
f.writelines(lst)
f.close()
f=open('fun1.txt','r')
data=f.read()
print(data)
print("file read successfully")
f.close()
'''
#file object attributes
'''
f=open('bio.txt','r')
data=f.read()
print(f.name)
print(f.mode)
print(f.closed)
print(f.readable())
print(f.writable())
f.close()
f=open('bio.txt','r')
data=f.read()
print(data)
f.close()
print(f.closed)
'''
#opening file using with keyword
'''
with open('bio.txt','r') as f:
    data=f.read()
    print(data)
print("file closed:",f.closed)
'''
'''
with open('bio.txt','rb') as f:
    f.seek(-15,2)
    data=f.read(10)
    print(data)
'''
#tell() to find cursor position
'''
with open('bio.txt','rb') as f:
    f.seek(15,0)
    p=f.tell()
    print(p)
    data=f.read(10)
    print(data)
'''
#rename() method
'''
import os
os.rename('fun1.txt','fun.txt')
'''
#binary file reading
'''
with open('CHITTI.JPEG','rb') as f:
    data=f.read()
    print(data)
'''







