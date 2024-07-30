'''    Problem Statement:

    You are given a string S representing the colours of houses (red(R), blue(8) or white(W)).
    The badness value is the number of differently-coloured adjacent houses.
    You can paint the white houses red or blue to minimize the badness value.
    Your task is to find and return an integer value representing the minimum possible badness value.
    Input Specification:input1: A string value S, representing the colours of houses
    Output Specification:Return an integer value representing the minimum possible badness value.
    try to change white house with prev house colour
    www====0
    rrwrbwbw====rrrrbbbb=1 only 1 change
'''
'''
s=list(input())
for i in range(0,len(s)):
    if s[i]=='w':
        if i==0:
            for j in range(1,len(s)):
                if s[j]!="w":
                    s[i]=s[j]
                    break
        else:
            s[i]=s[i-1]
bad=0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        bad+=1
print(bad)
'''
'''
12     15      minimum no that you have to add to make the given number symmetric

1100--->1111
finding the symmetric number
+3   A symmetrical number is nothing but whose binary number contains all 1's
'''
'''
n=int(input())
sym_num=0
pov=0
temp=n
while (temp>0):
    sym_num+=(2**pov)
    temp=temp//2
    pov+=1
print(sym_num)
print(sym_num-n)
'''
'''
Problem Statement: A person's body mass index is a simple calculation based on height and
weight that classifies the person as underweight, overweight, or normal.

The formula for the metric unit is, BMI = weight in kilograms/ (height in meters)^2

You are given an integer weight and a floating-point number height of a person as input.
Calculate the BMI of the person and print the person's BMI category as per the given rules:

1. IF BMI < 18, print 0.

2. If 18 <= BMI < 25, print 1.

3. IF 25<=BMI < 30, print 2.

4. If 30 <= BMI < 40, print 3.
5. If BMI>= 40, print 4.

Note:

The unit of weight is Kilogram.

The unit of height is meter
Compute BMI as a floating-point.

Pytha

1

2

Input Format:

Each test case consists of two lines of input

The first line of input contains an integer. i.e. weight in kilograms.

the second line contains a float number, i.e, height in meters.

Input will be read from the STDIN by the candidate

Sample Input:

60

1.75

Sample Output:

1



wt=int(input())
ht=float(input())
bmi=wt/(ht**2)
if bmi<18:
    print(0)
elif bmi>=18 and bmi<25:
    print(1)
elif bmi>=25 and bmi<30:
    print(2)
elif bmi>=30 and bmi<40:
    print(3)
elif bmi>=40:
    print(4)
'''

'''
#mine
You are given an integer array A of size N. Your task is to find and return
an integer value representing the product of all the elements in the array

Input Specification:

inputl: An integer array A

input2: An integer value N representing the size of the array

Output Specification:

Return an integer value representing the product of all the elements in the array.

l=list(map(int,input().split()))
c=1
for i in l:
    c=c*i
print(c)
'''
#sir
'''
l=list(map(int,input().split()))
c=1
for i in l:
    if i==0:
        c=0
        break
    c=c*i
print(c)
'''
'''
0       
1 1     
2 2 2   
3 3 3 3

n=int(input())
for i in range(n):
    for j in range(n):
        if j<=i:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
Problem Statement:

You have been given an integer N as input. Your task is to write a program to print N rows of Floyd's Triangle pattern.
Floyd's Triangle is a right-angled triangular array of natural numbers, used for the numbering of lines in a printout.

Sample Input:

4

Sample Output:
1       
2 3     
4 5 6   
7 8 9 10

n=int(input())
start=1
for i in range(n):
    for j in range(n):
        if j<=i:
            print(start,end=" ")
            start=start+1
        else:
            print(" ",end=" ")
    print()
'''
'''
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
n=int(input())
for i in range(n):
    for j in range(n):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
'''
A         
B C       
D E F     
G H I J   
K L M N O 
n=int(input())
start="A"
for i in range(n):
    for j in range(n):
        if j<=i:
            print(start,end=" ")
            start=chr(ord(start)+1) # ascii value
        else:
            print(" ",end=" ")
    print()
'''
'''
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * * * 
n=int(input())
for i in range(n):
    for j in range(2*n-1):
        if i+j==n-1 or j-i==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

#ELECTIONS
n=int(input())

arr=list(map(int,input().split()))

d={}

if n==1:

    print(arr[0])

