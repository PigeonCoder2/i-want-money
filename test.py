class Renter:
    
    renters = []
    basic_cost = 119 * 1.15
    rooms_available = [i for i in range(1, 9)]
    
    def __init__(self, name, num_of_days, cost, plan=""):
        self.name = name
        self.num_of_days = num_of_days
        self.cost = round(cost, 2)
        print("Cost of stay: ", self.cost)
        self.plan = plan
        
        if len(Renter.rooms_available) == 0:
            print("No rooms available")
            return
        
        self.room_number = Renter.rooms_available[0]
        Renter.rooms_available = Renter.rooms_available[1:]
        
        Renter.renters.append(self)

    @classmethod
    def rent_a_room(cls):
        
        print("Input name:")
        name = input()
        
        print("Number of days staying:")
        num_of_days = int(input())
        
        if num_of_days <= 14:
            ShortTermRenter(name, num_of_days)
        else:
            LongTermRenter(name, num_of_days)
            
        
    def checkout(room_number):
        for renter in Renter.renters:
            if renter.room_number == room_number:
                Renter.renters.remove(renter)
                Renter.rooms_available.append(room_number)
                return 
            
    
    def __str__(self):
        return f"Renter1 ({self.room_number}): {self.num_of_days} day stay {self.plan}"
            
            
class ShortTermRenter(Renter):
    
    def __init__(self, name, num_of_days):
        
        cost = self.basic_cost * num_of_days
        
        print("Would they like to purchase the breakfast plan? (Y/N)")
        
        plan = ""
        if input() == "Y":
            cost += 5.99 * num_of_days
            plan = "(Breakfast Plan)"
            
        super().__init__(name, num_of_days, cost, plan)
        
class LongTermRenter(Renter):
    
    def __init__(self, name, num_of_days):
        
        cost = self.basic_cost * num_of_days * 0.7
        
        print("Would they like to purchase an insurance package?")
        print("0: No Package")
        print("1: Basic Package")
        print("2: Premium Package")
        choice = int(input())
        
        if choice == 1:
            plan = "(Basic)"
            cost += 25
            
        elif choice == 2:
            plan = "(Premium)"
            cost += 75
        
        super().__init__(name, num_of_days, cost, plan = "" or plan)
        


def main(): 
    while True:
        
        print()
        print("Make a Selection: ")
        print("Rent a Room (R), Check Out (C), Print Motel Details (P), Exit Program (X)")
        choice = input()
        
        if choice == "R":
            Renter.rent_a_room()
            
        elif choice == "C":
            print("Input the room number checking out:")
            Renter.checkout(int(input()))
            
        elif choice == "P":
            for renter in Renter.renters:
                print(renter)
                
        elif choice == "X":
            print("Thank you for using the program!")
            break
        
        
if __name__ == "__main__":
    main()