import os
import math
import random
# import colorama but as cr, as cr is easier to use.
import colorama as cr
cr.init(autoreset=True)

class tradeItemList:
# lists = index 0 - 3
    itemName = ["Opium", "Silk", "Arms", "General"]
    itemPrice = [0, 0, 0, 0]

    def __init__(self):
        self.SetPrices()

    def SetPrices(self):
        self.itemPrice = [random.randrange(300, 999, 5), random.randrange(50, 250, 1), random.randrange(5, 150, 5), random.randrange(1, 99, 1)]

    def GetItemPrice(self,index):
        return(self.itemPrice[index])

    def GetItemName(self,index):
        return(self.itemName[index])

class tradePort:
    portNames = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
    portIndex = 0

    def __init__(self):
        self.portIndex = 0
        
    def SetPort(self, newIndex):
        if (self.portIndex != newIndex):
            self.portIndex = newIndex
    
    def GetPort(self):
        return(self.portIndex)

    def GetPortName(self):
        return(self.portNames[self.portIndex])
        
    def GetPortNameList(self):
        pNames = ""
        portList = []
        for i in range(len(self.portNames)):
            if (i != self.portIndex):
                portList.append(self.portNames[i])
        pNames = ",".join(portList)
        return(pNames)

    def GetPortCharList(self):
        pChars = ""
        portList = []
        for i in range(len(self.portNames)):
            if (i != self.portIndex):
                portList.append(self.portNames[i][0])
        pChars = ",".join(portList)
        return(pChars)


class Gold:
    onHand = 0
    inBank = 0
    inDebt = 0

    def __init__(self, onHand):
        self.onHand = onHand
    
    def SpendGold(self,gold2spend):
        retVal = False
        if (gold2spend > self.onHand):
            print("Too much!")
        else : 
            self.onHand = (self.onHand - gold2spend)
            retVal = True
        return(retVal)

    def AddGold(self,gold2add):
        self.onHand = (self.onHand + gold2add)

    def GetGoldOnHand(self):
        return (self.onHand)

    def GetGoldInBank(self):
        return (self.inBank)

    def GetGoldInDebt(self):
        return (self.inDebt)

    def DepositGold(self,gold2dep):
        retVal = False
        if (int(gold2dep) > int(self.onHand)):
            print("Too much!")
        else : 
            self.onHand = (self.onHand - gold2dep)
            self.inBank = (self.inBank + gold2dep)
            retVal = True
        return(retVal)

    def WithdrawGold(self,gold2wd):
        retVal = False
        if (int(gold2wd) > int(self.inBank)):
            print("Too much!")
        else : 
            self.onHand = (self.onHand + gold2wd)
            self.inBank = (self.inBank - gold2wd)
            retVal = True
        return(retVal)

    def BorrowGold(self,gold2borrow):
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

    def RepayGold(self,gold2repay):
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
#    whseItemName = ["Opium", "Silk", "Arms", "General"]
    whseItemQty = [0, 0, 0, 0]
    whseMaxCapacity = 10000

    def __init__(self, name):
        self.name = name

    def GetCurrentCapacity(self):
        return (self.whseMaxCapacity - self.whseItemQty[0] - self.whseItemQty[1] - self.whseItemQty[2] - self.whseItemQty[3])

    def GetMaxCapacity(self):
        return(self.whseMaxCapacity)

