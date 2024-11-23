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
        self.total_ticket = 200
    def booking(self):
        req_ticket = int(input("How Many Tickets You Want : "))
        if req_ticket <= self.total_ticket:
            print('Congratulations....Your Tickets Have Been Booked Successfully')
            self.total_ticket -= req_ticket
            print(f'Only {self.total_ticket} Tickets Are Left')
        else:
            print(f'Sorry!!! We Have Only {self.total_ticket} Tickets Left')
@Outer
class RRR():
    def __init__(self):
        self.total_ticket = 220
    def booking(self):
        req_ticket = int(input("How Many Tickets You Want : "))
        if req_ticket <= self.total_ticket:
            print('Congratulations....Your Tickets Have Been Booked Successfully')
            self.total_ticket -= req_ticket
            print(f'Only {self.total_ticket} Tickets Are Left')
        else:
            print(f'Sorry!!! We Have Only {self.total_ticket} Tickets Left')
@Outer
class Dangal():
    def __init__(self):
        self.total_ticket = 250
    def booking(self):
        req_ticket = int(input("How Many Tickets You Want : "))
        if req_ticket <= self.total_ticket:
            print('Congratulations....Your Tickets Have Been Booked Successfully')
            self.total_ticket -= req_ticket
            print(f'Only {self.total_ticket} Tickets Are Left')
        else:
            print(f'Sorry!!! We Have Only {self.total_ticket} Tickets Left')
def BookMyShow():
    print('1) KGF_Chapter1 \n2) RRR \n3) Dangal')
    choice = int(input('Which Movie You Want To Watch : '))
    if choice == 1:
        user = KGF_Chapter1()
        user.booking()
    elif choice == 2:
        user = RRR()
        user.booking()
    elif choice == 1:
        user = Dangal()
        user.booking()
    else:
        print('Sorry!!! No Movie Available')
def Paytm():
    print('1) KGF_Chapter1 \n2) RRR \n3) Dangal')
    choice = int(input('Which Movie You Want To Watch : '))
    if choice == 1:
        user = KGF_Chapter1()
        user.booking()
    elif choice == 2:
        user = RRR()
        user.booking()
    elif choice == 1:
        user = Dangal()
        user.booking()
    else:
        print("Sorry!!! No Movie Available")
def GooglePay():
    print('1) KGF_Chapter1 \n2) RRR \n3) Dangal')
    choice = int(input('Which Movie You Want To Watch : '))
    if choice == 1:
        user = KGF_Chapter1()
        user.booking()
    elif choice == 2:
        user = RRR()
        user.booking()
    elif choice == 1:
        user = Dangal()
        user.booking()
    else:
        print("Sorry!!! No Movie Available")
def PhonePe():
    print('1) KGF_Chapter1 \n2) RRR \n3) Dangal')
    choice = int(input('Which Movie You Want To Watch : '))
    if choice == 1:
        user = KGF_Chapter1()
        user.booking()
    elif choice == 2:
        user = RRR()
        user.booking()
    elif choice == 1:
        user = Dangal()
        user.booking()
    else:
        print("Sorry!!! No Movie Available")
user1 = BookMyShow()
print('-' * 30)
user2 = Paytm()
print('-' * 30)
user3 = GooglePay()
print('-' * 30)
user4 = PhonePe()
print('-' * 30)
