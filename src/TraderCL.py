import os
import math
import random
# import colorama but as cr, as cr is easier to use.
import colorama as cr
cr.init(autoreset=True)

class tradeItemList:
# lists = index 0 - 3
    itemName = ["Silk", "Tea", "Gunpowder", "Opium"]
    itemPrice = [0, 0, 0, 0]

    def __init__(self):
        self.SetPrices()

    def SetPrices(self):
        self.itemPrice = [random.randrange(5, 45, 1), random.randrange(2, 25, 1), random.randrange(5, 75, 1), random.randrange(300, 999, 1)]

    def GetItemPrice(self,index):
        return(self.itemPrice[index])

    def GetItemName(self,index):
        return(self.itemName[index])

class tradePort:
    portNames = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
    portIndex = 0

    def __init__(self):
        self.portIndex = 0
        
    def setPort(self, newIndex):
        if (self.portIndex != newIndex):
            self.portIndex = newIndex
    
    def getPort(self):
        return(self.portIndex)

    def getPortName(self):
        return(self.portNames[self.portIndex])
        
    def getPortNameList(self):
        portNames = ""
        needComma = False
        for i in range(len(self.portNames)):
            if (i != self.portIndex):
                if (needComma == True):
                    portNames = portNames + ", "
                portNames = portNames + self.portNames[i]
                needComma = True
        return(portNames)

    def getPortCharList(self):
        portChars = ""
        needComma = False
        for i in range(len(self.portNames)):
            if (i != self.portIndex):
                if (needComma == True):
                    portChars = portChars + ","
                portChars = portChars + self.portNames[i][0]
                needComma = True
        return(portChars)


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

    def GetCashInBank(self):
        return (self.inBank)

    def GetCashInDebt(self):
        return (self.inDebt)

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


class Warehouse:
    whseItemName = ["Silk", "Tea", "Gunpowder", "Opium"]
    whseItemQty = [0, 0, 0, 0]
    whseMaxCapacity = 1000

    def __init__(self, name):
        self.name = name

    def GetCurrentCapacity(self):
        return (self.whseMaxCapacity - self.whseItemQty[0] - self.whseItemQty[1] - self.whseItemQty[2] - self.whseItemQty[3])

    def GetMaxCapacity(self):
        return(self.whseMaxCapacity)

    def GetUsedCapacity(self):
        return (self.whseItemQty[0] + self.whseItemQty[1] + self.whseItemQty[2] + self.whseItemQty[3])

    def GetItemQty(self, index):
        return(self.whseItemQty[index])

    def StoreItem(self, index, qty2Store):
        retVal = False
        if (qty2Store <= self.GetCurrentCapacity()) :
            self.whseItemQty[index] = (self.whseItemQty[index] + qty2Store)
            retVal = True
        return (retVal)

    def RetrieveItem(self, index, qty2Retrieve):
        retVal = False
        if (qty2Retrieve <= self.whseItemQty[index]) :
            self.whseItemQty[index] = (self.whseItemQty[index] - qty2Retrieve)
            retVal = True
        return retVal


