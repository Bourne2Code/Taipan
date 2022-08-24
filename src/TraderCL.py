import os
import random

class Money:
    onHand = 0
    inBank = 0
    inDebt = 0
    
    def __init__(self, onHand):
        self.onHand = onHand
        
    def NetWorth(self):
        return((onHand + inBank) - inDebt)

    def print_MoneyStatus(self):
        print("Gold On Hand :", self.onHand)
        print("Gold in Bank :", self.inBank)
        print("Gold in Debt :", self.inDebt,"\n")
    
    def SpendMoney(self,gold2spend):
        retVal = False
        if (gold2spend > self.onHand):
            print("Too much!")
        else : 
            self.onHand = (self.onHand - gold2spend)
            retVal = True
        return(retVal)

    def AddMoney(self,gold2add):
        self.onHand = (self.onHand + gold2add)


class Ship:
#    itemName = ["Silk", "Tea", "Gunpowder", "Opium"]
    itemQty = [0, 0, 0, 0]
    
    def __init__(self, name, capacity, defense):
        self.name = name
        self.capacity = capacity
        self.defense = defense
        
    def print_ShipStatus(self):
        print("Ship Name     :", self.name)
        print("Ship Defense  :", self.defense)
        print("Ship Capacity :", self.capacity,"\n")

    def getItemQty(self, index):
        return (self.itemQty[index])

    def getCapacity(self):
        return (self.capacity)
        
    def addItem(self, index, amount2add):
        retVal = False
        if (amount2add > self.capacity) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] + amount2add)
            self.capacity = (self.capacity - amount2add)
            retVal = True
        return retVal
        
    def removeItem(self, index, amount2rem):
        retVal = False
        if (amount2rem > self.itemQty[index]) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] - amount2rem)
            self.capacity = (self.capacity + amount2rem)
            retVal = True
        return retVal
        
global Company_Name
global Port_Names               # Constant? 
global TradedItems_Name         # Constant? 
global TradedItems_Price
global TradedItems_InShip
global TradedItems_InWarehouse
global Current_Port
global Current_Port_Name
global User_Action
global Trade_Ship
global Player_Ship
global Player_Money

Port_Names = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
TradedItems_Name = ["Silk", "Tea", "Gunpowder", "Opium"]
TradedItems_Price = [20, 10, 50, 500]
Current_Port = 0
Player_Ship = Ship("The Peace Dividend", 15, 1000)
Player_Money = Money(1000)


def Clear_Screen():
    os.system('cls')
#    subprocess.run(["cls"])
    
def Config_Player():
    global Company_Name
    global Silver_OnHand
    global Silver_InBank
    global TradedItems_InShip
    global TradedItems_InWarehouse

    Clear_Screen()
    print("Welcome to the East Empire Trading Simulation!\n")
    Company_Name = input("What shall we use for a company name?\n")
    Silver_OnHand = 1000
    Silver_InBank = 0
    TradedItems_InShip = [0, 0, 0, 0]
    TradedItems_InWarehouse = [0, 0, 0, 0]


def Set_Prices():
    global TradedItems_Price
    TradedItems_Price = [random.randrange(5, 45, 1), random.randrange(2, 25, 1), random.randrange(5, 75, 1), random.randrange(300, 999, 1)]

def Travel_toPort():
    global Current_Port

    print('\033[39m')
    print(f"Ports: [H,B,C,J,M,P,R,S]")
    for i in range(7):
        print(Port_Names[i])

    Port_Desired = input("Where would you like to go? [H,B,C,J,M,P,R,S]")[0].upper()
    while (Port_Desired != "H") and (Port_Desired != "B") and (Port_Desired != "C") and (Port_Desired != "J") and (Port_Desired != "M") and (Port_Desired != "P") and (Port_Desired != "R") and (Port_Desired != "S"):
        Port_Desired = input("invalid selection. \nWhere would you like to go? [H,B,C,J,M,P,R,S]")[0].upper()

    match Port_Desired:
        case "H":
            Current_Port = 0
        case "B":
            Current_Port = 1
        case "C":
            Current_Port = 2
        case "J":
            Current_Port = 3
        case "M":
            Current_Port = 4
        case "P":
            Current_Port = 5
        case "R":
            Current_Port = 6
        case "S":
            Current_Port = 7

    Set_Prices()


def Buy_Cargo(tI):
    global TradedItems_Name
    global TradedItems_Price

    print(f"Buy {TradedItems_Name[tI]}!")
    Can_Buy = Silver_OnHand // TradedItems_Price[tI]
    print(f"You can afford {Can_Buy} {TradedItems_Name[tI]}.")
    Want_Buy = int(input("How much do you want to buy?"))
    if (Want_Buy > Can_Buy):
        print("Unable to complete the transaction.  Insufficient Funds!")
        User_Action = input("Press <ENTER> to continue")
    else :
        if (Player_Ship.addItem(tI, Want_Buy) == False):
            print("Unable to complete the transaction.  Check capacity!")
            User_Action = input("Press <ENTER> to continue")
        else :
            Player_Money.SpendMoney(Want_Buy * TradedItems_Price[tI])
    

