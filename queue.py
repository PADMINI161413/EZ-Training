#queue implementation
'''
global max
max=5
global q
q=[]
def enq():
    if len(q)== max:
        print("stack is overflow")
    else:
        ele=int(input("enter the element"))
        q.append(ele)
        print("the element pushed is ",ele)
def deq():
    if len(q)==0:
        print("stack is underflow")
    else:
        ele=q.pop(0)
        print("the element popped is ",ele)
def peek():
    if len(q)==0:
        print("the stack is empty")
    else:
        print(q[0])
def display():
    if len(q)==0:
        print("the stack is empty")
    else:
        print(q)
        
while True:
    print("1.insert\t2.delete\t3.peek\t4.display\t5.exit")
    ch=int(input("enter ur choice"))
    if ch==1:
        enq()
    elif ch==2:
        deq()
    elif ch==3:
        peek()
    elif ch==4:
        display()
    elif ch==5:
        break
        '''
#queue implementation using the linked list
'''
class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class stack:
    def __init__(self,size):
        self.front=None
        self.rare=None
        self.size=size
        self.count=0
    def push(self):
        if self.count==self.size:
            print("queue overflow")
        else:
            elem=int(input("Enter the elemen : "))
            nn=Node(elem)
            if self.rare==None:
                self.rare=nn
                self.front=nn
            else:
                self.rare.next=nn
                self.rare=nn
            self.count+=1
            print(self.rare.data,"is enqueued ")
    def pop(self):
        if self.front==None:
            print("queue underflow")
        else:
            e=self.front
            self.front=self.front.next
            print(e.data,"is dequeued ")
            del e
            self.count-=1
    def peek(self):
        if self.front==None:
            print("List is empty")
        else:
            print("peek  element is",self.front.data)
    def display(self):
        if self.front==None:
            print("queue is empty")
        else:
            current=self.front
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
'''
#queue implementation using the front and rare end
'''
q=[]
front=rare=-1
size=int(input("enter the size of the queue"))
def enq():
    global front,rare
    if rare==size-1:
        print("queue is overflow")
    else:
        ele=int(input("enter the element"))
        if rare==-1:
            front=0
        rare+=1
        q.append(ele)
        print("the element enqueued is ",ele)
def deq():
    global front,rare
    if front==-1 or front>rare:
        print("queue is underflow")
    else:
        ele=q[front]
        front+=1
        print("the element dequeued is ",ele)
def peek():
    global front,rare
    if front==-1 or front>rare:
        print("the queue is empty")
    else:
        print(q[front])
def display():
   global front,rare
   if front==-1 or front>rare:
        print("queue is underflow")
   else:
        for i in range(front,rare+1):
            print(q[i],end=" ")
        print()      
while True:
    print("1.insert\t2.delete\t3.peek\t4.display\t5.exit")
    ch=int(input("enter ur choice"))
    if ch==1:
        enq()
    elif ch==2:
        deq()
    elif ch==3:
        peek()
    elif ch==4:
        display()
    elif ch==5:
        print("exiting....")
        break
    else:
        print("invalid choice")
'''
#queue with insert befor and insert after
'''
class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class stack:
    def __init__(self,size):
        self.front=None
        self.rare=None
        self.size=size
        self.count=0
    def push(self):
        if self.count==self.size:
            print("queue overflow")
        else:
            elem=int(input("Enter the elemen : "))
            nn=Node(elem)
            if self.rare==None:
                self.rare=nn
                self.front=nn
            else:
                self.rare.next=nn
                self.rare=nn
            self.count+=1
            print(self.rare.data,"is enqueued ")
    def insert_bfr(self,ele,trgt):
        nn=Node(ele)
        if self.rare==None:
            print("list is empty not possible")
        elif self.rare.data==trgt:
            nn.next=self.rare
            self.front=nn
            self.rare=nn
        else:
            current=self.front
            while current.next and current.next.data !=trgt:
                current=current.next
            if current:
                nn.next=current.next
                current.next=nn
            else:
                print("target not found")
            self.count+=1
            print(nn.data,"is enququed")
    def insert_aftr(self,ele,trgt):
        nn=Node(ele)
        current=self.front
        while current and current.data !=trgt:
            current=current.next
        if current:
            nn.next=current.next
            current.next=nn
        else:
            print("node with data not found")
    def pop(self):
        if self.front==None:
            print("queue underflow")
        else:
            e=self.front
            self.front=self.front.next
            print(e.data,"is dequeued ")
            del e
            self.count-=1
    def peek(self):
        if self.front==None:
            print("List is empty")
        else:
            print("peek  element is",self.front.data)
    def display(self):
        if self.front==None:
            print("queue is empty")
        else:
            current=self.front
            while current:
                print(current.data,end= " ")
                current=current.next
            print()
size=int(input("Enter the number of elements: "))
stck=stack(size)
count=0
while True:
    print("Enter\n 1.Push\n 2.Pop\n 3.peek\n 4.Display\n5.inert bfr\n6.insert aftr\n7.Exit\n")
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
        ele=int(input("enter the element to insert"))
        trgt=int(input("enter the target elemet"))
        stck.insert_bfr(ele,trgt)
    elif ch==6:
        ele=int(input("enter the element to insert"))
        trgt=int(input("enter the target elemet"))
        stck.insert_aftr(ele,trgt)
    elif ch==7:
        break
'''
#circular queue
'''
class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class circularqueue:
    def __init__(self,size):
        self.rare=None
        self.front=None
        self.size=size
        self.count=0
    def is_full(self):
        return self.count==self.size
    def is_empty(self):
        return self.count==0
    def enq(self):
        if self.is_full():
            print("Queue overflow")
        else:
            elem=int(input("Enter the element : "))
            nn=Node(elem)
            if self.is_empty():
                self.rare=nn
                self.front=nn
                self.rare.next=self.front
            else:
                self.rare.next=nn
                self.rare=nn
                self.rare.next=self.front
            self.count+=1
            print(self.rare.data,"is Insered")
    def deq(self):
        if self.is_empty():
            print("Queue underflow")
        else:
            nd=self.front
            self.front=self.front.next
            self.rare.next=self.front
            print(nd.data,"is deleted")
            del nd
            self.count-=1
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Deleting element is",self.front.data)
    def display(self):
        if self.front==None:
            print("List is empty")
        else:
            current=self.front
            while current:
                print(current.data,end= " ")
                current=current.next
                if current==self.front:
                    break
            print()
size=int(input("Enter the number of elements: "))
CQ=circularqueue(size)
count=0
while True:
    print("Enter\n 1.Insert\n 2.Delete\n 3.peek\n 4.Insert_before\n 5.Insert_after\n 6.Display\n 7.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        CQ.enq()
    elif ch==2:
        CQ.deq()
    elif ch==3:
        CQ.peek()
    elif ch==4:
        CQ.enq_before()
    elif ch==5:
        CQ.enq_after()
    elif ch==6:
        CQ.display()
    elif ch==7:
        break
'''
#priority queue using the sll
'''
class Node:
    def __init__(self,ele,prty):
        self.data=ele
        self.next=None
        self.priority=prty
class Priorityqueue:
    def __init__(self):
        self.front=None
    def is_empty(self):
        return self.front is None
    def enq(self):
            ele=int(input("Enter the element : "))
            priority=int(input("enter the priority"))
            nn=Node(ele,priority)
            if self.is_empty()or priority > self.front.priority:
                nn.next=self.front
                self.front=nn
            else:
                current=self.front
                while current.next and current.next.priority > priority:
                    current=current.next
                nn.next=current.next
                current.next=nn
            print(ele,"is Insered")
    def deq(self):
        if self.is_empty():
            print("Queue underflow")
        else:
            e=self.front
            self.front=self.front.next
            print(e.data,"is deleted")
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("peek element is",self.front.data)
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current=self.front
            while current:
                print(current.data ,"-", current.priority )
                current=current.next
            print()
p=Priorityqueue()
count=0
while True:
    print("Enter\n 1.Insert\n 2.Delete\n 3.peek\n 4.Display\n 5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        p.enq()
    elif ch==2:
        p.deq()
    elif ch==3:
        p.peek()
    elif ch==4:
        p.display()
    elif ch==5:
        break
'''
# binary tree inorder preorder post order traversal
max_size=20
bt=[0]*max_size
def inorder(index):
    if bt[index]!=0:
        inorder(index*2+1)
        print(bt[index],end=' ')
        inorder(index*2+1)
def preorder(index):
    if bt[index]!=0:
        print(bt[index],end=' ')
        inorder(index*2+1)
        inorder(index*2+1)
def postorder(index):
    if bt[index]!=0:
        inorder(index*2+1)
        inorder(index*2+1)
        print(bt[index],end=' ')
def create(i,r):
    bt[i]=r
    ch=input("\n Is left child available for %d: press y/n\ : "%r)
    if ch=='y':
        value=int(input("Enter leftchild %d of node : : "%r))
        create(2*i+1,value)
    ch=input("\n Is rigth child available fro %d:press y/n : "%r)
    if ch=='y':
        value=int(input("enter rigth child %d of node : "%r))
        create(2*i+2,value)
r=int(input("enter root node : "))
create(0,r)
while True:
    print("1.inorder\n2.preorder\n3.postorder\n4.exit")
    ch=int(input("enter ur choice : "))
    if ch==1:
        inorder(0)
    elif ch==2:
        preorder(0)
    elif ch==3:
        postorder(0)
    elif ch==4:
        print("exiting.... ")
        break
    else:
        print("invalid choice")