class Ship:
    itemName = ["Silk", "Tea", "Gunpowder", "Opium"]
    itemQty = [0, 0, 0, 0]
    shipMaxDefense = 500
    shipDefense = 500
    shipGuns = 5
    shipMaximumCapacity = 25
    shipAvailableCapacity = 25
    
    def __init__(self, name):
        self.name = name
    
    def getShipName(self):
        return (self.name)
        
    def getShipDefense(self):
        return (self.shipDefense)

    def getShipMaxDefense(self):
        return (self.shipMaxDefense)
    
    def getDamage(self):
        return (self.shipMaxDefense-self.shipDefense)

    def getItemQty(self, index):
        return (self.itemQty[index])
        
    def getTotalWeight(self):
        return(self.itemQty[0] + self.itemQty[1] + self.itemQty[2] + self.itemQty[3])

    def getItemName(self,index):
        return(self.itemName[index])

    def getShipCapacity(self):
        return(round(self.shipMaximumCapacity * (self.shipDefense / self.shipMaxDefense)))

    def getShipMaxCapacity(self):
        return(self.shipMaximumCapacity)
        
    def getShipCurrentCapacity(self):
        return(self.getShipCapacity() - self.itemQty[0] - self.itemQty[1] - self.itemQty[2] - self.itemQty[3])
    
    def setCapacity(self,newCap):
        self.shipMaximumCapacity = newCap
    
    def addItem(self, index, amount2add):
        retVal = False
        if (amount2add > self.getShipCurrentCapacity()) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] + amount2add)
            retVal = True
        return retVal
    
    def removeItem(self, index, amount2rem):
        retVal = False
        if (amount2rem > self.itemQty[index]) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] - amount2rem)
            retVal = True
        return retVal

    def damageShip(self,Damage):
        self.shipDefense = (self.shipDefense - Damage)
        if (self.getTotalWeight() > self.getShipCapacity()):
            while (self.getTotalWeight() > self.getShipCapacity()) and (self.getItemQty(1) > 0):
                self.removeItem(1,1);
        if (self.getTotalWeight() > self.getShipCapacity()):
            while (self.getTotalWeight() > self.getShipCapacity()) and (self.getItemQty(2) > 0):
                self.removeItem(2,1);
        if (self.getTotalWeight() > self.getShipCapacity()):
            while (self.getTotalWeight() > self.getShipCapacity()) and (self.getItemQty(0) > 0):
                self.removeItem(0,1);
        if (self.getTotalWeight() > self.getShipCapacity()):
            while (self.getTotalWeight() > self.getShipCapacity()) and (self.getItemQty(3) > 0):
                self.removeItem(3,1);
        

    def repairShip(self,Repair):
        self.shipDefense = (self.shipDefense + Repair)
        if (self.shipDefense > self.shipMaxDefense):
            self.shipDefense = self.shipMaxDefense

    def Attack(self):
        return(int(self.shipGuns * random.randrange(5, 50, 5)))
        

    
global Company_Name
global User_Action
global Game_Items
global Game_Port
global Player_Ship
global Player_Money
global Player_WHouse



def Clear_Screen():
    os.system('cls')

    
def Config_Player():
    global Company_Name
    global Game_Items
    global Game_Port
    global Player_Ship
    global Player_Money
    global Player_WHouse

    Clear_Screen()
    print("Welcome to the East Empire Trading Simulation!\n")
    Company_Name = input("What shall we use for a company name?\n")
    
    Game_Items = tradeItemList()
    
    Game_Port = tradePort()
    Player_Ship = Ship(Company_Name)
    Player_Money = Money(1000)
    Player_WHouse = Warehouse("My Warehouse")



def Print_PirateShips(pirateQty):

    line01 ="  _  _                  "
    line02 ="   \/      ]▓▓▓         "
    line03 ="       ____|_____       "
    line04 ="     /           /      "
    line05 ="     |           |      "
    line06 ="     \           \      "
    line07 ="      \___________\     "
    line08 ="  \ _______||__________ "
    line09 ="   \|_|_O_|_|_O_|_|_O_| "
    line10 ="^^%%\_,,_.,.  ,, ..,/   "
    line11 ="%^!^^^!!^^^%%%%%!!!!^^^%"


    pline01 = line01 
    pline02 = line02 
    pline03 = line03 
    pline04 = line04 
    pline05 = line05 
    pline06 = line06 
    pline07 = line07 
    pline08 = line08 
    pline09 = line09 
    pline10 = line10 
    pline11 = line11 


    if (pirateQty > 1):

        pline01 = pline01 + line01
        pline02 = pline02 + line02
        pline03 = pline03 + line03
        pline04 = pline04 + line04
        pline05 = pline05 + line05
        pline06 = pline06 + line06
        pline07 = pline07 + line07
        pline08 = pline08 + line08
        pline09 = pline09 + line09
        pline10 = pline10 + line10
        pline11 = pline11 + line11

    if (pirateQty > 2):

        pline01 = pline01 + line01
        pline02 = pline02 + line02
        pline03 = pline03 + line03
        pline04 = pline04 + line04
        pline05 = pline05 + line05
        pline06 = pline06 + line06
        pline07 = pline07 + line07
        pline08 = pline08 + line08
        pline09 = pline09 + line09
        pline10 = pline10 + line10
        pline11 = pline11 + line11
 
    print(pline01)
    print(pline02)
    print(pline03)
    print(pline04)
    print(pline05)
    print(pline06)
    print(pline07)
    print(f"{cr.Fore.YELLOW}"+pline08)
    print(f"{cr.Fore.YELLOW}"+pline09)
    print(f"{cr.Fore.BLUE}"+pline10)
    print(f"{cr.Fore.BLUE}"+pline11)
    