def Sell_Cargo(tI):
    global TradedItems_Name
    global TradedItems_Price

    print(f"Sell {TradedItems_Name[tI]}!")

    Can_Sell = Player_Ship.getItemQty(tI)
    print(f"You can sell {Can_Sell} {TradedItems_Name[tI]}.")
    Want_Sell = int(input("How much do you want to sell?"))

    if (Player_Ship.removeItem(tI, Want_Sell) == False):
        print("Unable to complete the transaction.  Check capacity!")
        User_Action = input("Press <ENTER> to continue")
    else:
        Player_Money.AddMoney(Want_Sell * TradedItems_Price[tI])


def Buy_SelectItem():
    global TradedItems_Name

s    Cargo_ToBuy = input("What would you like to buy? [S,T,G,O]")[0].upper()
    while (Cargo_ToBuy != "S") and (Cargo_ToBuy != "T") and (Cargo_ToBuy != "G") and (Cargo_ToBuy != "O"):
        Cargo_ToBuy = input("invalid selection. \nWhat would you like to buy? [S,T,G,O]")[0].upper()

    match Cargo_ToBuy:
        case "S":
            Buy_Cargo(0)
        case "T":
            Buy_Cargo(1)
        case "G":
            Buy_Cargo(2)
        case "O":
            Buy_Cargo(3)
        case _:
            print("What?")

def Sell_SelectItem():
    global TradedItems_Name

#    Clear_Screen()
#    Show_Status()
    Cargo_ToSell = input("What would you like to sell? [S,T,G,O]")[0].upper()
    while (Cargo_ToSell != "S") and (Cargo_ToSell != "T") and (Cargo_ToSell != "G") and (Cargo_ToSell != "O"):
        Cargo_ToSell = input("invalid selection. \nWhat would you like to sell? [S,T,G,O]")[0].upper()

    match Cargo_ToSell:
        case "S":
            Sell_Cargo(0)
        case "T":
            Sell_Cargo(1)
        case "G":
            Sell_Cargo(2)
        case "O":
            Sell_Cargo(3)
        case _:
            print("What?")

def HongKong():

#    Clear_Screen()
#    Show_Status()

    User_Action = input("Would you like to visit the Money Lender, the Bank, or the Warehouse? [M,B,W]")[0].upper()

    while (User_Action != "M") and (User_Action != "B") and (User_Action != "W"):
        User_Action = input("invalid selection. \nWould you like to visit the Money Lender, the Bank, or the Warehouse? [M,B,W]")[0].upper()

    match User_Action:
        case "M":
            Visit_MoneyLender()
        case "B":
            Visit_Bank()
        case "W":
            Visit_Warehouse()
        case _:
            print("What?")


def Visit_Bank():
    global TradedItems_Name
    global TradedItems_Price
    global TradedItems_InShip

#    Clear_Screen()
#    Show_Status()

    User_Action = input("Would you like to Deposit or Withdraw? [D,W]")[0].upper()

    while (User_Action != "D") and (User_Action != "W"):
        User_Action = input("invalid selection. \nWould you like to Deposit or Withdraw? [D,W]")[0].upper()

    match User_Action:
        case "D":
            Visit_MoneyLender()
        case "W":
            Visit_Bank()
        case _:
            User_Action = input("invalid selection. \nWould you like to Deposit or Withdraw? [D,W]")[0].upper()



def Play():
    global Player_Ship

    Clear_Screen()
    Current_Port_Name = Port_Names[Current_Port]

    print("Welcome to",str(Current_Port_Name+","),Company_Name,"!\n")
    Player_Ship.print_ShipStatus()
    Player_Money.print_MoneyStatus()

    print("GOODS        PRICE     QTY IN SHIP     QTY IN WAREHOUSE\n")

    for i in range(4):
        print((TradedItems_Name[i]).ljust(9," "), ": ", str(TradedItems_Price[i]).ljust(9," "), str(Player_Ship.getItemQty(i)).ljust(15," "), TradedItems_InWarehouse[i])
    print("\n")

    
    User_Action = input("Would you like to Buy, Sell, or Travel to a new port? [B,S,T]")[0].upper()

    while (User_Action != "B") and (User_Action != "S") and (User_Action != "T"):
        User_Action = input("invalid selection. \nWould you like to Buy, Sell, or Travel to a new port? [B,S,T]")[0].upper()

    match User_Action:
        case "B":
            Buy_SelectItem()
        case "S":
            Sell_SelectItem()
        case "T":
            Travel_toPort()
        case _:
            User_Action = input("invalid selection. \nWould you like to Buy, Sell, or Travel to a new port? [B,S,T]")[0].upper()
    
# End Play()



def main():
    global Trade_Ship
    
    Trade_Ship = {'shipName':"The Peace Dividend", 'shipCapacity':15, 'shipDefense':1000}
    
    Config_Player()
    Set_Prices()
    
    while (Silver_OnHand < 10000000):
        Play()


if __name__ == "__main__":
    main()

