import employee
'''
employee.n()#syntax:modulename.function/resource
employee.r()
'''
a=int(input("enter first number "))
b=int(input("enter second number"))
o=input("enter an operator (+,-,*,/) ")
if o=='+':
    r=employee.add(a,b)
    print(f"{a} {o}  {b}= {r} ")
elif o=='-':
    r=employee.sub(a,b)
    print(f"{a} {o}  {b}= {r} ")
elif o=='*':
    r=employee.mul(a,b)
    print(f"{a} {o}  {b}= {r} ")
elif o=='/':
    r=employee.div(a,b)
    print(f"{a} {o}  {b}= {r} ")

