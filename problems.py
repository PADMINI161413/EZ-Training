#vowel repetition problem -in given string find most  frequent vowel in the given str
'''
s=input()
mx=0
ans=0
d={'a':0,'e':0,'i':0,'o':0,'u':0}
for c in s:
    if c in d:
        d[c]=d[c]+1
        if mx<d[c]:
            mx=d[c]
            ans=c
    
print(d)
print(ans)
'''
'''
s=input()
v="aeiou"
mx=0
ans=0
d={}
for c in s:
    if c in v:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
        if mx<d[c]:
            mx=d[c]
            ans=c
    
print(d)
print(ans)
'''
#take input array size 6 and take array elements [11,21,32,45,1,23] and take input no.
#6 whose prime factors are to be found 6=2*3 pow of 2=1 and 3=1
#the output shd be sum=1*arr[2]+1*arr[3] ie 32+45=77
'''
s=int(input())
l=list(map(int,input().split()))
n=int(input())
def pf(n):
    i=2
    ans=[]
    while i<=n:
        if n%i==0:
            ans.append(i)
            n=n//i
        else:
            i=i+1
    return ans
ans=pf(n)
sm=0
for i in ans:
    sm=sm+l[i]
print(sm)
'''
#pizza -each frnd shd get equal pizza . so she shd call extra frnds who she get
#equal no.of pizza input=100 17 === op=2 ie sum of digits
'''
a,b=map(int,input().split())
ans=0
s=0
d=0
while True:
    if a%b==0:
        ans=b
        break
    else:
        b=b+1
while ans>0:
    d=ans%10
    s=s+d
    ans//=10
print(s)

'''
#take the size of arraya and array elements .such that the sum of rhs and sum of lhs
#must be same if it is return the equilibrium posityion else return middle element
#without using slicing operation
'''
s=int(input())
l=list(map(int,input().split()))
rs=0
ls=0
limit=0
sm=0
flag=0
for i in l:
    a=sum(l)
    limit=a//2
    for j in range(0,len(l)):
        if limit>sm:
            sm=l[j]+sm
            eq=j
            flag=1
        else:    
            mid=len(l)//2
            flag=0
if flag==1:            
    print(eq+1)
else:
    print(mid+1)
'''
# method 2 
'''
#a=[2,4,3,1,2,1,2,3]
#a=[5,2,1,3,1,2,5]
#a=[1,1,1,2,1]
a=list(map(int,input().split()))
f=0
for i in range(0,len(a)):
    i1=i
    j=i+1
    s1=0
    s2=0
    #left
    while i>=0:
        s1+=a[i]
        i=i-1
    while j<len(a):
        s2+=a[j]
        j=j+1
    if s1==s2:
        print(i1+1)
        f=1
        break
if f==0:
    print(len(a)//2+1)
'''    
#find a peak element in the given lsit of elements -there might be multiple peaks
#select the highest peak [1 3 2 20 4 6 5 1] = 3peaks 3 20 6 :op =20
'''
s=int(input())
l=list(map(int,input().split()))
mp=0
p=0
for i in range(1,len(l)-1):
    if (l[i-1]<l[i] ) and (l[i]>l[i+1]):
        p=l[i]
        if p>mp:
            mp=p
print(mp)
'''
#find the unique triplets. take input an array [5,3,20,10,1,4,2]
#and a product 60 the op shd be 3
#[5,4,3],[20,3,1],[10,3,2]==3 unique solutions
'''
s=int(input())
l=list(map( int,input().split()))
p=int(input())
tc=0
for i in range(s):
    for j in range(i+1,s):
        for k in range(j+1,s):
            if l[i]*l[j]*l[k]==p:
                print(l[i],l[j],l[k])
                tc+=1
print(tc)
'''
#hw == to solve the abv prblm without using 3rd for loop using sort







