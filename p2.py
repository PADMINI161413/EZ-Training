#ant on rail
'''
n=int(input())
c=0
a=0
m=list(map(int,input().split()))
for i in m:
    c=c+i
    if c==0:
        a=a+1
print(a)
'''
# chocolate jar how many chocolates will a get
'''
n=list(map(int,input().split()))
s=int(input())
r=0
a=0
t=0
for i in range(len(n)):
    if n[i]%3==0:
        a=n[i]//3
        t=t+a
    if n[i]%3!=0:
        r=n[i]//3
        a=r+1
        t=t+a
print(t)
'''
#dogs age 1 dog year=7 human year
'''
n=int(input())
a=n*7
print(a)
'''
#diwali prblm max has 4hrs time ip is no.of prblms and time to travel
'''
p=int(input())
t=int(input())
tl=240-t
n=0
rem=0
for i in range(1,p+1):
    rem=5*i+rem
    a=tl-rem
    if a>=0:
        n=i
print(n)
'''
'''
p=int(input())
t=int(input())
rt=240-t
c=0
s=0
for i in range(0,p):
    s=s+5*i
    if s>rt:
        break
    c=c+1
print(c)
'''

#basket ball problem input should be given as no.of shots played by player and size of array
# and the array of integers .
#5
#2
#1 2 3 4 5
#by the given size divide the array and multiply the array ele with the position 
'''
goal=int(input())
size=int(input())
arr=list(map(int,input().split()))
mx=-1
for i in range(0,len(arr)-size+1):
    temp=arr[i:i+size]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k+=1
    if s>mx:
        mx=s
print(mx)
'''
#space counter
#without using split
'''
s=input()
count=0
for i in s:
    if i==' ':
        count=count+1
print(count)
'''
#with split
'''
s=input()
h=s.split()
print(len(h)-1)
'''
#encode the num you need to square and concat them whitout using str
'''
n=167
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    return c
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
ans=rev(n)
def rev2(n):
    ans2=0
    while n>0:
        digit=n%10
        ans2=ans2*10+digit
        n//=10
    return ans2
print(rev2(ans))
'''
# farthest distance
'''
n=list(map(int,input().split()))
m=0
s=0
for i in n:
    s=s+i
    if s>m:
        m=s 
print(m)
'''
#encodinga number
'''
def en(n):
    result = 0
    factor = 1    
    while n > 0:
        digit = n % 10
        squared = digit * digit       
        if squared < 10:
            result = squared * factor + result
            factor *= 10
        else:
            result = squared * factor + result
            factor *= 100
        n //= 10
    return result
n = int(input())
en = en(n)
print(en)  
'''
#fing the minimum average of the given list which can happen only when the list is
#sorted and without usingsort remove pop find the largest and second largest numner
#from the given list
'''
l=list(map(int,input().split()))
m1=0
m2=0
s=0
avg=0
for i in l:
    if m1<i:
        m2=m1
        m1=i
    elif i>m2:
        m2=i
print(m1)
print(m2)
avg=(m1+m2)//2
for j in l:
    if j>avg:
        s=s+j
print(s)

'''
#with 2 for loops
'''
l=list(map(int,input().split()))
m1=0
m2=0
s=0
avg=0
for i in l:
    if m1<i:
        m1=i
for  k in l:
    if k>m2 and k<m1: 
        m2=k
print(m1)
print(m2)
avg=(m1+m2)//2
for j in l:
    if j>avg:
        s=s+j
print(s)
'''
#toss the coin h=2 t=-1 game will end if 3 consecutive heads or input has only tails
'''
s=input()
ch=0
ct=0
sm=0
for i in s:
    if i=='h':
        ct=0
        ch=ch+1
        sm=sm+2
    elif i=='t':
        ch=0
        ct=ct+1
        sm=sm-1
    if ch==3 or ct==3:
        break
print(sm)
'''
# find missing and repeated values 2d list with size n such that the numbers in that will be from
#1-n**2 such that 1 number will be repeated and the other number wil be missing
'''
a=[]
d={}
ans=[]
r=3
c=3
rep=0
for i in range(0,3):
    sub=[]
    for j in range(0,3):
        ele=int(input())
        sub.append(ele)
    a.append(sub)
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(ans)
'''
#encrypting number x=123 with largest digit that is 333 and find the sum of those numbers
#[10,20,30]= 11+22+33=66
n=list(map(int,input().split()))
def encrypt(a):
    mx=0
    c=0
    ans=0
    temp=a
    while temp>0:
        d=temp%10
        if d>mx:
            mx=d
            c=c+1
        temp=temp//10
    while c>0:
        ans=ans*10+mx
        c=c-1
    return(ans)
for i in range(0,len(n)):
    res=encrypt(i)
print(res)
        
        






