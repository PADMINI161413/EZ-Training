un=[]
act=[]
lmt=[]
while True:
    print(" 1.add\t2.view\t3.delete\t4.modify")
    ch=int(input("enter ur choice - "))
    if ch==1:
        n=input("enter name: ")
        while True:
            an=int(input("enter account number : "))
            can=int(input("confirm account number: "))
            if an==can:
                l=int(input("enter the limit"))
                un.append(n)
                act.append(an)
                lmt.append(l)
                print("benificiary account added")
                break
            else:
                print("account number mismatched")
    elif ch==2:
            if len(un)==0:
                print("list is empty")
            else:
                print("Name\t\tAcct_Num\t\tLimit")
                for i in range(len(un)):
                    print("%s\t\t%d\t\t%d"%(un[i],act[i],lmt[i]))
    elif ch==3:
        if len(un)==0:
            print("list is empty")
        else:
            i=int(input("enter te index of the benificiary account to delete"))
            if i>=0 and i<len(un):
                del un[i]
                del act[i]
                del lmt[i]
                print("Beneficiary deleted.")
            else:
                print("Invalid index.")
    elif ch==4:
        if len(un)==0:
            print("list is empty")
        else:
            mi=int(input("Enter the index of the beneficiary to modify: "))
            if mi>=0 and mi<len(un):
                print("1.modify name\t2.modify limit")
                p=int(input("enter choice "))
                if p==1:
                    new_nm=input("Enter the new name : ")
                    un[mi] = new_nm
                    print("name modified.")   
                else:
                    new_l= int(input("Enter the new limit: "))
                    lmt[mi] = new_l
                    print("limit modified.")
            else:
                print("Invalid index.")
        
    c=input("do u want to continue :press y/n = ")
    if c.upper()=='N':
        break
