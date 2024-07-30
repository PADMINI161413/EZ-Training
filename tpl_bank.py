import random
open=5000
acnt=12345
avl_bal=open
trnsct=()
while True:
    print("1.to do transaction\t2.to view transaction\t3.exit ")
    ch=int(input("enter your choice : "))
    if ch==1:
        typ=input(" press d-Deposit or  w-withdraw : ")
        if typ.lower()=="d":
            amt=int(input("enter amount to deposit"))
            avl_bal=avl_bal+amt
            tid=random.randint(1000,9999)
            trnsct=trnsct+((tid,acnt,typ,amt,avl_bal),)
            print("deposit  is sucessful...")
        elif typ.lower()=='w':
            while True:
                amt=int(input("enter amount to Withdrw"))
                if amt<avl_bal:
                    avl_bal=avl_bal-amt
                    tid=random.randint(1000,9999)
                    trnsct=trnsct+((tid,acnt,typ,amt,avl_bal),)
                    print("withdraw  is sucessful...")
                    break
                else:
                    print("insufficient balance",avl_bal)
    elif ch==2:
        if len(trnsct)==0:
            print("No transaction")
        else:
            for i in trnsct:
                print(*i)
    elif ch==3:
        break
            

