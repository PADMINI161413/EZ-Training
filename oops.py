'''
class Test:
    id=1122
t=Test()
print(t.id)
'''
#
'''
class Emp():
    nm=None
    eid=None
    def set_details(self,n,id):
        self.nm=n
        self.eid=id
    def dsply(self):
        print(self.nm,self.eid)
e1=Emp()
e1.set_details("padmini",1122)
e1.dsply()
e2=Emp()
e2.set_details("joshi",1111)
e2.dsply()
'''
#__init() method constructor
'''
class Emp():
    def __init__(self,n,id):
        self.nm=n
        self.eid=id
    def dsply(self):
        print(self.nm,self.eid)
e1=Emp("padmini",1122)
e1.dsply()
e2=Emp("joshi",1111)
e2.dsply()
'''
#class vs object variable
'''
class Circle:
    pi=3.14159
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.pi*self.radius**2
c1=Circle(5)
c2=Circle(10)
print("radius=%.2f\tArea=%.2f"%(c1.radius,c1.area()))
print("radius=%.2f\tArea=%.2f"%(c2.radius,c2.area()))
'''
#__del__ method
'''
class Emp:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("destructor called,object deleted")
obj=Emp()
del obj
'''
# __len__ method
'''
class Emp():
    def __init__(self,n,id):
        self.nm=n
        self.eid=id
    def dsply(self):
        print(self.nm,self.eid)
    def __len__(self):
        return len(self.nm)        
e1=Emp("padmini",1122)
e1.dsply()
print("length of ",e1.nm,"is",len(e1))
'''
#when we try to print object directly it prints address
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p=point(15,25)
print(p)
'''
#converting an instance to a string
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p=point(15,25)
print(p)
'''
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dsply(self):
        print("(%d , %d )"%(self.x,-(self.y)))
p=point(1,-2)
p.dsply()
'''
#reflect point
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def rflct(self):
        return point(self.x,-self.y)
    def __str__(self):
        return f"point({self.x},{self.y})"
op=point(3,5)
rp=op.rflct()
print(f"original point :{op}")
print(f"reflected point :{rp}")
'''
'''
class point:
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
    def rflct(self,x2,y2):
        self.x2=x2
        self.y2=y2
    def mp(self):
         print((self.x1+self.x2)/2 ,(self.y1+self.y2)/2)
p=point(-2,1)
q=p.rflct(5,4)
p.mp()
'''
#to find midpoint using the given points taking mid outside the class
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
def mid(p1,p2):
    mx=(p1.x+p2.x)/2
    my=(p1.y+p2.y)/2
    return point(mx,my)
p=point(-2,1)
q=point(5,4)
r= mid(p,q)
print(str(r))
'''
# mid inside the class
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def mid(self,p1,p2):
        mx=(p1.x+p2.x)/2
        my=(p1.y+p2.y)/2
        print(mx,my)
p=point(-2,1)
q=point(5,4)
p.mid(p,q)
#print(str(r))
'''
'''
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def mid(p1,p2):
        mx=(p1.x+p2.x)/2
        my=(p1.y+p2.y)/2
        return point(mx,my)
p=point(-2,1)
q=point(5,4)
r=p.mid(q)
print(str(r))
'''
#data encapsulation
'''
class Emp():
    def __init__(self,n,id):
        self.nm=n
        self.__eid=id
    def __dsply(self):
        print(self.nm,self.__eid)
e1=Emp("padmini",1122)
print(e1.nm)
e1._Emp__dsply()
print(e1._Emp__eid)
'''
'''
class ABC():
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def dsply(self):
        print("from class method,var1=",self.var1)
        print("from class method,var2=",self.__var2)
obj=ABC(10,20)
obj.dsply()
print("from main module,var1=",obj.var1)
#print("from main module,var2=",obj.__var2)
print("from main module,var2=",obj._ABC__var2)
'''
#caling a class from another class
'''
class Emp():
    def __init__(self,n,id):
        self.nm=n
        self.eid=id
    def dsply(self):
        print(self.nm,self.eid)
class call():
    def abc(self):
        e1=Emp("padmini",1122)
        e1.dsply()
a=call()
a.abc()
'''
#calling class method from another class method
'''
class Emp():
    def __init__(self,n,id):
        self.nm=n
        self.eid=id
    def dsply(self):
        print(self.nm,self.eid)
    def call(self):
        self.dsply()

e1=Emp("padmini",1122)
e1.call()
'''
'''
class ABC():
    def __init__(self,var):
        self.var=var
    def dsply(self):
        print("var is =",self.var)
    def add_2(self):
        self.var+=2
        self.dsply()
obj=ABC(10)
obj.add_2()
'''
#inheritance
'''
class college():
    def __init__(self,n,age):
        self.nm=n
        self.ag=age
    def display(self):
        print(self.nm,self.ag)
class student(college):
    pass
s1=student("raj",20)
s1.display()
'''
#multi level inheritance
'''
class college():
    def clg(self):
        print("college :    ")
class dept(college):
    def d(self):
        print("department :  ")
class dsgntn(dept):
    def dsg(self):
        print("desgnation :   ")
e=dsgntn()
e.clg()
e.d()
e.dsg()
'''
#multiple inheritance
'''
class college():
    def clg(self):
        print("college :    ")
class dept():
    def d(self):
        print("department :  ")
class dsgntn(college,dept):
    def dsg(self):
        print("desgnation :   ")
e=dsgntn()
e.clg()
e.d()
e.dsg()
'''
#polymorphism
'''
class vehicle:
    def wheels(self):
        pass
class cycle(vehicle):
    def wheels(self):
        return "two"
class auto(vehicle):
    def wheels(self):
        return "three"
class car(vehicle):
    def wheels(self):
        return "four"
def display(vehicle):
    return vehicle.wheels()
cy=cycle()
at=auto()
cr=car()
print(display(cy))
print(display(at))
print(display(cr))
'''

class addition():
    def __init__(self,num):
        self.n=num
    def __add__(self,othr):
        return self.n+othr.n
n1=addition(22)
n2=addition(33)
print(n1+n2)