else:

    for num in arr:

        if num not in d:

            d[num]=1

        else:

            d[num]+=1

    x=sorted(d.items(),key=lambda x:x[1],reverse=True)

    if x[0][1]==x[1][1]:

        print(-1)

    else:

        print(x[0][0])

#ELECTIONS WITHOUT USING LAMBDA
n=int(input())
arr=list(map(int,input().split()))
d={}
for num in arr:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1
max_val=0
for key in d:
    if d[key]>max_val:
        max_val=d[key]
winner=[]
for key in d:
    if d[key]==max_val:
        winner.append(key)
if len(winner)>1:
    print(-1)
else:
    print(winner[0])

#DIWALI PARTY
N=int(input())
P=int(input())
time_left=4*60-P
i=1
problems=0
while(time_left>=5*i):
    time_left=time_left-5*i
    problems+=1
    i+=1
print(min(N,problems))


#object score

N,M=map(int,input().split())
capacity=list(map(int,input().split()))
items=[]
for _ in range(M):
    items.append(list(map(int,input().split())))
items.sort()
res=[]
for cap in capacity:
    total=0
    for item in items:
        if cap<item[0]:
            break
        else:
            total+=item[1]
    res.append(total)
print(*res,sep=" ")
has context menu


#equlibrium
n=int(input())
arr=list(map(int,input().split()))
equillibrium=0
for i in range(0,n):
    if sum(arr[:i])==sum(arr[i+1:]):
        equillibrium=i+1
        break
if equillibrium==0:
    print("NOT FOUND")
else:
    print(equillibrium)


#number match
n=int(input())
arr=list(map(int,input().split()))
a,b=0,0
for num in set(arr):
    if num%2==0:
        if arr.count(num)%2==0:
            a+=1
        else:
            b+=1
    else:
        if arr.count(num)%2==0:
            b+=1
        else:
            a+=1
if a>b:
    print("A",a-b)
elif a==b:
    print("T 0")
else:
    print("B",b-a)

#candies
n,k,start=map(int,input().split())
start-=1
print((start+k-1)%n+1)

#reverse pack string

n=int(input())
if n==0:
    print("NULL")
else:
    s=input()
    k=int(input())%n
    print(s[k:]+s[:k])

'''

Problem Statement:

Imagine you have three magical crystals, each with a number on it: X, Y, and Z.

You are on a magical adventure where you pick two crystals from a table.
Your goal is to find the highest sum you can get by choosing two of these magical crystals,
using their numbers to create the most powerful combination.

Input Format:

The first line of input contains three space-separated integers X,Y and Z.

Output Format:

Print the highest possible sum of the numerals inscribed on the chosen two crystals.

Constraints:

1<=X,Y,Z<=10^8
'''
#trio
trio=list(map(int,input().split()))
trio.sort()
print(trio[-1]+trio[-2])

Given an array of positive integers, you need to create a new list where
Each element represents the frequency count of occurrence of all unique numbers in the original array.
Each frequency count occurs the number of times in the new list equal to the value of the
corresponding unique number in the original array. Finally, Sort the new list and display.
Input Format
The first line contains an integer n, denoting the size of the array.

The second line contains n space-separated integers, representing the elements of the array.

Sample Input:
6

331112

Sample Output: [1, 1, 2, 2, 2, 3]

Explanation:

[3, 3, 1, 1, 2] we have (3:2,1:3,2:1). So the list we get is (2, 2, 2, 3, 1, 1) sorting the list we have [1, 1, 2, 2, 2, 3]

#Reverse pack - 32
n=int(input())
arr=list(map(int,input().split()))
d={}
for num in arr:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1
res=[]
for key,val in d.items():
    res=res+[val]*key
res.sort()
print(res)

#string shortening
s=input()
while len(s)>0:
    temp=s
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            s=s[:i]+s[i+2:]
            break
    if temp==s:
        print(s)
        break
if len(s)==0:
    print("Empty String")



#prime factor ADDITION

n=int(input()) arr=list(map(int,input().split()))
num=int(input()) primes=[]
if len(arr)==0:
    print(-1)
else:
    while num%2==0:
        primes.append(2)
        num=num//2
    for i in range(3,int(num**0.5)+1,2):
        while num%i==0:
            primes.append(i)
            num=num//i
            if num>2:
                primes.append(num)
                res=0
                x=set(primes)
                try:
                    for pri in x:
                        res+=(primes.count(pri))*arr[pri]
                        print(res)
                except:
                    print(0)









