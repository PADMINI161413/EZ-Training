#prime number
'''num = int(input("Enter the number: "))

if num > 1:
# check for factors
for i in range(2,num):
if (num % i) == 0:
print(num,"is not a prime number")
print(i,"times",num//i,"is",num)
break
else:
print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
print(num,"is not a prime number")'''
#palindrome
'''
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
'''
#reverse
'''
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)
'''

