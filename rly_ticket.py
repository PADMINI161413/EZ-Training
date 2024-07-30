
'''
import random
avl_seats=5
pnr={}
nm={}
age={}
source={}
destin={}
def booking():
    for i in range(s):
            global n
            n=input("enter passenger name")
            global ag
            ag=int(input("enter passenger age"))
            global src
            src=input("enter source station")
            global dst
            dst=input("enter destination station")
            global pnr
            pnr=random.randint(1000,9999)
            age[pnr]=ag
            nm[pnr]=n
            source[pnr]=src
            destin[pnr]=dst
    print("ticket booked successfully")
def view():
    for i,j in pnr.items():
        print(f"%d\t%s\t%d\t%s\t%s"%(i,j,pnr[i],pnr[i],pnr[i]))
       
while True:
    print("1.ticket booking\n2.view booking\n3.cancel booking\n4.exit")
    ch=int(input("enter ur choice "))
    if ch==1:
         s=int(input("enter the number of tickes you want to book"))
         if s<=avl_seats:
             booking()
         else:
             print("seats are not available")
    elif ch==2:
        if len(pnr)==0:
            print("the list is empty")
        else:
            view()
'''        
             
















'''

import datetime

# initial train details
train_details = {
    "name": "",
    "age": 0,
    "source": "",
    "destination": "",
    "total_seats": 5,
    "available_seats": 5,
    "waiting_list": [],
    "booked_seats": []
}


def display_details():
    print("\nTrain Details")
    print(f"Name: {train_details['name']}")
    print(f"Age: {train_details['age']}")
    print(f"Source: {train_details['source']}")
    print(f"Destination: {train_details['destination']}")
    print(f"Total Seats: {train_details['total_seats']}")
    print(f"Available Seats: {train_details['available_seats']}")
    print(f"Waiting List: {train_details['waiting_list']}")
    print(f"Booked Seats: {train_details['booked_seats']}")


def book_ticket():
    if train_details["available_seats"] > 0:
        train_details["available_seats"] -= 1
        train_details["booked_seats"].append(datetime.datetime.now())
        print("\nTicket booked successfully.")
    elif train_details["available_seats"] == 0:
        if train_details["waiting_list"]:
            train_details["waiting_list"].append(datetime.datetime.now())
            print("\nTicket waiting in list.")
        else:
            print("\nAll seats are booked.")
    else:
        print("\nInvalid operation.")


def cancel_ticket():
    if train_details["booked_seats"]:
        train_details["booked_seats"].pop()
        train_details["available_seats"] += 1
        if train_details["waiting_list"]:
            train_details["waiting_list"].pop(0)
            train_details["booked_seats"].append(datetime.datetime.now())
            train_details["available_seats"] -= 1
        print("\nTicket cancelled successfully.")
    else:
        print("\nNo tickets to cancel.")


def run():
    while True:
        display_details()
        print("\nOperations")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            book_ticket()
        elif choice == 2:
            cancel_ticket()
        elif choice == 3:
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid operation. Please try again.")


if __name__ == "__main__":
    print("\nWelcome to the Train Ticket Booking System.")
    name = input("\nEnter your name: ")
    age = int(input("Enter your age: "))
    source = input("Enter source station: ")
    destination = input("Enter destination station: ")

    train_details["name"] = name
    train_details["age"] = age
    train_details["source"] = source
    train_details["destination"] = destination

    run()
'''
