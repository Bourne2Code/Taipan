import os
import math
import random
# import colorama but as cr, as cr is easier to use.
import colorama as cr
cr.init(autoreset=True)

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
        print("Gold in Debt :", round(self.inDebt),"\n")

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

    def DepositMoney(self,gold2dep):
        retVal = False
        if (int(gold2dep) > int(self.onHand)):
            print("Too much!")
        else : 
            self.onHand = (self.onHand - gold2dep)
            self.inBank = (self.inBank + gold2dep)
            retVal = True
        return(retVal)

    def WithdrawMoney(self,gold2wd):
        retVal = False
        if (int(gold2wd) > int(self.inBank)):
            print("Too much!")
        else : 
            self.onHand = (self.onHand + gold2wd)
            self.inBank = (self.inBank - gold2wd)
            retVal = True
        return(retVal)

    def BorrowMoney(self,gold2borrow):
        retVal = False
        if ((self.inDebt + gold2borrow) > 1000):
            print("Too much! 1000 Max")
        else : 
            self.onHand = (self.onHand + gold2borrow)
            self.inDebt = (self.inDebt + gold2borrow)
            retVal = True
        return(retVal)

    def CompoundDebt(self):
        self.inDebt = (self.inDebt + (self.inDebt *.01))

    def RepayMoney(self,gold2repay):
        retVal = False
        if (self.onHand < gold2repay):
            print("Too much! Check cash on hand")
        elif (round(self.inDebt) < gold2repay):
            print("Too much! Overpayment!")
        else : 
            self.inDebt = round(self.inDebt)
            self.onHand = (self.onHand - gold2repay)
            self.inDebt = (self.inDebt - gold2repay)
            retVal = True
        return(retVal)


class Ship:
    itemName = ["Silk", "Tea", "Gunpowder", "Opium"]
    itemQty = [0, 0, 0, 0]
    whItemQty = [0, 0, 0, 0]
    shipMaxDefense = 200
    shipDefense = 200
    shipGuns = 5
    shipMaximumCapacity = 25
    shipAvailableCapacity = 25
    whouseMaximumCapacity = 1000
    whouseAvailableCapacity = 1000
    
    def __init__(self, name):
        self.name = name
    
    def print_ShipStatus(self):
        print("Ship Name     :", self.name)
        print("Ship Capacity :", self.shipAvailableCapacity, "/", self.shipMaximumCapacity)
        print("Ship Defense  :", self.shipDefense, "/", self.shipMaxDefense)
#        print("Ship Status   :", self.shipStatus)
        print("Warehouse Cap.:", self.whouseAvailableCapacity, "/", self.whouseMaximumCapacity,"\n")

    def getItemQty(self, index):
        return (self.itemQty[index])

    def getWHouseItemQty(self, index):
        return (self.whItemQty[index])

    def getItemName(self,index):
        return(self.itemName[index])

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

    def storeItem(self, index, amount2store):
        retVal = False
        if (amount2store > self.itemQty[index]) or (amount2store > self.whouseAvailableCapacity) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] - amount2store)
            self.whItemQty[index] = (self.whItemQty[index] + amount2store)
            self.shipAvailableCapacity = (self.shipAvailableCapacity + amount2store)
            self.whouseAvailableCapacity = (self.whouseAvailableCapacity - amount2store)
            retVal = True
        return retVal

    def retrieveItem(self, index, amount2retrieve):
        retVal = False
        if (amount2retrieve > self.whItemQty[index]) or (amount2retrieve > self.shipAvailableCapacity) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] + amount2retrieve)
            self.whItemQty[index] = (self.whItemQty[index] - amount2retrieve)
            self.shipAvailableCapacity = (self.shipAvailableCapacity - amount2retrieve)
            self.whouseAvailableCapacity = (self.whouseAvailableCapacity + amount2retrieve)
            retVal = True
        return retVal

    def damageShip(self,Damage):
        self.shipDefense = (self.shipDefense - Damage)




    
global Company_Name
global User_Action
global Player_Ship
global Player_Money
global Player_Port



def Clear_Screen():
    os.system('cls')

    
def Config_Player():
    global Company_Name
    global Player_Ship
    global Player_Money
    global Player_Port

    Clear_Screen()
    Player_Port = TradePort()
    Player_Ship = Ship("The Peace Dividend")
    Player_Money = Money(1000)

    print("Welcome to the East Empire Trading Simulation!\n")
    Company_Name = input("What shall we use for a company name?\n")



