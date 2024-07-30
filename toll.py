class TollGate:
    def __init__(self):
        self.vehicles = {}
        self.total_revenue = 0  

    def add_vehicle(self, vehicle_number, vehicle_type):
        if vehicle_number not in self.vehicles:
            self.vehicles[vehicle_number] = {'type': vehicle_type, 'fee_paid': False}
            print(f"Vehicle {vehicle_number} added successfully.")
        else:
            print(f"Vehicle {vehicle_number} is already registered.")
    def calculate_toll_fee(self, vehicle_type):
        if vehicle_type == 'car':
            return 5
        elif vehicle_type == 'truck':
            return 10
        elif vehicle_type == 'motorcycle':
            return 2
        else:
            return 0
    def display_vehicle_details(self, vehicle_number):
        if vehicle_number in self.vehicles:
            details = self.vehicles[vehicle_number]
            print(f"Vehicle Number: {vehicle_number}")
            print(f"Vehicle Type: {details['type']}")
            print(f"Fee Paid: {'Yes' if details['fee_paid'] else 'No'}")
        else:
            print(f"Vehicle {vehicle_number} not found.")
    def display_total_revenue(self):
        print(f"Total Revenue: {self.total_revenue}")
    def collect_toll_fee(self, vehicle_number):
        if vehicle_number in self.vehicles and not self.vehicles[vehicle_number]['fee_paid']:
            vehicle_type = self.vehicles[vehicle_number]['type']
            toll_fee = self.calculate_toll_fee(vehicle_type)
            self.total_revenue += toll_fee
            self.vehicles[vehicle_number]['fee_paid'] = True
            print(f"Toll fee collected for Vehicle {vehicle_number}. Fee: {toll_fee}")
        else:
            print(f"Invalid operation. Vehicle {vehicle_number} not found or fee already paid.")
toll_gate = TollGate()
while True:
    print("\nToll Gate Management System\n")
    print("1. Add Vehicle")
    print("2. Display Vehicle Details")
    print("3. Display Total Revenue")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        vehicle_number = input("Enter Vehicle Number: ")
        vehicle_type = input("Enter Vehicle Type (car/truck/motorcycle): ").lower()
        toll_gate.add_vehicle(vehicle_number, vehicle_type)
        toll_fee = toll_gate.calculate_toll_fee(vehicle_type)
        print(f"Toll Fee for {vehicle_type}: {toll_fee}")
    elif choice == '2':
        vehicle_number = input("Enter Vehicle Number: ")
        toll_gate.display_vehicle_details(vehicle_number)
    elif choice == '3':
        vehicle_number = input("Enter Vehicle Number: ")
        toll_gate.collect_toll_fee(vehicle_number)
        toll_gate.display_total_revenue()       
    elif choice == '4':
        print("Exiting ")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
