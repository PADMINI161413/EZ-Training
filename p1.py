#calculate the sum of numbers whose length is the power of length armstrong of number
'''n=int(input())
b=(str(n))
a=len(b)
sum=0
for i in range(0,n):
    rem=n%10
    p=rem**a
    sum=sum+p
    n=n//10
print(sum)'''

'''
n=int(input())
b=n
org=n
count=0
while b>0:
    b=b//10
    count=count+1
print(count)
sum=0
for i in range(0,n):
    rem=n%10
    p=rem**count
    sum=sum+p
    n=n//10
print(sum)
if sum==org:
    print("armstrong number")
else:
    print("not an armstrong number")
'''
'''
n=int(input())
count=0
b=n
org=n
while b>0:
    b=b//10
    count=count+1
print(count)
sum=0
while n>0:
    rem=n%10
    p=rem**count
    count=count-1
    sum=sum+p
    n=n//10
print(sum)
'''
#chessboard
'''
e_r='aceg'
o_r='
n=input("enter the coordinates ")
if n[0] in e_c:
    if s[1] in e_r:
        print(" black ")
    else :
        print("white")
else:
    if s[1] in e_r:
        print("black")
    else:
        print("white")
'''
#getting the 0s at the end and non 0s front
'''
b=[]
n=int(input("size "))
for i in range(0,n):
    a=int(input())
    b.append(a)
for i in range(len(b)):
    if b[i]==0:
        b.append(b[i])
        del(b[i])
print(b)
'''
#getting the 0s at the end and non 0s front w/o using 2 for and no 2 lists
'''
b=[]
j=0
n=int(input("size "))
for i in range(0,n):
    a=int(input())
    b.append(a)
for i in range(len(b)):
    if b[i]!=0:
        b[j]=b[i]
        j=j+1
while j<n:
    b[j]=0
    j=j+1
print(b)
'''
#recurrsion
'''
def sq(n,p):
    if p==0:
        return 1
    else:
        return n*sq(n,p-1)
n=int(input())
p=int(input())
print(sq(n,p))
'''
#sum of digits of a no. using recurrsion
'''
def sd(n):
    if n==0:
        return 0
    else:
        rem=n//10
        return n%10+sd(n//10)
n=int(input())
print(sd(n))
'''
# class object self constructor and parameterized constructor
'''
class cse1:
    def __init__(self,a,b):#parameterized constructor
        self.a1=a
        self.b1=b
        print("im constructor")
    def strength(self):
        print("the strength is 101")
        self.s=101
    def kn(self,c,d):
        print("the knowledge is good")
        self.know="excellent"
        pro=c*d
        print(pro)
    def details(self):
        print("the current strength and knowledge")
        c_s=self.s-11
        print(c_s,self.know)
        print(self.a1+self.b1)
d=cse1(20,30)
print("the functions are called now")
d.strength()
d.kn(3,5)
d.details()
'''
#inheritance
#single level
'''
class Faculty:#parent class
    def __init__(self,name,dept,fid):
        self.name=name
        self.dept=dept
        self.fid=fid
    def print_info(self):
        print("faculty info=",self.name,self.dept,self.fid)
obj=Faculty("a","cs",1)
obj.print_info()
class cse(Faculty):#child class
    pass
obj1=cse("b","ai",2)
obj1.print_info()
'''
#------------------------------------------
#multi level
'''
class gp:
    def gpa(self):
        print("grandfather")
        self.a=10
    def fun1(self):
        print("father")
        self.b=20
    def fun2(self):
        print("child")
        pro=self.a*self.b
        print(pro)
obj=gp()
def.

'''
#multiple
'''
class sub:
    math=int(input("enter marks"))
    eng=int(input("enter marks"))
    c=int(input("enter marks"))
class pmark:
    cpract=int(input("enter c practical marks"))
class res:
    def tot:
        if self.math>=40 and self.eng>=40 and self.c>=40 and self.cpract>=50:
            print("pass")
        else :
            print("fail")
o1=sub()
'''
#sorting without using sort
'''
lst=[2,1,0,1,1,2,0,0]
lst.sort()
print(lst)
'''
'''
lst=[2,1,0,1,1,2,0,0]
count0=0
count1=0
count2=0
for i in range(len(lst)):
    if lst[i]==0:
        count0=count0+1
    elif lst[i]==1:
        count1=count1+1
    elif lst[i]==2:
        count2=count2+1
print(count0)
print(count1)
print(count2)
j=0
while count0>0:
    lst[j]=0
    j=j+1
    count0-=1
while count1>0:
    lst[j]=1
    j+=1
    count1-=1
while count2>0:
    lst[j]=2
    j+=1
    count2-=1
print(lst)
'''
#create a class car_showroom in which -
#1.create a function named car_company which will allow user to select a car company out of the displayed companies.
#if the user enters any random car company he/she should be asked to re enter
#2. accdng to the car company selected the user should be redirected to selecting the models
#of that company out of the given list. if anything other than list is entered renter
#3.after selecting the model the user should be redirected to selecting the variant(petrol/diesel).
#4.according to the car company model and variant a price should be calculated to which sgst and cgst are added to make it the total price.
#note::sgst and cgst are common for all the cars .
'''
class car:
    def __init__(self):
        self.cgst = 5555
        self.sgst = 5555
        self.insurance = 5555
    def company(self):
        while True :
            print("Toyota,Mercedes")
            self.n = input("enter the car company")
            if self.n=="Toyota":
                print("Welcome to toyo")
                self.model()
                break
            elif self.n == "Mercedes":
                print("Welcome to merc")
                self.model()
                break
            else:
                print("enter valid company")
    def model(self):
        if self.n=="Toyota":
            while True:
                print("select from fortuner and LC")
                self.choice = iput("Enter the car model")
                if self.choice == "Fortuner":
                    self.price(self.choice)
                    break
                elif self.choice == "LC":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid")
        elif self.n=="Mercedes":
            while True:
                print("Select from amg and gw")
                self.choice = input("Enter the car model")
                if self.choice =="amg":
                    self.price(self.choice)
                    break
                elif self.choice == "gw":
                    self.price(self.choice)
                    break
                else:
                    print("enter vaild")
    def price(self,choice):
        if choice=="Fortuner":
            self.p = 4500000
        elif choice=="LC":
            self.p = 1000000
        elif choice=="amg":
            self.p = 24432874
        elif choice=="gw":
            self.p = 843726837
        tot_p = self.p + self.sgst + self.cgst + self.insurance
        print(tot_p)
c = car()
c.company()
'''