def Ship_UnderAttack():

    underAttack = True
    shipCount = random.randrange(1, 10, 1)

    while (underAttack):
        print("We are under attack by ", shipCount, "ships!")
        print(f"{cr.Fore.WHITE}Shall we {cr.Fore.GREEN}F{cr.Fore.WHITE}ight or {cr.Fore.GREEN}R{cr.Fore.WHITE}un?\n")
        Fight = input("[F,R]")[0].upper()
        while (Fight not in "FR"):
            print(f"{cr.Fore.YELLOW}Invalid Selection!\n{cr.Fore.WHITE}We're under attack.  Shall we {cr.Fore.GREEN}F{cr.Fore.WHITE}ight or {cr.Fore.GREEN}R{cr.Fore.WHITE}un?\n")
            Fight = input("[F,R]")[0].upper()

        if (Fight == "F"):
            shipsSunk = int(random.randrange(1, 4, 1))
            shipCount = shipCount - shipsSunk
            shipDamage = int(random.randrange(1, 25, 1))
            Player_Ship.damageShip(int(random.randrange(1, 25, 1)))
            if (shipCount < 1):
                print(f"{cr.Fore.WHITE}We have sunk all attacking ships!")
                underAttack = False
            else :
                print(f"{cr.Fore.WHITE}We have sunk ", shipsSunk, "ships!")
        else :
            outRun = random.randrange(1, 4, 1)
            if (outRun == shipCount):
                shipDamage = int(random.randrange(1, 20, 1))
                underAttack = False
                print(f"{cr.Fore.WHITE}We have escaped!")
        
    
    

def Travel_toPort():

    Port_Desired = ""

    Player_Port.print_PortNameList()
    Port_Desired = input("Where would you like to go? [H,B,C,J,M,P,R,S]")
    if (len(Port_Desired) > 0) :
        Port_Desired = Port_Desired.upper()

    match Port_Desired:
        case "H":
            Player_Port.setPort(0)
        case "B":
            Player_Port.setPort(1)
        case "C":
            Player_Port.setPort(2)
        case "J":
            Player_Port.setPort(3)
        case "M":
            Player_Port.setPort(4)
        case "P":
            Player_Port.setPort(5)
        case "R":
            Player_Port.setPort(6)
        case "S":
            Player_Port.setPort(7)

    Attack = random.randrange(1, 10, 1)
    if (Attack == 6):
        Ship_UnderAttack()

def Buy_Cargo(bIndex):

    print(f"Buy {Player_Port.getItemName(bIndex)}!")
    Can_Buy = Player_Money.GetCashOnHand() // Player_Port.getItemPrice(bIndex)
    print(f"You can afford {Can_Buy} {Player_Port.getItemName(bIndex)}.")
    Want_Buy = int(input("How much do you want to buy?"))
    if (Want_Buy > Can_Buy):
        print("Unable to complete the transaction.  Insufficient Funds!")
        User_Action = input("Press <ENTER> to continue")
    else :
        if (Player_Ship.addItem(bIndex, Want_Buy) == False):
            print("Unable to complete the transaction.  Check capacity!")
            User_Action = input("Press <ENTER> to continue")
        else :
            Player_Money.SpendMoney(Want_Buy * Player_Port.getItemPrice(bIndex))
    

def Sell_Cargo(sIndex):

    print(f"Sell {Player_Port.getItemName(sIndex)}!")

    Can_Sell = Player_Ship.getItemQty(sIndex)
    print(f"You can sell {Can_Sell} {Player_Port.getItemName(sIndex)}.")
    Want_Sell = int(input("How much do you want to sell?"))

    if (Player_Ship.removeItem(sIndex, Want_Sell) == False):
        print("Unable to complete the transaction.  Check capacity!")
        User_Action = input("Press <ENTER> to continue")
    else:
        Player_Money.AddMoney(Want_Sell * Player_Port.getItemPrice(sIndex))