#    def GetUsedCapacity(self):
#        return (self.whseItemQty[0] + self.whseItemQty[1] + self.whseItemQty[2] + self.whseItemQty[3])

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
#    itemName = ["Opium", "Silk", "Arms", "General"]
    itemQty = [0, 0, 0, 0]
    shipMaxDefense = 500
    shipDefense = 500
    shipGuns = 5
    shipMaximumCapacity = 50
    shipAvailableCapacity = 50
    
    def __init__(self, name):
        self.name = name
    
    def GetShipName(self):
        return (self.name)
        
    def GetShipDefense(self):
        return (self.shipDefense)

    def GetShipGuns(self):
        return (self.shipGuns)

    def GetDamage(self):
        return (self.shipMaxDefense-self.shipDefense)

    def GetStatus(self):
        return (round((self.shipDefense/self.shipMaxDefense) * 100))

    def GetItemQty(self, index):
        return (self.itemQty[index])
        
    def GetTotalWeight(self):
        return(self.itemQty[0] + self.itemQty[1] + self.itemQty[2] + self.itemQty[3])

    def GetShipCapacity(self):
        return(round(self.shipMaximumCapacity * (self.shipDefense / self.shipMaxDefense)))

    def GetShipMaxCapacity(self):
        return(self.shipMaximumCapacity)
        
    def GetShipCurrentCapacity(self):
        return(self.GetShipCapacity() - self.itemQty[0] - self.itemQty[1] - self.itemQty[2] - self.itemQty[3])
    
    def SetCapacity(self,newCap):
        self.shipMaximumCapacity = newCap
    
    def AddItem(self, index, amount2add):
        retVal = False
        if (amount2add > self.GetShipCurrentCapacity()) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] + amount2add)
            retVal = True
        return retVal
    
    def RemoveItem(self, index, amount2rem):
        retVal = False
        if (amount2rem > self.itemQty[index]) :
            print("Too much!")
        else :
            self.itemQty[index] = (self.itemQty[index] - amount2rem)
            retVal = True
        return retVal

    def DamageShip(self,Damage):
        self.shipDefense = (self.shipDefense - Damage)
        if (self.GetTotalWeight() > self.GetShipCapacity()):
            while (self.GetTotalWeight() > self.GetShipCapacity()) and (self.GetItemQty(3) > 0):
                self.RemoveItem(3,1);
        if (self.GetTotalWeight() > self.GetShipCapacity()):
            while (self.GetTotalWeight() > self.GetShipCapacity()) and (self.GetItemQty(2) > 0):
                self.RemoveItem(2,1);
        if (self.GetTotalWeight() > self.GetShipCapacity()):
            while (self.GetTotalWeight() > self.GetShipCapacity()) and (self.GetItemQty(1) > 0):
                self.RemoveItem(1,1);
        if (self.GetTotalWeight() > self.GetShipCapacity()):
            while (self.GetTotalWeight() > self.GetShipCapacity()) and (self.GetItemQty(0) > 0):
                self.RemoveItem(0,1);
        

    def RepairShip(self,Repair):
        self.shipDefense = (self.shipDefense + Repair)
        if (self.shipDefense > self.shipMaxDefense):
            self.shipDefense = self.shipMaxDefense

    def Attack(self):
        return(int(self.shipGuns * random.randrange(5, 50, 5)))
        
    
global Company_Name
global Game_Items
global Game_Port
global Player_Ship
global Player_Gold
global Player_WHouse


def Clear_Screen():
    os.system('cls')

    
def Config_Game():
    global Company_Name
    global Game_Items
    global Game_Port
    global Player_Ship
    global Player_Gold
    global Player_WHouse

    Clear_Screen()
    print("Welcome to the East Empire Trading Simulation!\n")
    Company_Name = input("What shall we use for a company name?\n")
    
    Game_Items = tradeItemList()
    
    Game_Port = tradePort()
    Player_Ship = Ship(Company_Name)
    Player_Gold = Gold(1000)
    Player_WHouse = Warehouse("My Warehouse")


def Print_PirateShips(pirateQty):

    if (pirateQty < 1):
        return()

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

#  end Print_PirateShips


def Select_TradeItem():

    Selection = ""

    while (Selection != "O") and (Selection != "S") and (Selection != "A") and (Selection != "G") and (Selection != "Q"):
        print(f"Sellect item: {cr.Fore.GREEN}O{cr.Fore.WHITE}pium ,{cr.Fore.GREEN}S{cr.Fore.WHITE}ilk, {cr.Fore.GREEN}A{cr.Fore.WHITE}rms ,or {cr.Fore.GREEN}G{cr.Fore.WHITE}eneral cargo?")
        Selection = input("[O,S,A,G,Q]")
        if (len(Selection) > 0) :
            Selection = Selection[0].upper()

    return(Selection)
        



