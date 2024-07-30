'''
for i in range(1,4):
    for j in range(1,6):
        print(i,end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,4):
        print(i,end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()
'''
'''
for i in range(1,6):          
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
'''
'''
n=int(input("enter a number"))
for i in range(1,n+1):          
    for j in range(1,n-i+2):
        print(j,end=' ')
    print()
'''
'''
n=int(input("enter a number"))
for i in range(1,n+1):          
    for j in range(1,n-i+2):
        print(i,end=' ')
    print()
'''
'''
n=int(input("enter a number"))
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()
for i in range(n,0,-1):          
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
'''
for i in range(5,0,-1):          
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,6):
        m=i*j
        print("%2d"%m,end=' ')
    print()
 '''
'''
cnt=0
for i in range(5):          
    for j in range(i+1):
        print(cnt,end=' ')
        cnt+=1
    print()
'''
'''
r=4
n=1
for i in range(1,r+1):          
    for j in range(n,n-i,-1):
        print("%2d"%j,end=' ')
        n=n+1+i
    print()
'''