def Buy_SelectItem():

    print(f"Would you like to buy {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
    Cargo_ToBuy = input("[S,T,G,O]")
    if (len(Cargo_ToBuy) > 0) :
        Cargo_ToBuy = Cargo_ToBuy.upper()

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
            print(f"{cr.Fore.YELLOW}Invalid Selection! Press <ENTER> to continue")
            User_Action = input("")

def Sell_SelectItem():

    print(f"Would you like to sell {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
    Cargo_ToSell = input("[S,T,G,O]")
    if (len(Cargo_ToSell) > 0) :
        Cargo_ToSell = Cargo_ToSell.upper()

    while (Cargo_ToSell != "S") and (Cargo_ToSell != "T") and (Cargo_ToSell != "G") and (Cargo_ToSell != "O"):
        print(f"{cr.Fore.YELLOW}Invalid Selection! \n{cr.Fore.WHITE}Would you like to sell {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")[0].upper()
        Cargo_ToSell = input("[S,T,G,O]")[0].upper()

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
            User_Action = input("Press <ENTER> to continue")


def Visit_Bank():
    x_Amount = 0

    print(f"Would you like to {cr.Fore.GREEN}D{cr.Fore.WHITE}eposit, {cr.Fore.GREEN}W{cr.Fore.WHITE}ithdraw, {cr.Fore.GREEN}B{cr.Fore.WHITE}orrow or {cr.Fore.GREEN}R{cr.Fore.WHITE}epay?")
    Bank_Action = input("[D,W,B,R]")
    if (len(Bank_Action) > 0) :
        Bank_Action = Bank_Action.upper()

    while (Bank_Action not in "DWBR"):
        print(f"{cr.Fore.YELLOW}Invalid Selection! \n{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}D{cr.Fore.WHITE}eposit, {cr.Fore.GREEN}W{cr.Fore.WHITE}ithdraw, {cr.Fore.GREEN}B{cr.Fore.WHITE}orrow or {cr.Fore.GREEN}R{cr.Fore.WHITE}epay?")[0].upper()
        Bank_Action = input("[D,W,B,R]")[0].upper()

    match Bank_Action:
        case "D":
            x_Amount = int(input("How much would you like to deposit?"))
            if (Player_Money.DepositMoney(x_Amount) == False):
                print("Unable to complete the transaction.  Check cash on hand!")
                Bank_Action = input("Press <ENTER> to continue")

        case "W":
            x_Amount = int(input("How much would you like to withdraw?"))
            if (Player_Money.WithdrawMoney(x_Amount) == False):
                print("Unable to complete the transaction.  Check cash in bank!")
                Bank_Action = input("Press <ENTER> to continue")

        case "B":
            x_Amount = int(input("How much would you like to borrow?"))
            if (Player_Money.BorrowMoney(x_Amount) == False):
                print("Unable to complete the transaction.  1000 Max!")
                Bank_Action = input("Press <ENTER> to continue")

        case "R":
            x_Amount = int(input("How much would you like to repay?"))
            if (Player_Money.RepayMoney(x_Amount) == False):
                print("Unable to complete the transaction.  Check cash on hand!")
                Bank_Action = input("Press <ENTER> to continue")


def Store_Cargo(sIndex):

    Can_Store = Player_Ship.getItemQty(sIndex)
    print(f"You can store {Can_Store} {Player_Ship.getItemName(sIndex)}.")
    Want_Store = int(input("How much do you want to store?"))

    print(f"Store {Player_Ship.getItemName(sIndex)}!")

    if (Player_Ship.storeItem(sIndex, Want_Store) == False):
        print("Unable to complete the transaction.  Check cargo!")
        User_Action = input("Press <ENTER> to continue")


def Store_SelectItem():

    print(f"{cr.Fore.WHITE}Would you like to store {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
    Cargo_ToStore = input("[S,T,G,O]")
    if (len(Cargo_ToStore) > 0) :
        Cargo_ToStore = Cargo_ToStore.upper()

    while (Cargo_ToStore not in "STGO"):
        print(f"{cr.Fore.YELLOW}Invalid Selection! \{cr.Fore.WHITE}nWould you like to store {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
        Cargo_ToStore = input("[S,T,G,O]")[0].upper()

    match Cargo_ToStore:
        case "S":
            Store_Cargo(0)
        case "T":
            Store_Cargo(1)
        case "G":
            Store_Cargo(2)
        case "O":
            Store_Cargo(3)


def Retrieve_Cargo(rIndex):

    Can_Retrieve = Player_Ship.getWHouseItemQty(rIndex)
    print(f"You can retrieve {Can_Retrieve} {Player_Ship.getItemName(rIndex)}.")
    Want_Retrieve = int(input("How much do you want to retrieve?"))

    print(f"Retrieve {Player_Ship.getItemName(rIndex)}!")

    if (Player_Ship.retrieveItem(rIndex, Want_Retrieve) == False):
        print("Unable to complete the transaction.  Check cargo!")
        User_Action = input("Press <ENTER> to continue")


def Retrieve_SelectItem():

    print(f"{cr.Fore.WHITE}Would you like to retrieve {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
    Cargo_ToRetrieve = input("[S,T,G,O]")
    if (len(Cargo_ToRetrieve) > 0) :
        Cargo_ToRetrieve = Cargo_ToRetrieve.upper()

    while (Cargo_ToRetrieve not in "STGO"):
        print(f"{cr.Fore.YELLOW}Invalid Selection! \n{cr.Fore.WHITE}Would you like to retrieve {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
        Cargo_ToRetrieve = input("[S,T,G,O]")[0].upper()

    match Cargo_ToRetrieve:
        case "S":
            Retrieve_Cargo(0)
        case "T":
            Retrieve_Cargo(1)
        case "G":
            Retrieve_Cargo(2)
        case "O":
            Retrieve_Cargo(3)


def Use_Warehouse():
    xfer_Amount = 0
    xfer_Item = 0

    print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}S{cr.Fore.WHITE}tore or {cr.Fore.GREEN}R{cr.Fore.WHITE}etrieve items from the warehouse?")
    User_Action = input("[S,R]")
    if (len(User_Action) > 0) :
        User_Action = User_Action.upper()

    while (User_Action not in "SR"):
        print(f"{cr.Fore.YELLOW}Invalid Selection! \n{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}S{cr.Fore.WHITE}tore or {cr.Fore.GREEN}R{cr.Fore.WHITE}etrieve items from the warehouse?")

    match User_Action:
        case "S":
            Store_SelectItem()
        case "R":
            Retrieve_SelectItem()


def Play():

    Clear_Screen()
    print(f"{cr.Fore.GREEN}Welcome to " + str(Player_Port.getPortName()) + ", " + Company_Name + "!\n")
    
    Player_Ship.print_ShipStatus()
    Player_Money.print_MoneyStatus()


    print("GOODS        PRICE     QTY IN SHIP     QTY IN WAREHOUSE")
    print("=====        =====     ===========     ================")

    for i in range(4):
        print((Player_Port.getItemName(i)).ljust(9," "), ": ", str(Player_Port.getItemPrice(i)).ljust(9," "), str(Player_Ship.getItemQty(i)).ljust(15," "), str(Player_Ship.getWHouseItemQty(i)))

    print("\n")
    if (Player_Port.getPort() == 0):
        print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, {cr.Fore.GREEN}V{cr.Fore.WHITE}isit the Bank, use the {cr.Fore.GREEN}W{cr.Fore.WHITE}arehouse or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
        User_Action = input("[B,S,V,W,T]")
    
        if (len(User_Action) > 0) :
            User_Action = User_Action.upper()

        while (User_Action not in "BSVWT"):
            print(f"{cr.Fore.YELLOW}Invalid Selection! \n{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, {cr.Fore.GREEN}V{cr.Fore.WHITE}isit the Bank, use the {cr.Fore.GREEN}W{cr.Fore.WHITE}arehouse or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
            User_Action = input("[B,S,V,W,T]")[0].upper()
    
        match User_Action:
            case "B":
                Buy_SelectItem()
            case "S":
                Sell_SelectItem()
            case "V":
                Visit_Bank()
            case "W":
                Use_Warehouse()
            case "T":
                Travel_toPort()
            case _:
                User_Action = input("Press <ENTER> to continue")

    
    else:
        print(f"Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
        User_Action = input("[B,S,T]")[0].upper()
  
        while (User_Action not in "BST"):
            print(f"{cr.Fore.YELLOW}Invalid Selection! \n{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
            User_Action = input("[B,S,T]")[0].upper()
  
        match User_Action:
            case "B":
                Buy_SelectItem()
            case "S":
                Sell_SelectItem()
            case "T":
                Travel_toPort()
    
# End Play()



def main():
    Silver_OnHand = 1000
  
    Config_Player()
    
    while (Silver_OnHand < 10000000):
        Play()


if __name__ == "__main__":
    main()