#contigious sub array with max sum
#kadanes algorithm
'''
n=int(input())
l=list(map(int,input().split()))
ms=0
cs=0
for i in l:
    cs=max(i,cs+i)
    ms=max(ms,cs)
print(ms)
'''
#target sum == to fnd the sum of the elements in the given list and return their index
'''
l=list(map(int,input().split()))
n=int(input())
l.sort()
r=0
i=0
j=len(l)-1
while i<j:
    r=l[i]+l[j]
    if  r==n:
        print(i,j)
        i+=1
        j-=1
    elif r>n:
        j=j-1
    else:
        i=i+1
'''
#minimum number of key presses 11 numeric keys (0,1,2,3,4,5,6,7,8,9.00)
'''

s=input()
c=0
pos=0
while pos<len(s)-1:
    if  s[pos]=='0' and s[pos+1]=='0':
        pos+=2
        c=c+1
    else:
        pos+=1
        c+=1
if pos<len(s):
    c=c+1  
print(c)
    
'''
#magic string ... take a string check which char is max and find the length of str
#if the count is more  the len of str-count is ans
'''
s=input()
d={}
mx=0
ans=0
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        if mx<d[i]:
            mx=d[i]
            
print(d)
print(mx)
res=len(s)-mx
print(res)
'''
#******************************************************************************
#missing alphabets :
'''
s=input()
v="abcdefghijklmnopqrstuvwxyz"
for i in v:
    if i not in s:
        print(i,end="")
'''
#take x and y 2 numbers such that y shd bcm 0 .if y =0 return x . else x<y interchange x and y
#else t=x-y and set x=y and y=t
'''
x=int(input())
y=int(input())
t=0
temp=0
while True:
    if x<y:
        temp=x #x,y=y,x
        x=y
        y=temp
    elif y==0:
        print(x)
        break
    elif x>=y:
        t=x-y
        x=y
        y=t
        '''

#fellis function using recurrsion
'''
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return f(n-1)+7*f(n-2)+(n//4)%(10**9+7)    
n=int(input())
print(f(n))
        
'''

#using for loop
'''
n=int(input())
lst=[1,1]
for i in range(2,n+1):
    ans=(lst[i-1]+7*lst[i-2]+i//4)%(10**9+7)
    lst.append(ans)
print(lst[n])
        
'''
#corner seat
'''
s=input()
l=list(map(str,input().split()))
n=l.index(s)
m=0
ans=0
#left
for i in range(0,n):
    if l[i]=="-":
        if abs(n-i)-1<m:
            m=abs(n-i)-1
#right
for i in range(n+1,len(s)):
    if l[i]=="-":
        if abs(i-n)-1<m:
            m=abs(i-n)-1
        
print(m)        
 '''
#spl fibbo
'''
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return (f(n-1)**2+(n-2)**2)%47    
n=int(input())
print(f(n))       
'''
# using for
'''
n=int(input())
lst=[1,1]
for i in range(2,n+1):
    ans=(lst[i-1]**2+(i-2)**2)%47
    lst.append(ans)
print(lst[n])
 '''
# maximiz sum product the sum of a pair shd be 18 and a>b and their product shd be greatest
'''
n=int(input())
l=list(map(int,input().split()))
l.sort()
mx=0
r=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]+l[j]==18:
            if l[i]>l[j]:
                r=l[i]*l[j]
                if mx<r:
                    mx=r
                    print(l[i],l[j])
'''
#give the minimum bitterness
'''
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=[]
for i in range(0,n):
        sm=a[i]+b[i]
        m.append(sm)
print(min(m))
'''                
#prefix and suffix:
'''
n=int(input())
l=list(map(int,input().split()))
ls=sum(l)
sm=0
res=[]
for i in range(0,n):
    sm=sm+l[i]
    ts=ls-sm
    res.append(abs(ts-sm))
print(res)    
'''        


'''
3 3 3 2 2 2 1 1 1 
3 3 2 2 1 1 
3 2 1
for i in range(3,0,-1):
    for j in range(3,0,-1):
        k=i
        while k>0:
            print(j,end=" ")
            k=k-1
    print()

'''
#***********************************************************************

#boring arrays u need to take the maximum sum from taking the differences bw the array ele
'''
n=int(input())
l=list(map(int,input().split()))
l.sort()
s=0
for i in range(0,n//2):
    s+=abs(l[i]-l[n-i-1])
print(s)
#5
#1 2 3 4 5
#6

'''
#using while
'''
l=list(map(int,input().split()))
l.sort()
s=0
lt=0
rt=len(l)-1
while lt<=rt:
    d=abs(l[rt]-l[lt])
    s=s+d
    lt+=1
    rt-=1
print(s)
'''

#basket ball
#5
#2
#1 2 3 4 5
#14
'''
n=int(input())
sz=int(input())
a=list(map(int,input().split()))
m=0
for i in range(0,len(a)-sz+1):#if we wont take it like this we get index out of range 
    temp=a[i:i+sz]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k=k+1
    if m<s:
        m=s
print(m)
'''

#a**2+b**2+ab+bc+ca=n
'''
n=int(input())
tc=0
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if (i**2+j**2+i*j+j*k+k*i)==n:
                tc+=1
                print(i,j,k)
                break
if tc>0:
    print(tc)
else:
    print("np")
'''
#6
#1 1 1
#1
#changed equation for 6
'''
n=int(input())
tc=0
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if (i**2+j**2+k**2+i*j+j*k+k*i)==n:
                tc+=1
                print(i,j,k)
                break
if tc>0:
    print(tc)
else:
    print("np")
'''    
#counting the number of commas
#not working for 10010000
'''
n=int(input())
c=0
for i in range(1,n+1):
    if i>=1000:
        s=len(str(i))
        t=s//3
        c=c+t       
print(c)
'''

