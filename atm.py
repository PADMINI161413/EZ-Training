import sys
card1=111
pin1=1020
mb1=123456
i=0
while i!=2:
    c1=int(input("enter card number"))
    p1=int(input("enter pin number"))
    if c1==card1 and p1==pin1:
        print("user found")
        break
        sys.exit()
    else:
        print("invalid user")
        a=input("fogot password yes/no")
        if a=="yes" or a=="YES" or a=="Yes":
            m1=int(input("enter verified mobile number"))
            if m1==mb1:
                print(f"your pin is {pin1}")
            else:
                print("invalid mobile number")
        else:
            print("do you want to update/reset password yes/no")
            c=input( )
            if c=="yes" or c=="YES" or c=="Yes":
                m1=int(input("enter verified mobile number"))
                if m1==mb1:
                    re_pin1=int(input( "enter new pin "))
                    pin1=re_pin1
                    print("pin updated successfully")
                else:
                    print("invalid mobile number")
print("1success")
'''
while  i!=2:
    if c1==card2:
        p2=int(input("enter pin number"))
        if  p2==pin2:
            print("user found")
        else:
            print("invalid pin")
            b=input("fogot password yes/no")
            if b=="yes" or b=="YES" or b=="Yes":
                m2=int(input("enter verified mobile number"))
                if m2==mb2:
                    print(f"your pin is {pin2}")
                else:
                    print("invalid mobile number")
            else:
                print("do you want to update/reset password yes/no")
                d=input( )
                if d=="yes" or d=="YES" or d=="Yes":
                    m2=int(input("enter verified mobile number"))
                    if m2==mb2:
                        re_pin2=int(input( "enter new pin "))
                        p2=re_pin2
                        print("pin updated successfully")
                    else:
                        print("invalid mobile number")
print("login 2")
       
'''
