'''
for i in range(5):
    print(i,end=' ')
    '''
'''
for i in range(10,16):
    print(i,end=' ')
print(i)
'''
'''
for i in range(11,22,4):
    print(i,end=' ')
'''
'''
for i in range(22,11,-4):
    print(i,end=' ')
'''
#to read input and print using for
'''
a=int(input("start"))
b=int(input("end"))
for i in range(a,b+1)or range(b,a+1):
    print(i,end=' ')
'''
#take input of numbers and print its avg
'''
n=int(input("enter no."))
sum=0
for i in range(n):
    a=int(input("enter number %d " %(i+1)))
    sum=sum+a
avg=sum//n
print("average is :",avg)
print(f"the avg of {n} numbers is :{avg:.2f}")#string formatting 
'''
#print odd numbers
'''
x=int(input("from "))
y=int(input("to "))
for i in range(x,y):
    if i%2!=0:
        print(i,end=' ')
        '''
#multipilication tabel
'''
n=int(input("enter num"))
for i in range(1,10+1):
        #print(n,"* %2d"%i,"=","%2d"%(n*i))
 '''
#sum of digits of a number
'''
num= int(input("Enter a number: "))
sum= 0
for i in str(num):
    #if i>='0' or i<='9':
        sum=sum+int(i)
#print("The sum of digits in the number is:",sum )
print(f"the sum of the digits of {num} is :{sum}")
'''
#prime number or not
'''
num=int(input("enter a number : "))
cnt=0
for i in range(2,num):
    if num%i==0:
        cnt=cnt+1
if cnt==0:
    print(" prime number")
else:
        print("not a prime  number")
        '''
#prime number using boolesn
'''
num=int(input("enter a number : "))
if num<=1:
    is_prime=False
else:
    is_prime=True
    for i in range(2,num):
     if num%i==0:
        is_prime=False
        break
if is_prime:
    print(" prime number")
else:
        print("not a prime  number")
        '''
#factorial of a number
'''
import sys
n=int(input("enter a number"))
f=1
if n<0:
    print("factorial is not defined for negative number")
    sys.exit()
else:
    for i in range(1,n+1):
     f=f*i
print(f"the factorial of {n} is :{f}")
'''
#reverse a number and palindrome
'''
n= int(input("Enter a number: "))
rev=0
temp=n
n_str=str(n)
d=len(n_str)
for i in range(d):
        rem=n%10
        rev=rev*10+rem
        n=n//10    
print(f"the rev of the number {temp} is {rev}")
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")
'''
#fibbo
'''
n= int(input("Enter a number: "))
f,s=0,1 #tuple
print("fibonacci series are : ")
if n==1:
    print(0)
elif n==2:
    print(1)
else:
    for i in range(n):
        print(f,end=" ")
        f,s=s,f+s
'''
#rev num using while and palindrome
'''
rev=0;
n=int(input("enter number"))
temp=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")
'''