#find the next greater value for every element [14,2,16,4,3,5] if not greater than that number return -1 solve this using stacks                       
'''
def ne(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
nums = [14, 2, 16, 4, 3, 5]
print(ne(nums))
'''
#you are the head of election committee in ur village.each political party
#is if 2 partie shave same no. of vote then return -1 else print the majority
#if only 1 party is there print its vote
'''
d={}
n=int(input())
a=list(map(int,input().split()))#to take the input in same line 
if len(a)==0:
    print(a[0])
else:
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
ans=-1
vals=list(d.items())
print(vals)
vals.sort(reverse=True,key=lambda x:x[1])
print(vals)
if vals[0][1]==vals[1][1]:
    ans=-1
else:
    ans=vals[0][0]
print(ans)
'''
#find a prime no. which is next no.of the given number and smallest prime number
'''
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i)==0:
            return False
    return True
n=int(input())
k=n+1
while True:
    if isprime(k):
        print(k)
        break
    k=k+1
'''
'''
def isprime(n):
    i=2
    if n<=1:
        return False
    else:
        while((i*i)<n):
            if n%i==0:
                return False
            i+=1
        if((i*i)>n):
            return True
num=int(input())
i=num+1
while i>num:
    if(isprime(i)):
        print(i)
        break
    i+=1
'''

'''
n=int(input())
k=22
for i in range(0,n+1):
    print(n)
    n=n+k
    k=k+16
 '''
'''
a=2
b=3
n=int(input())
for i in range(0,n+1):
    n=a*b
    print(n)
    a=a+2
    b=b+4

'''
#[12,14,2,16,5,3]
#find next smaller
#find previous greater
#find previous smaller
'''
#next smaller
def ne(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] <= nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
nums = [12,14,2,16,5,3]
print(ne(nums))
'''
'''def psmall(a):
    stack=[]
    res=[]
    for n in a:
        while stack and stack[-1]>=n:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(n)
    return res
n= [12,14,2,16,5,3]
print(psmall(n))'''
            
#prev greater
'''
def pgreater(a):
    stack=[]
    res=[]
    for n in a:
        while stack and stack[-1]<=n:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(n)
    return res
n= [12,14,2,16,5,3]
print(pgreater(n))
'''
#largest area of the rectangle wrt the adjacent rectangle values











    


        
        
