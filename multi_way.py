#number +ve ,-ve,0
'''x=int(input("enter a number"))
if x==0:
    print("zero")
elif x<0:
        print("negative")
else:
    print("positive")
'''
#profit loss
'''
cost=float(input("enter cost price"))
sell=float(input("enter selling price"))
a=sell-cost
if a>0:
    print("Profit: $",a)
elif a<0:
    print("Loss: $%.2f"%-a)
else:
    print("same")
'''
#designation
'''
sal=int(input( ))
if sal>25000 and sal<40000:
    print("Manager")
elif sal>15000 and sal<=25000:
        print("Accountant")
elif sal<=15000:
     print("Clerk")
'''
#library book fine
'''
day=int(input("enter no.of days "))
if day>=1 and day<=5:
    print("$%d"%15)
elif day>=6 and day<=10:
    print("$%d"%50)
elif day>10 and day<=29:
    print("$%d"%100)
elif day==30 or day>30:
    print("Membership canceled")
 '''
#directions
'''
char=input("enter ")
if char=='n' or char=='N':
    print("North")
elif char=='s' or char=='S':
    print("South")
elif char=='w' or char=='W':
    print("West")
elif char=='e' or char=='E':
    print("East")
    '''
