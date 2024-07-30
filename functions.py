#add 2 nmbers with parameter and return value
'''
def add(n1,n2):
    sm=n1+n2
    return sm
a=int(input("enter first number "))
b=int(input("enter second number"))
r=add(a,b)
print(r)
'''
#without parameter and return value
'''
def add():
    a=int(input("enter first number "))
    b=int(input("enter second number"))
    s=a+b
    return s
i=add()
print(i)
'''
#without parameter and without return value
'''
def add():
    a=int(input("enter first number "))
    b=int(input("enter second number"))
    s=a+b
    print(s)
i=add()
'''
#with parameter and without return value
'''
def add(n1,n2):
    sm=n1+n2
    print(sm)
a=int(input("enter first number "))
b=int(input("enter second number"))
r=add(a,b)
'''
#local vs global variables
'''
n1=1122
def show():
    n1=2020
    n2=1011
    print(n1)
    print(n2)
show()
print(n1)
print(n2)
'''
'''
n1=1122
def show():
    global n2
    n2=2020
    n3=1011
    print(n1)
    print(n2)
    print(n3)
show()
print(n1)
print(n2)
print(n3)
'''
#calculator
'''
def add(n1,n2):
    res=n1+n2
    return res
def sub(n1,n2):
    res=n1-n2
    return res
def mul(n1,n2):
    res=n1*n2
    return res
def div(n1,n2):
    res=(n1//n2)
    return res
a=int(input("enter first number "))
b=int(input("enter second number"))
o=input("enter an operator (+,-,*,/) ")
if o=='+':
    r=add(a,b)
    print(f"{a} {o}  {b}= {r} ")
elif o=='-':
    r=sub(a,b)
    print(f"{a} {o}  {b}= {r} ")
elif o=='*':
    r=mul(a,b)
    print(f"{a} {o}  {b}= {r} ")
elif o=='/':
    r=div(a,b)
    print(f"{a} {o}  {b}= {r} ")
'''
#positional parameter
'''
def add(n1,n2):
    print(n1.upper(),n2)
a="kv"
b=1122
add(a,b)
'''
'''
def add(n1,n2):
    print(n1.upper(),n2)
a=1122
b="kv"
add(a,b)
'''
#keyword arguments
'''
def kw_ar(iv,fv,sv):
    print(iv,fv,sv)
kw_ar(iv=10,fv=10.5,sv="a")
kw_ar(fv=10.5,iv=1,sv="a")
kw_ar(sv="a",iv=10,fv=2.5)
kw_ar(i=10,f=10.5,s="a")
'''
#variable length arg
'''
def vl_ar(*arg):
    print()
    for i in arg:
        print(i,end=" ")
vl_ar(1122)
vl_ar(1122,2.5)
vl_ar(1122,2.5,'py')
'''
#variable length keyword arg
'''
def vl_ar(**kwarg):
    print()
    for n,v in kwarg.items():
        print(n,v,end=" ")
vl_ar(a=1122)
vl_ar(a=1122,b=2.5)
vl_ar(a=1122,b=2.5,c='py')
'''
#default arg
'''
def dis(name,course="btech"):
    print("name : "+name)
    print("course:",course)
dis(course="bca",name="arav")
dis(name="reyansh")
'''
#documentation string
'''
def cb(x):
    ''''''cube of  a number''''''
    print(x**3)
print(cb.__doc__)
cb(5)
'''
#passing lst tpl set to function
'''
def pca(m1,m2):
    print(m1,m2)
lst=[11,22,33,44]
tpl=(55,66,77)
pca(lst,tpl)
'''
#fun in fun
'''
def f1(x):
    return x+2
def f2(y):
    print(y)
f2(f1(5))
'''
#inner function
'''
def out():
    def inn():
        print("python")
    inn()
out()
'''
#recursive
#to find gcd
'''
def gcd_rec(n1,n2):
    if n2==0:
        return n1
    else:
        return gcd_rec(n2,n1%n2)
num1=48
num2=18
res=gcd_rec(num1,num2)
print(res)

'''
#gcd without recursive
'''
def gcd_rec(n1,n2):
    while n2:
        n1,n2=n2,n1%n2
    return n1
num1=48
num2=18
res=gcd_rec(num1,num2)
print(res)
'''
#factorial of a number using recursive
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=5
res=fact(num)
print(res)
'''
#fibonacci using recursion
'''
def fib(n):
    if n==1 or n==0 :
        return n
    else:
        return fib(n-1)+fib(n-2)
        
num=6
for i in range(num):
    print(f"%d"%(fib(i)))
'''
#filter function
'''
def evn_chck(n):
    return n%2==0
no=range(21,30)
evn_lst=list(filter(evn_chck,no))
print(evn_lst)
'''
#map()
'''
def sq(n):
    return n**2
no=[1,2,3,4,5]
sq_lst=map(sq,no)
print(list(sq_lst))
'''
#reduce() function
'''
from functools import reduce
def add(x,y):
    return x+y
num=[1,2,3,4,5]
res=reduce(add,num)
print(res)
'''
#
#
#module
#save with .py
'''
def n():
    print("name:-----")
def r():
    print("rno:---")
print(__name__)
n()
r()
'''
#math module 
'''
import math
print(dir(math))
'''
'''
import math
print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.floor(1122.45))
print(math.pow(2,8))
print(math.pi)
print(math.sqrt(36))
print(math.gcd(50,90))
'''
'''
from math import pi,e
print(pi)
print(e)
print(gcd(48,18))
'''
#time module
'''
import time
print(dir(time))
'''
'''
import time
print(time.gmtime())
print(time.localtime())
print(time.asctime())
print(time.strftime("%H:%M:%S"))
'''
#traffic signal
'''
import time
def trffc_sgnl():
    print("red light -stop!")
    time.sleep(10)
    print("yellow light -prepare to stop !")
    time.sleep(5)
    print("green light -gooo!")
    time.sleep(15)
for i in range(3):
    trffc_sgnl()
'''
#random module
'''
import random
print(dir(random))
'''
import random
'''
print(random.randint(11,22))
print(random.randint(11,22))
print(random.randint(11,22))
'''
#choice and shuffle
'''
lst=[10,20,30,40]
print(random.choice(lst))
random.shuffle(lst)
print(lst)
'''