#
# ┌──────────────────────────────────────────────────────────────────────┐
# │                 Company Name : The Peace Dividend                    │
# │  Hong Kong                                             99 jan 1860   │
# │ ┌────────────────────────────────────┐ ┌───────────────────────────┐ │
# │ │ Goods    Price   Ship   Warehouse  │ │ Gold On Hand : 1,000,000  │ │
# │ │ ================================== │ │ Gold in Bank : 0          │ │
# │ │ Opium    9999    99     10,000     │ │ Gold in Debt : 0          │ │
# │ │ Silk     999     0      0          │ ├───────────────────────────┤ │
# │ │ Arms     99      0      0          │ │ Ship Capacity : 50 / 50   │ │
# │ │ General  99      0      0          │ │ Ship Guns     : 5         │ │
# │ │                  ================= │ │ Ship Defense  : 500       │ │
# │ │       Available  99     99,999     │ │ Ship Status   : 100%      │ │
# │ └────────────────────────────────────┘ └───────────────────────────┘ │
# │                                                                      │
# └──────────────────────────────────────────────────────────────────────┘
                   

def print_GameStatus() :
    print(f"{cr.Fore.GREEN} ┌──────────────────────────────────────────────────────────────────────┐")
    print(f"{cr.Fore.GREEN} │" + ("Firm: " + Player_Ship.GetShipName()).center(70) + "│")
    print(f"{cr.Fore.GREEN} │  {cr.Fore.WHITE}" + Game_Port.GetPortName().ljust(49),end="")
    print(f"{cr.Fore.GREEN}Date: {cr.Fore.WHITE}" +"99 JAN 1860",end="")
    print(f"{cr.Fore.GREEN}  │")
    print(f"{cr.Fore.GREEN} │ ┌────────────────────────────────────┐ ┌───────────────────────────┐ │")
    print(f"{cr.Fore.GREEN} │ │ Goods    Price   Ship   Warehouse  │ │ Gold On Hand : " + str("{:,}".format(Player_Gold.GetGoldOnHand())).ljust(11) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ ================================== │ │ Gold in Bank : " + str("{:,}".format(Player_Gold.GetGoldInBank())).ljust(11) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Game_Items.GetItemName(0)).ljust(9) + str(Game_Items.GetItemPrice(0)).ljust(8) + str(Player_Ship.GetItemQty(0)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(0))).ljust(11) + "│ │ Gold in Debt : " + str("{:,}".format(round(Player_Gold.GetGoldInDebt()))).ljust(11) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Game_Items.GetItemName(1)).ljust(9) + str(Game_Items.GetItemPrice(1)).ljust(8) + str(Player_Ship.GetItemQty(1)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(1))).ljust(11) + "│ ├───────────────────────────┤ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Game_Items.GetItemName(2)).ljust(9) + str(Game_Items.GetItemPrice(2)).ljust(8) + str(Player_Ship.GetItemQty(2)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(2))).ljust(11) + "│ │ Ship Capacity : " + (str(Player_Ship.GetShipCapacity()) + " / " + str(Player_Ship.GetShipMaxCapacity())).ljust(10) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Game_Items.GetItemName(3)).ljust(9) + str(Game_Items.GetItemPrice(3)).ljust(8) + str(Player_Ship.GetItemQty(3)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(3))).ljust(11) + "│ │ Ship Guns     : " + str(Player_Ship.GetShipGuns()).ljust(10) + "│ │")
    print(f"{cr.Fore.GREEN} │ │                  ================= │ │ Ship Defense  : "  + str(Player_Ship.GetShipDefense()).ljust(10) + "│ │")
    print(f"{cr.Fore.GREEN} │ │       Available  " + str(Player_Ship.GetShipCurrentCapacity()).ljust(7) + str("{:,}".format(Player_WHouse.GetCurrentCapacity())).ljust(11) + "│ │ Ship Status   : " + str(Player_Ship.GetStatus()).ljust(3) + "%      │ │")
    print(f"{cr.Fore.GREEN} │ └────────────────────────────────────┘ └───────────────────────────┘ │")
    print(f"{cr.Fore.GREEN} └──────────────────────────────────────────────────────────────────────┘")
    