#
# ┌───────────────────────────────────────────────────────────────────────┐
# │                 Company Name  : The Peace Dividend                    │
# │ ┌────────────────────────────────────┐                                │
# │ │ Hong Kong Warehouse                │              Date              │
# │ │     Silk        10,000   In Use    │           99 JAN 1860          │
# │ │     Tea         0         0        │                                │
# │ │     Gunpowder   0        Vacant    │            Location            │
# │ │     Opium       0         10,000   │            Hong Kong           │
# │ └────────────────────────────────────┘                                │
# │ ┌────────────────────────────────────┐              Debt              │
# │ │ Ship's Hold 60          Guns 5     │               0                │
# │ │     Silk        0                  │                                │
# │ │     Tea         0                  │           Ship Status          │
# │ │     Gunpowder   0                  │              100%              │
# │ │     Opium       0                  │                                │
# │ └────────────────────────────────────┘                                │
# │  Cash: 1,000,000     Bank: 1,000,000                                  │
# └───────────────────────────────────────────────────────────────────────┘
# Present prices per unit here are:
#      Opium: 5500    Silk: 550
#      Arms : 60       Gunpowder: 15
#
#Gold On Hand : 1,000,000
#Gold in Bank : 0        
#Gold in Debt : 0        

def print_GameStatus() :
    print(f"{cr.Fore.GREEN} ┌───────────────────────────────────────────────────────────────────────┐")
    print(f"{cr.Fore.GREEN} │ " + ("Firm: " + Player_Ship.getShipName()).center(70) + "│")
    print(f"{cr.Fore.GREEN} │ ┌────────────────────────────────────┐                                │")
    print(f"{cr.Fore.GREEN} │ │ Hong Kong Warehouse                │              Date              │")
    print(f"{cr.Fore.GREEN} │ │     Silk        " + str(Player_WHouse.GetItemQty(0)).ljust(9) + "In Use:   │           99 JAN 1860          │")
    print(f"{cr.Fore.GREEN} │ │     Tea         " + str(Player_WHouse.GetItemQty(1)).ljust(10) +  str(Player_WHouse.GetUsedCapacity()).ljust(9) + "│                                │")
    print(f"{cr.Fore.GREEN} │ │     Gunpowder   " + str(Player_WHouse.GetItemQty(2)).ljust(9) + "Vacant:   │             Location           │")

    tmpVal = "{:,}".format(Player_WHouse.GetCurrentCapacity())
    print(f"{cr.Fore.GREEN} │ │     Opium       " + str(Player_WHouse.GetItemQty(3)).ljust(10) +  tmpVal.ljust(9) + "│            Hong Kong           │")
    print(f"{cr.Fore.GREEN} │ └────────────────────────────────────┘                                │")


#   Port: {cr.Fore.WHITE}" + Game_Port.getPortName().ljust(46," "),end="")


#   print(f"{cr.Fore.GREEN} │ Port: {cr.Fore.WHITE}" + Game_Port.getPortName().ljust(46," "),end="")



#    print(f"{cr.Fore.GREEN}Date: {cr.Fore.WHITE}" +"99 JAN 1860",end="")
#    print(f"{cr.Fore.GREEN} │")
#    print(f"{cr.Fore.GREEN} │ ┌────────────────────────────────────┐   ┌──────────────────────────┐ │")
#    print(f"{cr.Fore.GREEN} │ │ Company Name  : {cr.Fore.WHITE}" + Player_Ship.getShipName().ljust(19," "),end="")
#    print(f"{cr.Fore.GREEN}│   │ Gold On Hand : {cr.Fore.WHITE}" + str(Player_Money.GetCashOnHand()).ljust(9," "),end="")
#    print(f"{cr.Fore.GREEN} │ │")
#    print(f"{cr.Fore.GREEN} │ │ Ship Capacity : {cr.Fore.WHITE}" + (str(Player_Ship.getShipCapacity())+ " / " + str(Player_Ship.getShipMaxCapacity())).ljust(19," "),end="")
#    print(f"{cr.Fore.GREEN}│   │ Gold in Bank : {cr.Fore.WHITE}" + str(Player_Money.GetCashInBank()).ljust(9," "),end="")
#    print(f"{cr.Fore.GREEN} │ │")
#    print(f"{cr.Fore.GREEN} │ │ Ship Status   : {cr.Fore.WHITE}" + (str(Player_Ship.getShipDefense()) + " / " + str(Player_Ship.getShipMaxDefense())).ljust(19," "),end="")
#    print(f"{cr.Fore.GREEN}│   │ Gold in Debt : {cr.Fore.YELLOW}" + (str(round(Player_Money.GetCashInDebt()))).ljust(9," "),end="")
#    print(f"{cr.Fore.GREEN} │ │")
#    print(f"{cr.Fore.GREEN} │ └────────────────────────────────────┘   └──────────────────────────┘ │")



