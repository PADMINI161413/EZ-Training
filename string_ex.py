
'''
s="welcome to python programming"
print(s.split())
print(s.partition("python"))
print("-".join(s))
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())
'''
#to print all asci values 
'''
for i in range(1,128):
    print(chr(i),end=" ")
'''
#to print uc
'''
for i in range(65,91):
    print(chr(i),end=" ")
'''
#to print lc
'''
for i in range(97,123):
    print(chr(i),end=" ")
'''
'''
n=input("enter ur name")
for i in n:
    print(i,"-",ord(i),end=" ")
'''
#to replace 1st letter with $
'''
n=input("enter ur name")
fc=n[0]
r=fc+n[1:].replace(fc.lower(),"$").replace(fc.upper(),"$")
print(r)
'''
#add ing at the end of the word if it already has ing add ly if len<3 leave
'''
n=input("enter a string ")
f=len(n)
if f<=2:
    print(n)
elif n.endswith("ing"):
    print(n+"ly")
else:
    print(n+"ing")
'''
#replacing in above
'''
n=input("enter a string ")
r,t="ing","ly"
f=len(n)
if f>3 and n.endswith(r):
    print(n[:-3]+t)
else:
    print(n if f<=3 else n+r)
    '''
'''
s=input("enter a string : ")
word=s.split()
max_len=0
for i in word:
    if len(i)>max_len:
        max_len=len(i)
        long=i
print(f"longest word in string {long} and its length is {max_len}")
'''
#exchange 1st and laast char of str
'''
s=input("enter a string ")
if len(s)>=2:
    ns=s[-1]+s[1:-1]+s[0]
    print("modified string is :",ns)
else:
    print("string is too short")

'''
#to remove odd index value char in str
'''
s=input("enter a string :  ")
ns=s[::2]
print(ns)

'''
#ask input only if user enter quit then quit the prgm
'''
while True: 
    s=input("enter a string ")
    if s.upper()=='QUIT':
        print("exiting the program")
        break
    l=len(s)
    print("the length of the string is ",l)
'''
#to take 5 words frm user if len<6 ask again else print
'''
for i in range(5):
    while True :
        s=input("enter word %d "%(i+1))
        if len(s)<6:
            print("please enter it again")
        else:
            print(s)
            break
'''

      
        
    






