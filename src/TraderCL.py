import os
import random

class TradePort:
    portNames = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
    portIndex = 0
    itemName = ["Silk", "Tea", "Gunpowder", "Opium"]
    itemPrice = [0, 0, 0, 0]

    def __init__(self):
        self.portIndex = 0
        self.setPrices()
        
    def setPort(self, newIndex):
        if (self.portIndex != newIndex):
            self.portIndex = newIndex
            self.setPrices()
    
    def getPort(self):
        return(self.portIndex)

    def getPortName(self):
        return(self.portNames[self.portIndex])
        
    def print_PortNameList(self):
        print(*self.portNames,sep=", ")

    def setPrices(self):
        self.itemPrice = [random.randrange(5, 45, 1), random.randrange(2, 25, 1), random.randrange(5, 75, 1), random.randrange(300, 999, 1)]

    def getItemPrice(self,getIndex):
        return(self.itemPrice[getIndex])

    def getItemName(self,getIndex):
        return(self.itemName[getIndex])


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

    def GetCashOnHand(self):
        return (self.onHand)


class Ship:
    itemName = ["Silk", "Tea", "Gunpowder", "Opium"]
    itemQty = [0, 0, 0, 0]
    shipStatus = 100
    shipDefense = 100
    shipMaximumCapacity = 15
    shipAvailableCapacity = 15
    
    def __init__(self, name):
        self.name = name
    
    def print_ShipStatus(self):
        print("Ship Name     :", self.name)
        print("Ship Capacity :", self.shipAvailableCapacity, "/", self.shipMaximumCapacity)
        print("Ship Defense  :", self.shipDefense)
        print("Ship Status   :", self.shipStatus,"\n")

    def getItemQty(self, index):
        return (self.itemQty[index])

    def getAvailableCapacity(self):
        return (self.shipAvailableCapacity)
    
    def setCapacity(self,newCap):
        self.shipMaximumCapacity = newCap
    
    def addItem(self, index, amount2add):
        retVal = False
        if (amount2add > self.shipAvailableCapacity) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] + amount2add)
            self.shipAvailableCapacity = (self.shipAvailableCapacity - amount2add)
            retVal = True
        return retVal
    
    def removeItem(self, index, amount2rem):
        retVal = False
        if (amount2rem > self.itemQty[index]) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] - amount2rem)
            self.shipAvailableCapacity = (self.shipAvailableCapacity + amount2rem)
            retVal = True
        return retVal
    
global Company_Name
global Port_Names               # Constant? 
global TradedItems_InWarehouse
global Current_Port
global Current_Port_Name
global User_Action
global Player_Ship
global Player_Money
global Player_Port

Port_Names = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
Current_Port = 0



def Clear_Screen():
    os.system('cls')
    
def Config_Player():
    global Company_Name
    global Silver_OnHand
    global Silver_InBank
    global TradedItems_InWarehouse
    global Player_Ship
    global Player_Money
    global Player_Port

    Clear_Screen()
    Player_Port = TradePort()
    Player_Ship = Ship("The Peace Dividend")
    Player_Money = Money(1000)

    print("Welcome to the East Empire Trading Simulation!\n")
    Company_Name = input("What shall we use for a company name?\n")
    Silver_OnHand = 1000
    Silver_InBank = 0
    TradedItems_InWarehouse = [0, 0, 0, 0]



def Travel_toPort():
    global Current_Port

#    print(f"You may travel to these ports:")
    Player_Port.print_PortNameList()


    Port_Desired = input("Where would you like to go? [H,B,C,J,M,P,R,S]")[0].upper()
    while (Port_Desired != "H") and (Port_Desired != "B") and (Port_Desired != "C") and (Port_Desired != "J") and (Port_Desired != "M") and (Port_Desired != "P") and (Port_Desired != "R") and (Port_Desired != "S"):
        Port_Desired = input("invalid selection. \nWhere would you like to go? [H,B,C,J,M,P,R,S]")[0].upper()

    match Port_Desired:
        case "H":
            Current_Port = 0
            Player_Port.setPort(0)
        case "B":
            Current_Port = 1
            Player_Port.setPort(1)
        case "C":
            Current_Port = 2
            Player_Port.setPort(2)
        case "J":
            Current_Port = 3
            Player_Port.setPort(3)
        case "M":
            Current_Port = 4
            Player_Port.setPort(4)
        case "P":
            Current_Port = 5
            Player_Port.setPort(5)
        case "R":
            Current_Port = 6
            Player_Port.setPort(6)
        case "S":
            Current_Port = 7
            Player_Port.setPort(7)



def Buy_Cargo(tI):

    print(f"Buy {Player_Port.getItemName(tI)}!")
    Can_Buy = Player_Money.GetCashOnHand() // Player_Port.getItemPrice(tI)
    print(f"You can afford {Can_Buy} {Player_Port.getItemName(tI)}.")
    Want_Buy = int(input("How much do you want to buy?"))
    if (Want_Buy > Can_Buy):
        print("Unable to complete the transaction.  Insufficient Funds!")
        User_Action = input("Press <ENTER> to continue")
    else :
        if (Player_Ship.addItem(tI, Want_Buy) == False):
            print("Unable to complete the transaction.  Check capacity!")
            User_Action = input("Press <ENTER> to continue")
        else :
            Player_Money.SpendMoney(Want_Buy * Player_Port.getItemPrice(tI))
    

def Sell_Cargo(tI):

    print(f"Sell {Player_Port.getItemName(tI)}!")

    Can_Sell = Player_Ship.getItemQty(tI)
    print(f"You can sell {Can_Sell} {Player_Port.getItemName(tI)}.")
    Want_Sell = int(input("How much do you want to sell?"))

    if (Want_Sell > Can_Sell):
        print("Unable to complete the transaction.  Insufficient Items!")
        User_Action = input("Press <ENTER> to continue")
    else :
        if (Player_Ship.removeItem(tI, Want_Sell) == False):
            print("Unable to complete the transaction.  Check capacity!")
            User_Action = input("Press <ENTER> to continue")
        else:
            Player_Money.AddMoney(Want_Sell * Player_Port.getItemPrice(tI))


def Buy_SelectItem():

    Cargo_ToBuy = input("What would you like to buy? [S,T,G,O]")[0].upper()
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

    Clear_Screen()
    Current_Port_Name = Port_Names[Current_Port]

    print("Welcome to",str(Player_Port.getPortName()+","),Company_Name,"!\n")
    Player_Ship.print_ShipStatus()
    Player_Money.print_MoneyStatus()

    print("GOODS        PRICE     QTY IN SHIP     QTY IN WAREHOUSE")
    print("=====        =====     ===========     ================")

    for i in range(4):
        print((Player_Port.getItemName(i)).ljust(9," "), ": ", str(Player_Port.getItemPrice(i)).ljust(9," "), str(Player_Ship.getItemQty(i)).ljust(15," "), TradedItems_InWarehouse[i])

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
  
    Config_Player()
    
    while (Silver_OnHand < 10000000):
        Play()


if __name__ == "__main__":
    main()