#    print("Ship Name     :", Player_Ship.getShipName())
#    print("Ship Capacity :", Player_Ship.getShipCapacity(), "/", Player_Ship.getShipCapacity())
    print("Ship Defense  :", Player_Ship.getShipDefense(), "/", Player_Ship.getShipMaxDefense())
    print("Warehouse Cap.:", str(Player_WHouse.GetCurrentCapacity()), "/", str(Player_WHouse.GetMaxCapacity()),"\n")
    print("Gold On Hand :", Player_Money.GetCashOnHand())
    print("Gold in Bank :", Player_Money.GetCashInBank())
    print("Gold in Debt :", round(Player_Money.GetCashInDebt()),"\n")




def Ship_UnderAttack():

    underAttack = True
    piratesInitial = random.randrange(1, 15, 1)
    piratesDefense = (piratesInitial * 100)
    piratesLeft = piratesInitial   # use piratesInitial to calculate the flotsam and jetsam.  more ships = greater reward
    while (underAttack):
        Clear_Screen()
        shipDamage = int(random.randrange(1, 15, 1))
        Player_Ship.damageShip(shipDamage)
        print_GameStatus()

        Print_PirateShips(piratesLeft)

        print(f"We are under attack by{cr.Fore.YELLOW} " + str(piratesLeft), end=" ")
        print(f"{cr.Fore.WHITE}ships!")
