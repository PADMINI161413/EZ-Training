import random
an={}
ac_bal={}
while True:
    print("********BANK OF BITM***********")
    print("1.create\t2.view\t3.exit")
    ch=int(input("enter ur choice :"))
    if ch==1:
        while True:
            acnt_nmbr=random.randint(10000,99999)
            if acnt_nmbr not in an:
                n=input("enter the a/c holder name : ")
                amt=int(input("enter deposit amount : "))
                an[acnt_nmbr]=n
                ac_bal[acnt_nmbr]=amt
                print("account created successfully")
                break
    elif ch==2:
        if len(an)==0:
            print("no accounts")
        else:
            print("-------------------------------------------------")
            print("a/c number\tUser Name\tAvailable Balanace")
            print("-------------------------------------------------")
            for i,j in an.items():
                print("%d\t\t%s\t\t%d"%(i,j,ac_bal[i]))
                print("-------------------------------------------------")
    elif ch==3:
        print("exiting....")
        break
    
    
