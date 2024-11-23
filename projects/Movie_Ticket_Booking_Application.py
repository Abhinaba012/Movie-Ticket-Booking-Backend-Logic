def Outer(arg):
    L = []
    def Inner():
        if len(L) == 0:
            obj = arg()
            L.append(obj)
        return L[0]
    return Inner

@Outer
class KGF_Chapter1():
    def __init__(self):
        self.Total_Tickets = 200
    def booking(self):
        req_tickets = int(input("How Many Tickets You Want : "))
        if req_tickets <= self.Total_Tickets:
            print(f'{req_tickets} Tickets Has Been Booked Successfully For You')
            self.Total_Tickets -= req_tickets
            print(f'{self.Total_Tickets} Tickets Are Left')
        else:
            print(f'Sorry!!! We Have Only {self.Total_Tickets} Tickets Left')

@Outer
class RRR():
    def __init__(self):
        self.Total_Tickets = 200
    def booking(self):
        req_tickets = int(input("How Many Tickets You Want : "))
        if req_tickets <= self.Total_Tickets:
            print(f'{req_tickets} Tickets Has Been Booked Successfully For You')
            self.Total_Tickets -= req_tickets
            print(f'{self.Total_Tickets} Tickets Are Left')
        else:
            print(f'Sorry!!! We Have Only {self.Total_Tickets} Tickets Left') 

@Outer 
class Dangal():
    def __init__(self):
        self.Total_Tickets = 200
    def booking(self):
        req_tickets = int(input("How Many Tickets You Want : "))
        if req_tickets <= self.Total_Tickets:
            print(f'{req_tickets} Tickets Has Been Booked Successfully For You')
            self.Total_Tickets -= req_tickets
            print(f'{self.Total_Tickets} Tickets Are Left')
        else:
            print(f'Sorry!!! We Have Only {self.Total_Tickets} Tickets Left') 

def BookMyShow():
    print("1) KGF_Chapter1 \n2) RRR \n3) Dangal")
    choice = int(input("Please Choose The Movie : "))
    if choice == 1:
        user = KGF_Chapter1()
        user.booking()
    elif choice == 2:
        user = RRR()
        user.booking()
    elif choice == 3:
        user = Dangal()
        user.booking()
    else:
        print('No Movie Available')
user1 = BookMyShow()
print('-' * 30)
user2 = BookMyShow()
print('-' * 30)
user3 = BookMyShow()
print('-' * 30)
        