'''
n=int(input())
c=1000
comma=1
res=0
while c<=n:
    m=c*1000
    num=min(n-c+1,m-c)
    res+=num*comma
    c=m
    comma+=1
print(res)
'''
#find the minimum ascii distance bw the numbers
'''
a=input()
s=input()
l1=[]
l2=[]
d=0
df=[]
m=9999
sm=0
for i in a:
    o1=ord(i)
    l1.append(o1)
for j in s:
    o2=ord(j)
    l2.append(o2)
print(l1)
print(l2)
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        d=l2[j]-l1[i]
        if d<m:
            m=d
            df.append(m)
print(df)
print(sum(df))
'''        
#without using lists
'''
a=input()
s=input()
m=9999
sm=0
for i in range(len(a)):
    for j in range(len(s)):
        d=abs(ord(a[i])-ord(s[j]))
        if d<m:
            m=d
            sm+=d
print(sm)
'''

#pyramid sum n=3 res=17
    #1
    #212
    #32123
    #:
    #n____212____n
'''
n=int(input())
s=0
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i,1,-1):
        print(k,end="")
        s=s+k
    for l in range(1,i+1):
        print(l,end="")
        s=s+l
    print()
print(s)

'''
'''
n=int(input())
o=1
res=0
s=0
for i in range(1,n+1):
    d=sum(range(2,i+1))
    s=o+2*d
    res+=s
print(res)
'''
#sirs solution
'''
row=int(input())
ans=0
for i in range(2,row+1):
    n=i
    while n>1:
        ans+=2*n
        n=n-1
ans+=row
print(ans)
'''
#andrews grade
'''
s=input()
pos=int(input())
step=int(input())
s1=list(s)
mini=999
start=0
end=len(s1)
if abs(pos-step-1)>=0:
    start=abs(pos-step-1)
if pos+step<len(s1):
    end=pos+step
print(start,end)
for i in range(start,end):
    mini=min(ord(s1[i]),mini)
store=s1[pos-1]
s1[pos-1]=s1[s1.index(chr(mini))]
s1[s1.index(chr(mini))]=store
print(mini)
print(chr(mini))
print(''.join(s1))
'''
'''
abcde
3
2
0 5
97
a
cbade
'''
#gcd lcm
'''
def gcd(n1,n2):
    if n2==0:
        return n1
    return gcd(n2,n1%n2)
num1=int(input())
num2=int(input())
res=gcd(num1,num2)
res2=num1*num2//res
print(res)
print(res2)
'''
'''
def gcd(n1,n2):
    while n2:
        n1,n2=n2,n1%n2
    return n1
num1=48
num2=18
res=gcd(num1,num2)
print(res)

'''
#robo problem
'''
x,m,y,n=map(int,input().split())
time=max(x,y)
while True:
    if time>=x and (time-x)%m==0 and  time>=y and (time-y)%n==0:
        print(time)
        break
    time+=1
'''
#Robo race
'''
X,N,Y,M=map(int,input().split())
l=1
while True:
    k=(Y+l*M-X)/N
    if k-int(k)==0:
        break
    l+=1
print(X+int(k)*N)
'''
#generating numbers---p&c
'''
n,a,b=map(int,input().split())
cnt=0
a1=n//a
b1=n//b
for i in range(a1+1):
    for j in range(b1+1):
        if a*i+b*j<10:
            cnt+=1
print(cnt)
#10 3 5
#6

 '''
#reversing a string
#using slice
'''
s=input().split()
a=s[::-1]
print(*a,sep="")
'''
'''
s=input()
a=s[::-1]
print(*a,sep="")
'''
'''
s=input()
s1=list(s)
n=len(s1)
for i in range(0,n//2):
    temp=s1[i]
    s1[i]=s1[n-i-1]
    s1[n-i-1]=temp  
print(''.join(s1))

'''
# remaining toys
'''
a,b=map(int,input().split())
print((a-b))
        
'''
#pattern
'''
for i in range(3,0,-1):
    for j in range(3,0,-1):
        k=i
        while k>0:
            print(j,end="")
            k=k-1
    print()
'''
#minimum in the list
'''
a=list(map(int,input().split()))
m=999
for i in range(0,len(a)):
    if a[i]<m:
        m=a[i]
print(m)
'''
#pattern
'''
****
*  *
*  *
****
'''
'''
for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
    *
   ***
  *****
 *******
'''
'''
for i in range(1,5):
    for j in range(5-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
'''




















































