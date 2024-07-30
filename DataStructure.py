#to create linkedlist 1.create node 2.initialize 3.linking 4.traverse/display
'''
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
n1=Node(100)
n2=Node(150)
n3=Node(200)
n1.next=n2
n2.next=n3
start=n1
while start:
    print(start.data)
    start=start.next
'''
#to display the method using in the class
'''
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    def display(self):
        while self:
            print(self.data)
            self=self.next
n1=Node(100)
n2=Node(150)
n3=Node(200)
n1.next=n2
n2.next=n3
n1.display()
'''

# inserting node at end begin
'''
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_last(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=nn
    def insert_first(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn
    def insert_bfr(self,ele,trgt):
        nn=Node(ele)
        if self.head==None:
            print("list is empty not possible")
        elif self.head.data==trgt:
            nn.next=self.head
            self.head=nn
        elif self.head.next.data==trgt:
            nn.next=self.head.next
            self.head.next=nn
        else:
            current=self.head
            while current.next and current.next.data !=trgt:
                current=current.next
            if current.next:
                nn.next=current.next
                current.next=nn
    def insert_aftr(self,ele,trgt):
        nn=Node(ele)
        current=self.head
        while current and current.data !=trgt:
            current=current.next
        if current:
            nn.next=current.next
            current.next=nn
        else:
            print("node with data not found")
    def del_first(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            self.head=temp.next
            print(temp.data,"deleted")
            del temp
    def del_end(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            while current.next!=None:
                prev=current
                current=current.next
            prev.next=None
            print(current.data,"deleted")
            del current
    def search(self,key):
        self.count=0
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            while current.next!=None:
                if current.data==key:
                    self.found=1
                self.count+=1
                current=current.next
            if self.found==1:
                print("element found at",self.count )
            else:
                print("element not found")
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    ''''''def rev_dsply(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            l=[]
            while current:
                l.append(current.data)
                current=current.next
                r=list(reversed(l))
            print(r)''''''
    def rev_dsply(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            prev=None
            while current:
                nextnode=current.next
                current.next=prev
                prev=current
                current=nextnode
            self.head=prev
            
llst=linkedlist()
while True:
    print("1.insert at last \n2.insert at first\n3.insert bfr node\n"+
          "4.insert aftr node\n5.deleting @beginning\n"+
          "6.deleting @end\n7.display\n8.search\n9.reverse display\n10.exit")
    ch=int(input("enter ur choice"))
    if ch==1:
        ele=int(input("enter the element to insert"))
        llst.insert_last(ele)
    elif ch==2:
        ele=int(input("enter the element to insert"))
        llst.insert_first(ele)
    elif ch==3:
        ele=int(input("enter the element to insert"))
        trgt=int(input("enter target element whose before you want to insert"))
        llst.insert_bfr(ele,trgt)
    elif ch==4:
        ele=int(input("enter the element to insert"))
        trgt=int(input("enter target element whose after you want to insert"))
        llst.insert_aftr(ele,trgt)
    elif ch==5:
        llst.del_first()
    elif ch==6:
        llst.del_end()
    elif ch==7:
        llst.display()
    elif ch==8:
        key=int(input("enter an element to search"))
        llst.search(key)
    elif ch==9:
        llst.rev_dsply()
        llst.display()
    elif ch==10:
        print("exiting ...")
        break
'''
#double linked list
'''
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
n1=Node(100)
n2=Node(150)
n3=Node(200)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
start=n1
while start:
    print(start.data)
    start=start.next #start=start.prev for reverse order 
'''
'''
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    def display(self):
        while self:
            print(self.data)
            self=self.next
n1=Node(100)
n2=Node(150)
n3=Node(200)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n1.display()
'''
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_last(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=nn
            nn.prev=current
    def insert_first(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            nn.next=self.head
            self.head.prev=nn
            self.head=nn           
    def insert_bfr(self,ele,trgt):
        nn=Node(ele)
        if self.head==None:
            print("list is empty not possible")
        elif self.head.data==trgt:
            nn.next=self.head
            self.head.prev=nn
            self.head=nn
        else:
            current=self.head
            while current.next and current.next.data !=trgt:
                current=current.next
            if current:
                current.next.prev=nn
                nn.next=current.next
                current.next=nn
                nn.prev=current
    def insert_aftr(self,ele,trgt):
        nn=Node(ele)
        current=self.head
        if self.head==None:
            print("list is empty not possible")
        elif self.head.data==trgt:
           self.head.next=nn
           nn.prev=self.head
        else:
            while current and current.data !=trgt:
                current=current.next
            if current:
                current.next.prev=nn
                nn.next=current.next
                current.next=nn
                nn.prev=current
            else:
                print("node with data not found")
    def del_first(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            self.head=temp.next
            print(temp.data,"deleted")
            del temp
    def del_end(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            while current.next!=None:
                temp=current
                current=current.next
            current.prev=None
            temp.next=None 
            print(current.data,"deleted")
            del current
    def search(self,key):
        self.count=0
        if self.head==None:
            print("list is empty")
        else:
            found=False
            count=0
            current=self.head
            while current.next!=None:
                if current.data==key:
                    found=True
                    break
                count+=1
                current=current.next
            if found:
                print("element found at",count )
            else:
                print("element not found")
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def rev_dsply(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            while current:
                print(current.data)
                current=current.prev
        
            
llst=linkedlist()
while True:
    print("1.insert at last \n2.insert at first\n3.insert bfr node\n"+
          "4.insert aftr node\n5.deleting @beginning\n"+
          "6.deleting @end\n7.display\n8.search\n9.reverse display\n10.exit")
    ch=int(input("enter ur choice"))
    if ch==1:
        ele=int(input("enter the element to insert"))
        llst.insert_last(ele)
    elif ch==2:
        ele=int(input("enter the element to insert"))
        llst.insert_first(ele)
    elif ch==3:
        ele=int(input("enter the element to insert"))
        trgt=int(input("enter target element whose before you want to insert"))
        llst.insert_bfr(ele,trgt)
    elif ch==4:
        ele=int(input("enter the element to insert"))
        trgt=int(input("enter target element whose after you want to insert"))
        llst.insert_aftr(ele,trgt)
    elif ch==5:
        llst.del_first()
    elif ch==6:
        llst.del_end()
    elif ch==7:
        llst.display()
    elif ch==8:
        key=int(input("enter an element to search"))
        llst.search(key)
    elif ch==9:
        llst.rev_dsply()
    elif ch==10:
        print("exiting ...")
        break












