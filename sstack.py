# stack implemetation using list
'''
global max
max=5
global s
s=[]
def push():
    if len(s)== max:
        print("stack is overflow")
    else:
        ele=int(input("enter the element"))
        s.append(ele)
        print("the element pushed is ",ele)
def pop():
    if len(s)==0:
        print("stack is underflow")
    else:
        ele=s.pop()
        print("the element popped is ",ele)
def peek():
    if len(s)==0:
        print("the stack is empty")
    else:
        s.reverse()
        print(s)
        
while True:
    print("1.push\t2.pop\t3.peek\t4.exit")
    ch=int(input("enter ur choice"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    elif ch==4:
        break
'''
#implementation of stack using the linked list without overflow
'''
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack_llst:
    def __init__(self):
        self.top=None
    def  push(self,ele):
        nn=Node(ele)
        if self.top==None:
            self.top=nn
        else:
            nn.next=self.top
            self.top=nn
    def pop(self):
        if self.top==None:
            print("stack is underflow")
        else:
            temp=self.top
            self.top=temp.next
            print("the element popped is ",temp.data)
            del temp
    def peek(self):
        if self.top==None:
            print("stack is empty")
        else:
            current=self.top
            print(current.data)
    def display(self):
        if self.top==None:
            print("stack is empty")
        else:
            current=self.top
            while current:
                print(current.data)
                current=current.next
slst=Stack_llst()
while True:
    print("1.push\t2.pop\t3.peek\t4.display\t5.exit")
    ch=int(input("enter ur choice"))
    if ch==1:
        ele=int(input("enter an element to push"))
        slst.push(ele)
    elif ch==2:
        slst.pop()
    elif ch==3:
        slst.peek()
    elif ch==4:
        slst.display()
    elif ch==5:
        break        
'''
#implementation of stack using the linked list with overflow
class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class stack:
    def __init__(self,size):
        self.top=None
        self.size=size
        self.count=0
    def push(self):
        if self.count==self.size:
            print("stack overflow")
        else:
            elem=int(input("Enter the elemen : "))
            nn=Node(elem)
            if self.top==None:
                self.top=nn
            else:
                nn.next=self.top
                self.top=nn
            self.count+=1
            print(self.top.data,"is pushed")
    def pop(self):
        if self.top==None:
            print("stack underflow")
        else:
            nd=self.top
            self.top=self.top.next
            print(nd.data,"is deleted")
            del nd
            self.count-=1
    def peek(self):
        if self.top==None:
            print("List is empty")
        else:
            print("Top element is",self.top.data)
    def display(self):
        if self.top==None:
            print("List is empty")
        else:
            current=self.top
            while current:
                print(current.data,end= " ")
                current=current.next
            print()
size=int(input("Enter the number of elements: "))
stck=stack(size)
count=0
while True:
    print("Enter\n 1.Push\n 2.Pop\n 3.peek\n 4.Display\n 5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        stck.push()
    elif ch==2:
        stck.pop()
    elif ch==3:
        stck.peek()
    elif ch==4:
        stck.display()
    elif ch==5:
        break



















        