def Ship_UnderAttack():

    underAttack = True
    piratesInitial = random.randrange(1, 15, 1)   # Set intitial number of attacking ships 
    piratesDefense = (piratesInitial * 100)       # Each ship takes 100 points of damage to sink it.
    piratesLeft = piratesInitial   # use piratesInitial to calculate the flotsam and jetsam.  more initial ships = greater reward
    while (underAttack):
        Clear_Screen()
        shipDamageTaken = int(random.randrange(1, ((piratesLeft if piratesLeft > 0 else 1)*2), 1))  # damage taken to Player_Ship -  calc on number of pirates left
        Player_Ship.DamageShip(shipDamageTaken)
        print_GameStatus()

        Print_PirateShips(piratesLeft)

        print(f"We are under attack by{cr.Fore.YELLOW} " + str(piratesLeft), end=" ")
        print(f"{cr.Fore.WHITE}ships!")
#        print("Defense: "+str(piratesDefense))
#        print("Start Ships: "+str(piratesInitial))
#        print("Ships Left: "+str(piratesLeft))
        print(f"We have sustained{cr.Fore.YELLOW} " + str(shipDamageTaken), end=" ")
        print(f"{cr.Fore.WHITE}damage to our defenses.")

        RunFight = ""
        while (RunFight != "F") and (RunFight != "R"):
            print(f"We're under attack.  Shall we {cr.Fore.GREEN}F{cr.Fore.WHITE}ight or {cr.Fore.GREEN}R{cr.Fore.WHITE}un?")
            RunFight = input("[F,R]")
            if (len(RunFight)> 0) :
                RunFight = RunFight[0].upper()

        if (RunFight == "F"):
            attackValue = Player_Ship.Attack()               # Ship Attack is based on Guns in ship
            piratesDefense = (piratesDefense - attackValue)
            piratesLeft = (piratesDefense // 100)
            if (piratesLeft < 1):
                print(f"{cr.Fore.WHITE}Victory!  We have sunk all of the attacking ships!")
                FlotsamQty = int(random.randrange(1, int(piratesInitial), 1))
                FlotsamItem = int(random.randrange(1, 4, 1))
                print("We have recovered some flotsam and jetsam.",FlotsamQty, "of",Player_Ship.GetItemName(FlotsamItem))
                if (FlotsamQty > Player_Ship.GetShipCurrentCapacity()):
                    FlotsamQty = Player_Ship.GetShipCurrentCapacity()
                Player_Ship.AddItem(FlotsamItem,FlotsamQty)
                underAttack = False
            else :
                print(f"{cr.Fore.WHITE}We hit them with  ", attackValue, "damage.")
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
    print(Game_Port.GetPortNameList())
    
    while (Port_Desired != "H") and (Port_Desired != "B") and (Port_Desired != "C") and (Port_Desired != "J") and (Port_Desired != "M") and (Port_Desired != "P") and (Port_Desired != "R") and (Port_Desired != "S") and (Port_Desired != "Q") :
        Port_Desired = input("Where would you like to go? ["+Game_Port.GetPortCharList()+",Q]")
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
        case "Q":
            newGamePort = Game_Port.GetPort()
            
    if (newGamePort == Game_Port.GetPort()):
        print("We're already there!")
        Port_Desired = input("Press <ENTER> to continue")
    else :
        Game_Items.SetPrices()
        Game_Port.SetPort(newGamePort)
        Attack = random.randrange(1, 10, 1)
        if (Attack > 6):
            Ship_UnderAttack()

def Buy_Cargo(bIndex):
    print(f"Buy {Game_Items.GetItemName(bIndex)}!")
    print(f"You can afford {Can_Buy} {Game_Items.GetItemName(bIndex)}.")
    bIndex = Select_TradeItem()
    Can_Buy = (Player_Gold.GetGoldOnHand() // Game_Items.GetItemPrice(bIndex))
    Want_Buy = int(input("How much do you want to buy?"))
    if (Want_Buy > Can_Buy):
        print("Unable to complete the transaction.  Insufficient Funds!")
        Want_Buy = input("Press <ENTER> to continue")
    else :
        if (Player_Ship.AddItem(bIndex, Want_Buy) == False):
            print("Unable to complete the transaction.  Check capacity!")
            Want_Buy = input("Press <ENTER> to continue")
        else :
            Player_Gold.SpendGold(Want_Buy * Game_Items.GetItemPrice(bIndex))
   

def Sell_Cargo():
    print(f"Sell {Game_Items.GetItemName(sIndex)}!")
    print(f"You have {Player_Ship.GetItemQty(sIndex)} of {Game_Items.GetItemName(sIndex)} to sell.")
    sIndex = Select_TradeItem()
    Want_Sell = int(input("How much do you want to sell?"))

    if (Player_Ship.RemoveItem(sIndex, Want_Sell) == False):
        print("Unable to complete the transaction.  Check capacity!")
        Want_Sell = input("Press <ENTER> to continue")
    else:
        Player_Gold.AddGold(Want_Sell * Game_Items.GetItemPrice(sIndex))


def Visit_Bank():
    Bank_Amount = 0
    Bank_Action = ""

    while (Bank_Action != "D") and (Bank_Action != "W") and (Bank_Action != "B") and (Bank_Action != "R") and (Bank_Action != "Q") :
        print(f"Would you like to {cr.Fore.GREEN}D{cr.Fore.WHITE}eposit, {cr.Fore.GREEN}W{cr.Fore.WHITE}ithdraw, {cr.Fore.GREEN}B{cr.Fore.WHITE}orrow or {cr.Fore.GREEN}R{cr.Fore.WHITE}epay?")
        Bank_Action = input("[D,W,B,R,Q]")
        if (len(Bank_Action) > 0) :
            Bank_Action = Bank_Action[0].upper()

    match Bank_Action:
        case "D":
            Bank_Amount = int(input("How much would you like to deposit?"))
            if (Player_Gold.DepositGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insuffcient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "W":
            Bank_Amount = int(input("How much would you like to withdraw?"))
            if (Player_Gold.WithdrawGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insuffcient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "B":
            Bank_Amount = int(input("How much would you like to borrow?"))
            if (Player_Gold.BorrowGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  1000 Max!")
                Bank_Action = input("Press <ENTER> to continue")

        case "R":
            Bank_Amount = int(input("How much would you like to repay?"))
            if (Player_Gold.RepayGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insuffcient Funds!")
                Bank_Action = input("Press <ENTER> to continue")


def Store_Cargo(sIndex):
    sIndex = Select_TradeItem()
    onShip = int(Player_Ship.GetItemQty(sIndex))
    WarehouseSpace = Player_WHouse.GetCurrentCapacity()
    
    if (onShip > WarehouseSpace):
        Can_Store = WarehouseSpace
    else:
        Can_Store = onShip

    print(f"Store {Game_Items.GetItemName(sIndex)}!")
    print("You can store", Can_Store, Game_Items.GetItemName(sIndex),".")

    qty2Store = int(input("How much do you want to store?"))
    while (qty2Store < 0) and (qty2Store > Can_Store):
        qty2Store = int(input("How much do you want to store?"))

    if (Player_Ship.RemoveItem(sIndex,qty2Store) == False):
        print("Unable to complete the transaction.  Check Ship cargo availability!")
    else:
        if (Player_WHouse.StoreItem(sIndex,qty2Store) == False):
            print("Unable to complete the transaction.  Check Warehouse capacity!")
        else:
            print("Stored", qty2Store,Game_Items.GetItemName(sIndex))

    continueGame = input("Press <ENTER> to continue")


def Retrieve_Cargo():
    rIndex = Select_TradeItem()
    inWhouse = Player_WHouse.GetItemQty(rIndex)
    ShipSpace = Player_Ship.GetShipCurrentCapacity()
    
    if (inWhouse > ShipSpace):
        Can_Retrieve = ShipSpace
    else: 
        Can_Retrieve = inWhouse

    print(f"Retrieve {Game_Items.GetItemName(rIndex)}!")
    print("You can retrieve", Can_Retrieve, Game_Items.GetItemName(rIndex),".")

    qty2Retrieve = int(input("How much do you want to retrieve?"))
    while (qty2Retrieve < 0) and (qty2Retrieve > Can_Retrieve):
        print("You can retrieve", Can_Retrieve, Game_Items.GetItemName(rIndex),".")
        qty2Retrieve = int(input("How much do you want to retrieve?"))

    print(f"Retrieve {Game_Items.GetItemName(rIndex)}!")

    if (Player_WHouse.RetrieveItem(rIndex,qty2Retrieve) == False):
        print("Unable to complete the transaction.  Check Warehouse capacity!")
    else:
        if (Player_Ship.AddItem(rIndex,qty2Retrieve) == False):
            print("Unable to complete the transaction.  Check Ship cargo availability!")
            print("Returning cargo")
            Player_WHouse.StoreItem(rIndex,qty2Retrieve)
        else:
            print("Retrieved", qty2Retrieve,Game_Items.GetItemName(rIndex))

    continueGame = input("Press <ENTER> to continue")


def Use_Warehouse():
    xfer_Amount = 0
    xfer_Item = 0
    Whse_Action = ""

    while (Whse_Action != "S") and (Whse_Action != "R") and (Whse_Action != "Q"):
        print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}S{cr.Fore.WHITE}tore or {cr.Fore.GREEN}R{cr.Fore.WHITE}etrieve items from the warehouse?")
        Whse_Action = input("[S,R,Q]")
        if (len(Whse_Action) > 0) :
            Whse_Action = Whse_Action[0].upper()

    match Whse_Action:
        case "S":
            Store_Cargo()
        case "R":
            Retrieve_Cargo()


def Repair_Ship():
    damAmount = Player_Ship.GetDamage()
    repCost = (damAmount * 10)

    print("Repairing a ship costs 10 gold per damage point.")
    print("Your ship has "+str(damAmount)+" damage points.")
    print("It will cost "+str(repCost)+" to fully repair your ship.")
    Want_Repair = int(input("How much DAMAGE do you want to repair?"))

    if ((Want_Repair * 10) > Player_Gold.GetGoldOnHand()):
        print("Unable to complete the transaction.  Insufficient Funds!")
        Want_Repair = input("Press <ENTER> to continue")
    else :
        if (Want_Repair > Player_Ship.GetDamage()):
            print("Unable to complete the transaction.  Check damage!")
            Want_Repair = input("Press <ENTER> to continue")
        else :
            Player_Gold.SpendGold(Want_Repair * 10)
            Player_Ship.RepairShip(Want_Repair)
   

def Play():

    Clear_Screen()
    print(f"{cr.Fore.GREEN}Welcome to " + str(Game_Port.GetPortName()) + ", " + Company_Name + "!\n")

    print_GameStatus() 

    print("\n")
    User_Action = ""
    if (Game_Port.GetPort() == 0):  # Hong Kong has more services
    
        while (User_Action != "B") and (User_Action != "S") and (User_Action != "V") and (User_Action != "W") and (User_Action != "R") and (User_Action != "T"):
            print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, {cr.Fore.GREEN}V{cr.Fore.WHITE}isit the Bank, use the {cr.Fore.GREEN}W{cr.Fore.WHITE}arehouse, {cr.Fore.GREEN}R{cr.Fore.WHITE}epair your ship, or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
            User_Action = input("[B,S,V,W,R,T]")
            if (len(User_Action) > 0) :
                User_Action = User_Action[0].upper()
    
        match User_Action:
            case "B":
                Buy_Cargo()
            case "S":
                Sell_Cargo()
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
  
    Config_Game()
    
    while (Player_Gold.GetGoldOnHand() < 10000000):
        Play()


if __name__ == "__main__":
    main()

