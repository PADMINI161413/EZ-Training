#try except handling
'''
n=int(input("enter numerator"))
d=int(input("enter denominator"))
try:
    q=n/d
    print(q)
except ZeroDivisionError:
    print("denominator cant be zero")
'''
#without exception handling
'''
n=int(input("enter numerator"))
d=int(input("enter denominator"))
q=n/d
print(q)
'''
#multiple except block
'''
try:
    n=int(input("enter numerator"))
    d=int(input("enter denominator"))
    q=n/d
    print(q)
except ZeroDivisionError:
    print("denominator cant be zero")
except ValueError:
    print("invalid data type")
'''
#multiple except in a single block
'''
try:
     n=int(input("enter numerator"))
     d=int(input("enter denominator"))
     q=n/d
     print(q)
except (ZeroDivisionError,ValueError):
    print("denominator cant be zero or ValueError")
'''
#except block without exception
'''
try:
    n=int(input("enter numerator"))
    d=int(input("enter denominator"))
    q=n/d
    print(q)
except ZeroDivisionError:
    print("denominator cant be zero")
except ValueError:
    print("invalid data type")
except:
    print("unknown error")
'''
#using else clause
'''
try:
    n=int(input("enter numerator"))
    d=int(input("enter denominator"))
    q=n/d
    print(q)
except ZeroDivisionError:
    print("denominator cant be zero")
except ValueError:
    print("invalid data type")
else:
    print("successful termination")
'''
#raise exception
'''
n=int(input("enter number"))
if n<0:
    raise Exception("negtive number not allowed")
'''
#finally
'''
try:
    print("raising an error")
    raise ValueError
finally:
    print("In finally block")
'''