#        print("Defense: "+str(piratesDefense))
#        print("Start Ships: "+str(piratesInitial))
#        print("Ships Left: "+str(piratesLeft))
        print(f"We have sustained{cr.Fore.YELLOW} " + str(shipDamage), end=" ")
        print(f"{cr.Fore.WHITE}damage to our defense.")
        RunFight = ""
        while (RunFight != "F") and (RunFight != "R"):
            print(f"We're under attack.  Shall we {cr.Fore.GREEN}F{cr.Fore.WHITE}ight or {cr.Fore.GREEN}R{cr.Fore.WHITE}un?")
            RunFight = input("[F,R]")
            if (len(RunFight)> 0) :
                RunFight = RunFight[0].upper()

        if (RunFight == "F"):
            piratesDefense = (piratesDefense - Player_Ship.Attack())
            piratesLeft = (piratesDefense // 100)
            if (piratesLeft < 1):
                print(f"{cr.Fore.WHITE}Victory!  We have sunk all of the attacking ships!")
                FlotsamQty = int(random.randrange(1, piratesInitial, 1))
                FlotsamItem = int(random.randrange(1, 4, 1))
                print("We have recovered some flotsam and jetsam.",FlotsamQty, "of",Player_Ship.getItemName(FlotsamItem))
                if (FlotsamQty > Player_Ship.shipAvailableCapacity):
                    FlotsamQty = Player_Ship.shipAvailableCapacity
                Player_Ship.addItem(FlotsamItem,FlotsamQty)
                underAttack = False
            else :
                print(f"{cr.Fore.WHITE}There are still ", piratesLeft, "ships attacking!")
        else :
            outRun = random.randrange(1, 4, 1)
            if (outRun >= piratesLeft):
                underAttack = False
                print(f"{cr.Fore.WHITE}We have escaped!")
            else :
                print("We have outrun", outRun, "ships!")
                piratesLeft = (piratesLeft - outRun)
        
        continueGame = input("Press <ENTER> to continue")
    

def Travel_toPort():

    Port_Desired = ""
    print(Game_Port.getPortNameList())
    
    while (Port_Desired != "H") and (Port_Desired != "B") and (Port_Desired != "C") and (Port_Desired != "J") and (Port_Desired != "M") and (Port_Desired != "P") and (Port_Desired != "R") and (Port_Desired != "S"):
        Port_Desired = input("Where would you like to go? ["+Game_Port.getPortCharList()+"]")
        if (len(Port_Desired) > 0) :
            Port_Desired = Port_Desired[0].upper()

    match Port_Desired:
        case "H":
            newGamePort = 0
        case "B":
            newGamePort = 1
        case "C":
            newGamePort = 2
        case "J":
            newGamePort = 3
        case "M":
            newGamePort = 4
        case "P":
            newGamePort = 5
        case "R":
            newGamePort = 6
        case "S":
            newGamePort = 7
            
    if (newGamePort == Game_Port.getPort()):
        print("We're already there!")
        User_Action = input("Press <ENTER> to continue")
    else :
        Game_Items.SetPrices()
        Game_Port.setPort(newGamePort)
        Attack = random.randrange(1, 10, 1)
        if (Attack > 6):
            Ship_UnderAttack()

def Buy_Cargo(bIndex):

    print(f"Buy {Game_Items.GetItemName(bIndex)}!")
    Can_Buy = (Player_Money.GetCashOnHand() // Game_Items.GetItemPrice(bIndex))
    print(f"You can afford {Can_Buy} {Game_Items.GetItemName(bIndex)}.")
    Want_Buy = int(input("How much do you want to buy?"))
    if (Want_Buy > Can_Buy):
        print("Unable to complete the transaction.  Insufficient Funds!")
        User_Action = input("Press <ENTER> to continue")
    else :
        if (Player_Ship.addItem(bIndex, Want_Buy) == False):
            print("Unable to complete the transaction.  Check capacity!")
            User_Action = input("Press <ENTER> to continue")
        else :
            Player_Money.SpendMoney(Want_Buy * Game_Items.GetItemPrice(bIndex))
    

def Sell_Cargo(sIndex):

    print(f"Sell {Game_Items.GetItemName(sIndex)}!")
    print(f"You have {Player_Ship.getItemQty(sIndex)} of {Game_Items.GetItemName(sIndex)} to sell.")
    Want_Sell = int(input("How much do you want to sell?"))

    if (Player_Ship.removeItem(sIndex, Want_Sell) == False):
        print("Unable to complete the transaction.  Check capacity!")
        User_Action = input("Press <ENTER> to continue")
    else:
        Player_Money.AddMoney(Want_Sell * Game_Items.GetItemPrice(sIndex))


def Buy_SelectItem():

    Cargo_ToBuy = ""
    
    while (Cargo_ToBuy != "S") and (Cargo_ToBuy != "T") and (Cargo_ToBuy != "G") and (Cargo_ToBuy != "O") and (Cargo_ToBuy != "Q"):
        print(f"Would you like to buy {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
        Cargo_ToBuy = input("[S,T,G,O,Q]")
        if (len(Cargo_ToBuy) > 0) :
            Cargo_ToBuy = Cargo_ToBuy[0].upper()

    match Cargo_ToBuy:
        case "S":
            Buy_Cargo(0)
        case "T":
            Buy_Cargo(1)
        case "G":
            Buy_Cargo(2)
        case "O":
            Buy_Cargo(3)

def Sell_SelectItem():

    Cargo_ToSell = ""

    while (Cargo_ToSell != "S") and (Cargo_ToSell != "T") and (Cargo_ToSell != "G") and (Cargo_ToSell != "O") and (Cargo_ToSell != "Q"):
        print(f"Would you like to sell {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
        Cargo_ToSell = input("[S,T,G,O,Q]")
        if (len(Cargo_ToSell) > 0) :
            Cargo_ToSell = Cargo_ToSell[0].upper()

    match Cargo_ToSell:
        case "S":
            Sell_Cargo(0)
        case "T":
            Sell_Cargo(1)
        case "G":
            Sell_Cargo(2)
        case "O":
            Sell_Cargo(3)


def Visit_Bank():
    Bank_Amount = 0
    Bank_Action = ""

    while (Bank_Action != "D") and (Bank_Action != "W") and (Bank_Action != "B") and (Bank_Action != "R") :
        print(f"Would you like to {cr.Fore.GREEN}D{cr.Fore.WHITE}eposit, {cr.Fore.GREEN}W{cr.Fore.WHITE}ithdraw, {cr.Fore.GREEN}B{cr.Fore.WHITE}orrow or {cr.Fore.GREEN}R{cr.Fore.WHITE}epay?")
        Bank_Action = input("[D,W,B,R]")
        if (len(Bank_Action) > 0) :
            Bank_Action = Bank_Action[0].upper()

    match Bank_Action:
        case "D":
            Bank_Amount = int(input("How much would you like to deposit?"))
            if (Player_Money.DepositMoney(Bank_Amount) == False):
                print("Unable to complete the transaction.  Check cash on hand!")
                Bank_Action = input("Press <ENTER> to continue")

        case "W":
            Bank_Amount = int(input("How much would you like to withdraw?"))
            if (Player_Money.WithdrawMoney(Bank_Amount) == False):
                print("Unable to complete the transaction.  Check cash in bank!")
                Bank_Action = input("Press <ENTER> to continue")

        case "B":
            Bank_Amount = int(input("How much would you like to borrow?"))
            if (Player_Money.BorrowMoney(Bank_Amount) == False):
                print("Unable to complete the transaction.  1000 Max!")
                Bank_Action = input("Press <ENTER> to continue")

        case "R":
            Bank_Amount = int(input("How much would you like to repay?"))
            if (Player_Money.RepayMoney(Bank_Amount) == False):
                print("Unable to complete the transaction.  Check cash on hand!")
                Bank_Action = input("Press <ENTER> to continue")


def Store_Cargo(sIndex):

    onShip = int(Player_Ship.getItemQty(sIndex))
    WarehouseSpace = Player_WHouse.GetCurrentCapacity()
    
    if (onShip > WarehouseSpace):
        Can_Store = WarehouseSpace
    else:
        Can_Store = onShip

    qty2Store = Can_Store + 1
    while (qty2Store > Can_Store):
        print("You can store", Can_Store, Game_Items.GetItemName(sIndex),".")
        qty2Store = int(input("How much do you want to store?"))

    print(f"Store {Game_Items.GetItemName(sIndex)}!")

    if (Player_WHouse.StoreItem(sIndex,qty2Store) == False):
        print("Unable to complete the transaction.  Check Warehouse capacity!")
        User_Action = input("Press <ENTER> to continue")
    else:
        if (Player_Ship.removeItem(sIndex,qty2Store) == False):
            print("Unable to complete the transaction.  Check Ship cargo availability!")
            User_Action = input("Press <ENTER> to continue")

    print("Stored", qty2Store,Game_Items.GetItemName(sIndex))
    continueGame = input("Press <ENTER> to continue")


def Store_SelectItem():
    Cargo_ToStore = ""

    while (Cargo_ToStore != "S") and (Cargo_ToStore != "T") and (Cargo_ToStore != "G") and (Cargo_ToStore != "O") and (Cargo_ToStore != "Q"):
        print(f"{cr.Fore.WHITE}Would you like to store {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
        Cargo_ToStore = input("[S,T,G,O,Q]")
        if (len(Cargo_ToStore) > 0) :
            Cargo_ToStore = Cargo_ToStore[0].upper()

    match Cargo_ToStore:
        case "S":
            Store_Cargo(0)
        case "T":
            Store_Cargo(1)
        case "G":
            Store_Cargo(2)
        case "O":
            Store_Cargo(3)


def Retrieve_Cargo(index):

    inWhouse = Player_WHouse.GetItemQty(index)
    ShipSpace = Player_Ship.getShipCurrentCapacity()
    
    if (inWhouse > ShipSpace):
        Can_Retrieve = ShipSpace
    else: 
        Can_Retrieve = inWhouse

    qty2Retrieve = Can_Retrieve + 1
    while (qty2Retrieve > Can_Retrieve):
        print("You can retrieve", Can_Retrieve, Game_Items.GetItemName(index),".")
        qty2Retrieve = int(input("How much do you want to retrieve?"))

    print(f"Retrieve {Game_Items.GetItemName(index)}!")

    if (Player_WHouse.RetrieveItem(index,qty2Retrieve) == False):
        print("Unable to complete the transaction.  Check Warehouse capacity!")
        User_Action = input("Press <ENTER> to continue")
    else:
        if (Player_Ship.addItem(index,qty2Retrieve) == False):
            print("Unable to complete the transaction.  Check Ship cargo availability!")
            User_Action = input("Press <ENTER> to continue")

    print("Retrieved", qty2Retrieve,Game_Items.GetItemName(index))
    continueGame = input("Press <ENTER> to continue")
    


def Retrieve_SelectItem():
    Cargo_ToRetrieve = ""

    while (Cargo_ToRetrieve != "S") and (Cargo_ToRetrieve != "T") and (Cargo_ToRetrieve != "G") and (Cargo_ToRetrieve != "O"):
        print(f"{cr.Fore.WHITE}Would you like to retrieve {cr.Fore.GREEN}S{cr.Fore.WHITE}ilk ,{cr.Fore.GREEN}T{cr.Fore.WHITE}ea, {cr.Fore.GREEN}G{cr.Fore.WHITE}unpowder ,or {cr.Fore.GREEN}O{cr.Fore.WHITE}pium?")
        Cargo_ToRetrieve = input("[S,T,G,O]")
        if (len(Cargo_ToRetrieve) > 0) :
            Cargo_ToRetrieve = Cargo_ToRetrieve[0].upper()

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
    Whse_Action = ""

    while (Whse_Action != "S") and (Whse_Action != "R"):
        print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}S{cr.Fore.WHITE}tore or {cr.Fore.GREEN}R{cr.Fore.WHITE}etrieve items from the warehouse?")
        Whse_Action = input("[S,R]")
        if (len(Whse_Action) > 0) :
            Whse_Action = Whse_Action[0].upper()

    match Whse_Action:
        case "S":
            Store_SelectItem()
        case "R":
            Retrieve_SelectItem()


def Repair_Ship():
    damAmount = Player_Ship.getDamage()
    repCost = (damAmount * 10)

    print("Repairing a ship costs 10 gold per damage point.")
    print("Your ship has "+str(damAmount)+" damage points.")
    print("It will cost "+str(repCost)+" to fully repair your ship.")
    Want_Repair = int(input("How much DAMAGE do you want to repair?"))

    if ((Want_Repair * 10) > Player_Money.GetCashOnHand()):
        print("Unable to complete the transaction.  Insufficient Funds!")
        User_Action = input("Press <ENTER> to continue")
    else :
        if (Want_Repair > Player_Ship.getDamage()):
            print("Unable to complete the transaction.  Check damage!")
            User_Action = input("Press <ENTER> to continue")
        else :
            Player_Money.SpendMoney(Want_Repair * 10)
            Player_Ship.repairShip(Want_Repair)
   


def Play():

    Clear_Screen()
    print(f"{cr.Fore.GREEN}Welcome to " + str(Game_Port.getPortName()) + ", " + Company_Name + "!\n")

    print_GameStatus() 
#    print("Ship Name     :", Player_Ship.getShipName())
#    print("Ship Capacity :", Player_Ship.getShipCurrentCapacity(), "/", Player_Ship.getShipMaxCapacity())
#    print("Ship Defense  :", Player_Ship.getShipDefense(), "/", Player_Ship.getShipMaxDefense())
#    print("Warehouse Cap.:", str(Player_WHouse.GetCurrentCapacity()), "/", str(Player_WHouse.GetMaxCapacity()),"\n")
#    Player_Money.print_MoneyStatus()

    print("GOODS        PRICE     QTY IN SHIP     QTY IN WAREHOUSE")
    print("=====        =====     ===========     ================")

    for i in range(4):
        print((Game_Items.GetItemName(i)).ljust(9," "), ": ", str(Game_Items.GetItemPrice(i)).ljust(9," "), str(Player_Ship.getItemQty(i)).ljust(15," "), str(Player_WHouse.GetItemQty(i)))

    print("\n")
    User_Action = ""
    if (Game_Port.getPort() == 0):  # Hong Kong has more services
    
        while (User_Action != "B") and (User_Action != "S") and (User_Action != "V") and (User_Action != "W") and (User_Action != "R") and (User_Action != "T"):
            print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, {cr.Fore.GREEN}V{cr.Fore.WHITE}isit the Bank, use the {cr.Fore.GREEN}W{cr.Fore.WHITE}arehouse, {cr.Fore.GREEN}R{cr.Fore.WHITE}epair your ship, or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
            User_Action = input("[B,S,V,W,R,T]")
            if (len(User_Action) > 0) :
                User_Action = User_Action[0].upper()
    
        match User_Action:
            case "B":
                Buy_SelectItem()
            case "S":
                Sell_SelectItem()
            case "V":
                Visit_Bank()
            case "W":
                Use_Warehouse()
            case "R":
                Repair_Ship()
            case "T":
                Travel_toPort()
            case _:
                User_Action = input("Press <ENTER> to continue")
    
    else:
        while (User_Action != "B") and (User_Action != "S") and (User_Action != "T"):
            print(f"Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
            User_Action = input("[B,S,T]")
            if (len(User_Action) > 0) :
                User_Action = User_Action[0].upper()
  
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

