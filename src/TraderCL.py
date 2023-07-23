import os
import math
import random
# import colorama but as cr, as cr is easier to use.
import colorama as cr
cr.init(autoreset=True)

class gameDate:
    monthName = ["Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec"]

    def __init__(self):
        self.DOM = 1
        self.MOY = 1
        self.YEAR = 1850

    def GetDate(self):
        return(str(self.DOM).rjust(2,"0") + " " + self.monthName[(self.MOY - 1)] + " " + str(self.YEAR))

    def GetMonth(self):
        return(self.MOY)

    def IncrementDate(self, Days2Add):
        self.DOM = self.DOM + Days2Add

        if (self.MOY == 1) or (self.MOY == 3) or (self.MOY == 5) or (self.MOY == 7) or (self.MOY == 8) or (self.MOY == 10) or (self.MOY == 12):
            if (self.DOM > 31):
                self.DOM -= 31
                self.MOY += 1
        if (self.MOY == 4) or (self.MOY == 6) or (self.MOY == 9) or (self.MOY == 11):
            if (self.DOM > 30):
                self.DOM -= 30
                self.MOY += 1
        if (self.MOY == 2):
            if (self.DOM > 28):
                self.DOM -= 28
                self.MOY += 1
        if (self.MOY > 12) :
            self.YEAR += 1
            self.MOY = 1
    
# -------[ END class gameDate ]---------

class TradeItems:
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

# -------[ END class TradeItems ]---------

class TradePort:
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

    def GetAvailableHarbors(self):
        hNames = ""
        for i in range(len(self.portNames)) :
            if (i != self.portIndex):
                hNames = hNames + "{cr.Fore.GREEN}" + (self.portNames[i])[:1] + "{cr.Fore.WHITE}" (self.portNames[i])[:-1] + " "
        return(hNames)

    def GetPortCharList(self):
        pChars = ""
        portList = []
        for i in range(len(self.portNames)):
            if (i != self.portIndex):
                portList.append(self.portNames[i][0])
        pChars = ",".join(portList)
        return(pChars)

# -------[ END class TradePort ]---------

class playerGold:
    onHand = 0
    inBank = 0
    inDebt = 0

    def __init__(self, onHand):
        self.onHand = onHand

    def SetGoldOnHand(self, newAmount):
        self.onHand = newAmount
        return (self.onHand)

    def GetGoldOnHand(self):
        return (self.onHand)

    def GetGoldInBank(self):
        return (self.inBank)

    def GetGoldInDebt(self):
        return (self.inDebt)

    def SpendGold(self,gold2spend):
        retVal = 9
        if (gold2spend > self.onHand):
            print("You do not have that much gold.")
            retVal = 1
        else : 
            self.onHand = (self.onHand - gold2spend)
            retVal = 0
        return(retVal)

    def AddGold(self,gold2add):
        self.onHand = (self.onHand + gold2add)

    def DepositGold(self,gold2dep):
        retVal = False
        if (int(gold2dep) > int(self.onHand)):
            print("You do not have that much gold.")
        else : 
            self.onHand = (self.onHand - gold2dep)
            self.inBank = (self.inBank + gold2dep)
            retVal = True
        return(retVal)

    def WithdrawGold(self,gold2wd):
        retVal = False
        if (int(gold2wd) > int(self.inBank)):
            print("You do not have that much gold.")
        else : 
            self.onHand = (self.onHand + gold2wd)
            self.inBank = (self.inBank - gold2wd)
            retVal = True
        return(retVal)

    def BorrowGold(self,gold2borrow):
        retVal = False
        if ((self.inDebt + gold2borrow) > 1000):
            print("You cannot borrow that much! 1000 Max")
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
            print("You do not have that much gold.")
        elif (round(self.inDebt) < gold2repay):
            print("Too much! Overpayment!")
        else : 
            self.inDebt = round(self.inDebt)
            self.onHand = (self.onHand - gold2repay)
            self.inDebt = (self.inDebt - gold2repay)
            retVal = True
        return(retVal)

# -------[ END class playerGold ]---------

class playerWarehouse:
    itemQty = [0, 0, 0, 0]

    def __init__(self):
        self.maxCapacity = 10000

    def GetCurrentCapacity(self):
        return (self.maxCapacity - self.itemQty[0] - self.itemQty[1] - self.itemQty[2] - self.itemQty[3])

    def GetMaxCapacity(self):
        return(self.maxCapacity)

    def GetItemQty(self, index):
        return(self.itemQty[index])

    def StoreItem(self, index, qty):
        retVal = False
        if (qty <= self.GetCurrentCapacity()) :
            self.itemQty[index] = (self.itemQty[index] + qty)
            retVal = True
        return (retVal)

    def RetrieveItem(self, index, qty):
        retVal = False
        if (qty <= self.itemQty[index]) :
            self.itemQty[index] = (self.itemQty[index] - qty)
            retVal = True
        return retVal

# -------[ END class playerWarehouse ]---------

class playerShip:
    itemQty = [0, 0, 0, 0]
    maxDefense = 500
    shipDefense = 500
    shipGuns = 5
    maxCapacity = 50
    
    def __init__(self, name):
        self.name = name
    
    def GetName(self):
        return (self.name)
        
    def GetDefense(self):
        return (self.shipDefense)

    def GetGuns(self):
        return (self.shipGuns)

    def GetDamage(self):
        return (self.maxDefense-self.shipDefense)

    def GetStatus(self):
        return (round((self.shipDefense/self.maxDefense) * 100))

    def GetItemQty(self, index):
        return (self.itemQty[index])
        
    def GetTotalWeight(self):
        return(self.itemQty[0] + self.itemQty[1] + self.itemQty[2] + self.itemQty[3])

    def GetMaxCapacity(self):
        return(self.maxCapacity)
        
    def GetCapacity(self):
        return(round(self.maxCapacity * (self.shipDefense / self.maxDefense)))

    def GetCurrentCapacity(self):
        return(self.GetCapacity() - self.GetTotalWeight())
    
    def SetCapacity(self,newCap):
        self.maxCapacity = newCap
    
    def AddItem(self, index, amount2add):
        retVal = False
        if (amount2add > self.GetCurrentCapacity()) :
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

    def Damage(self,Damage):
        self.shipDefense = (self.shipDefense - Damage)
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(3) > 0):
                self.RemoveItem(3,1);
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(2) > 0):
                self.RemoveItem(2,1);
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(1) > 0):
                self.RemoveItem(1,1);
        if (self.GetTotalWeight() > self.GetCapacity()):
            while (self.GetTotalWeight() > self.GetCapacity()) and (self.GetItemQty(0) > 0):
                self.RemoveItem(0,1);

    def Attack(self):
        return(int(self.shipGuns * random.randrange(5, 60, 5)))

    def Repair(self,Repair):
        self.shipDefense = (self.shipDefense + Repair)
        if (self.shipDefense > self.maxDefense):
            self.shipDefense = self.maxDefense
        
# -------[ END class playerShip ]---------


class pirateFleet:
    pirateDefense = 500
    
    def __init__(self, ships):
        self.ships = ships
        self.pirateDefense = (self.ships * 100)
    
# The number of pirate ships in the attacking fleet.    
    def GetShips(self):
        return (self.ships)

    def SetShips(self,newShips):
        self.ships = newShips
        self.pirateDefense = (self.ships * 100)

    def GetDefense(self):
        return (self.pirateDefense)

# damage delivered to Player_Ship -  calc on number of pirateShips)
    def Attack(self):
        dMin = self.GetShips()
        dMax = (self.GetShips()*9)
        return (int(random.randrange(dMin, dMax, 5)))

# Ships outrun by Player_Ship
    def Escape(self):
# How many ships are left behind
        outRun = random.randrange(1, 6, 1)
# Convert Ships to 100 damage each and reduce fleet defense.
        self.Damage(outRun * 100)
        return (outRun)

# Pirate damage determined by Player_Ship
    def Damage(self,pDamage):
        self.pirateDefense = (self.pirateDefense - pDamage)
        self.ships = (self.pirateDefense // 100)
        return (pDamage)


# -------[ END class pirateFleet ]---------


global Game_Date
global Trade_Port
global Trade_Items
global Player_Gold
global Player_WHouse
global Player_Ship
global Pirate_Fleet


def Clear_Screen():
    os.system('cls')
    
def Config_Game():
    global Game_Date
    global Trade_Port
    global Trade_Items
    global Player_Gold
    global Player_WHouse
    global Player_Ship
    global Pirate_Fleet

    Game_Date = gameDate()
    Trade_Items = TradeItems()
    Trade_Port = TradePort()
    Pirate_Fleet = pirateFleet(1)

    companyName = ""
    Clear_Screen()
    print("Welcome to the East Empire Trading Simulation!\n")
    companyName = input("What shall we use for a company name?\n")
    Player_Ship = playerShip(companyName)
    Player_Gold = playerGold(1000)
    Player_WHouse = playerWarehouse()


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
    line10 ="^^$$\_,,_.,.  ,, ..,/   "
    line11 ="$^!^^^!!^^^$$$$$!!!!^^^$"


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

def Get_Integer(iPrompt):

    RetVal = None
    while RetVal is None:
        try:
            RetVal = int(input(iPrompt))
        except ValueError:
            print("Not an integer!")

    return(RetVal)



def Select_TradeItem():

    Selection = ""

    while (Selection != "O") and (Selection != "S") and (Selection != "A") and (Selection != "G") and (Selection != "Q"):
        print(f"Sellect item: {cr.Fore.GREEN}O{cr.Fore.WHITE}pium ,{cr.Fore.GREEN}S{cr.Fore.WHITE}ilk, {cr.Fore.GREEN}A{cr.Fore.WHITE}rms ,or {cr.Fore.GREEN}G{cr.Fore.WHITE}eneral cargo?")
        Selection = input("[O,S,A,G,Q] ")
        if (len(Selection) > 0) :
            Selection = Selection[0].upper()

    match Selection:
        case "O":
            RetVal = 0
        case "S":
            RetVal = 1
        case "A":
            RetVal = 2
        case "G":
            RetVal = 3
        case "Q":
            RetVal = 9

    return(RetVal)
        

#
# ┌──────────────────────────────────────────────────────────────────────┐
# │                     Firm : The Peace Dividend                        │
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

def Print_GameStatus() :
    print(f"{cr.Fore.GREEN} ┌──────────────────────────────────────────────────────────────────────┐")
    print(f"{cr.Fore.GREEN} │" + ("Firm: " + Player_Ship.GetName()).center(70) + "│")
    print(f"{cr.Fore.GREEN} │  {cr.Fore.WHITE}" + Trade_Port.GetPortName().ljust(49),end="")
    print(f"{cr.Fore.GREEN}Date: {cr.Fore.WHITE}" + Game_Date.GetDate(),end="")
    print(f"{cr.Fore.GREEN}  │")
    print(f"{cr.Fore.GREEN} │ ┌────────────────────────────────────┐ ┌───────────────────────────┐ │")
    print(f"{cr.Fore.GREEN} │ │ Goods    Price   Ship   Warehouse  │ │ Gold On Hand : " + str("{:,}".format(Player_Gold.GetGoldOnHand())).ljust(11) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ ================================== │ │ Gold in Bank : " + str("{:,}".format(Player_Gold.GetGoldInBank())).ljust(11) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Trade_Items.GetItemName(0)).ljust(9) + str(Trade_Items.GetItemPrice(0)).ljust(8) + str(Player_Ship.GetItemQty(0)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(0))).ljust(11) + "│ │ Gold in Debt : " + str("{:,}".format(round(Player_Gold.GetGoldInDebt()))).ljust(11) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Trade_Items.GetItemName(1)).ljust(9) + str(Trade_Items.GetItemPrice(1)).ljust(8) + str(Player_Ship.GetItemQty(1)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(1))).ljust(11) + "│ ├───────────────────────────┤ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Trade_Items.GetItemName(2)).ljust(9) + str(Trade_Items.GetItemPrice(2)).ljust(8) + str(Player_Ship.GetItemQty(2)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(2))).ljust(11) + "│ │ Ship Capacity : " + (str(Player_Ship.GetCapacity()) + " / " + str(Player_Ship.GetMaxCapacity())).ljust(10) + "│ │")
    print(f"{cr.Fore.GREEN} │ │ " + str(Trade_Items.GetItemName(3)).ljust(9) + str(Trade_Items.GetItemPrice(3)).ljust(8) + str(Player_Ship.GetItemQty(3)).ljust(7) + str("{:,}".format(Player_WHouse.GetItemQty(3))).ljust(11) + "│ │ Ship Guns     : " + str(Player_Ship.GetGuns()).ljust(10) + "│ │")
    print(f"{cr.Fore.GREEN} │ │                  ================= │ │ Ship Defense  : "  + str(Player_Ship.GetDefense()).ljust(10) + "│ │")
    print(f"{cr.Fore.GREEN} │ │       Available  " + str(Player_Ship.GetCurrentCapacity()).ljust(7) + str("{:,}".format(Player_WHouse.GetCurrentCapacity())).ljust(11) + "│ │ Ship Status   : " + str(Player_Ship.GetStatus()).ljust(3) + "%      │ │")
    print(f"{cr.Fore.GREEN} │ └────────────────────────────────────┘ └───────────────────────────┘ │")
    print(f"{cr.Fore.GREEN} └──────────────────────────────────────────────────────────────────────┘")
    


# ┌──────────────────────────────────────────────────────────────────────┐
# │                               PIRATES!                               │
# │  ┌─────────────────────────────┐    ┌─────────────────────────────┐  │
# │  │  Pirate Ships   : 99        │    │  Gold On Hand  : 1,000,000  │  │
# │  │  Pirate Defense : 999       │    │                             │  │ 
# │  │                             │    │        Goods    Qty         │  │
# │  │ =========================== │    │ =========================== │  │
# │  │                             │    │        Opium   : 99         │  │
# │  │  Ship Status    : 100%      │    │        Silk    : 0          │  │
# │  │  Ship Defense   : 500       │    │        Arms    : 0          │  │
# │  │  Ship Guns      : 5         │    │        General : 0          │  │
# │  │  Ship Capacity  : 50 / 50   │    │                             │  │
# │  └─────────────────────────────┘    └─────────────────────────────┘  │
# └──────────────────────────────────────────────────────────────────────┘

def Print_AttackStatus() :
    print(f"{cr.Fore.GREEN} ┌──────────────────────────────────────────────────────────────────────┐")

    print(f"{cr.Fore.GREEN} │", end=" ")
    print(f"{cr.Fore.RED} " + str("PIRATES!").center(66)  , end=" ")
    print(f"{cr.Fore.GREEN} │")

    print(f"{cr.Fore.GREEN} │  ┌─────────────────────────────┐    ┌─────────────────────────────┐  │")
    print(f"{cr.Fore.GREEN} │  │  Pirate Ships   : " + str("{:,}".format(Pirate_Fleet.GetShips())).ljust(10) + "│    │  Gold On Hand  : " + str("{:,}".format(Player_Gold.GetGoldOnHand())).ljust(11) + "│  │")
    print(f"{cr.Fore.GREEN} │  │  Pirate Defense : " + str("{:,}".format(Pirate_Fleet.GetDefense())).ljust(10) + "│    │                             │  │")
    print(f"{cr.Fore.GREEN} │  │                             │    │        Goods    Qty         │  │")
    print(f"{cr.Fore.GREEN} │  │ =========================== │    │ =========================== │  │")
    print(f"{cr.Fore.GREEN} │  │                             │    │        Opium   : " + str("{:,}".format(Player_Ship.GetItemQty(0))).ljust(11) + "│  │")
    print(f"{cr.Fore.GREEN} │  │  Ship Status    : "  + str("{:,}".format(Player_Ship.GetStatus())).ljust(3) + "%      │    │        Silk    : " + str("{:,}".format(Player_Ship.GetItemQty(1))).ljust(11) + "│  │")
    print(f"{cr.Fore.GREEN} │  │  Ship Defense   : " + str("{:,}".format(Player_Ship.GetDefense())).ljust(10) + "│    │        Arms    : " + str("{:,}".format(Player_Ship.GetItemQty(2))).ljust(11) + "│  │")
    print(f"{cr.Fore.GREEN} │  │  Ship Guns      : " + str("{:,}".format(Player_Ship.GetGuns())).ljust(10) + "│    │        General : " + str("{:,}".format(Player_Ship.GetItemQty(3))).ljust(11) + "│  │")
    print(f"{cr.Fore.GREEN} │  │  Ship Capacity  : "  + (str(Player_Ship.GetCapacity()) + " / " + str(Player_Ship.GetMaxCapacity())).ljust(10) + "│    │                             │  │")
    print(f"{cr.Fore.GREEN} │  └─────────────────────────────┘    └─────────────────────────────┘  │")
    print(f"{cr.Fore.GREEN} └──────────────────────────────────────────────────────────────────────┘")

def Ship_UnderAttack():
    underAttack = True
    Pirate_Fleet.SetShips(random.randrange(1, 15, 1))
    piratesInitial = Pirate_Fleet.GetShips()

    while (underAttack):
        shipDamageTaken = Pirate_Fleet.Attack()
        Player_Ship.Damage(shipDamageTaken)
        Clear_Screen()
        print("Atacked: " + str(shipDamageTaken))
        Print_AttackStatus()
        Print_PirateShips(Pirate_Fleet.GetShips())


        RunFight = ""
        while (RunFight != "F") and (RunFight != "R") and (RunFight != "S"):
            print(f"{cr.Fore.WHITE}We're under attack.  Shall we {cr.Fore.GREEN}F{cr.Fore.WHITE}ight, {cr.Fore.GREEN}R{cr.Fore.WHITE}un, or {cr.Fore.GREEN}S{cr.Fore.WHITE}urrender?")
            RunFight = input("[F,R,S] ")
            if (len(RunFight)> 0) :
                RunFight = RunFight[0].upper()

        match RunFight:
            case "F" :
                pDamage = Pirate_Fleet.Damage(Player_Ship.Attack())   # Ship Attack is based on Guns in ship
                print(f"{cr.Fore.WHITE}We hit them with", pDamage, "damage.")

                if (Pirate_Fleet.GetShips() > 0) :
                    print(f"{cr.Fore.WHITE}There are still", Pirate_Fleet.GetShips(), "ships attacking!")
                else :
                    underAttack = False
                    print(f"{cr.Fore.WHITE}Victory!  We have sunk all of the attacking pirate ships!")
                    FlotsamQty = int(random.randrange(1, (piratesInitial+1), 1))
                    FlotsamItem = int(random.randrange(1, 4, 1))

                    if (FlotsamQty > Player_Ship.GetCurrentCapacity()):
                        FlotsamQty = Player_Ship.GetCurrentCapacity()
                    Player_Ship.AddItem(FlotsamItem,FlotsamQty)
                    print("We have recovered some flotsam and jetsam.",FlotsamQty, "of",Trade_Items.GetItemName(FlotsamItem))

            case "R" :
                pOutRun = Pirate_Fleet.Escape()

                if (Pirate_Fleet.GetShips() < 1):
                    underAttack = False
                    print(f"{cr.Fore.WHITE}We have escaped!")
                else :
                    print("We have outrun", pOutRun, "ships!")
        
            case "S" :
                StolenPct = (random.randrange(55, 90, 5) * .01)

                x = 0
                r = 0
                for x in range(4) :
                    r = int(Player_Ship.GetItemQty(x) * StolenPct)
                    Player_Ship.RemoveItem(x, r)
                    print("Pirates stole ", r, Trade_Items.GetItemName(x))
                    x = (x + 1)

                NewGold = 0
                NewGold = Player_Gold.GetGoldOnHand() - (int(Player_Gold.GetGoldOnHand() * StolenPct))

                Player_Gold.SetGoldOnHand(NewGold)
                print("Pirates stole", (StolenPct * 100), "percent of your gold and goods")
                Pirate_Fleet.SetShips(0)
                underAttack = False

        continueGame = input("Press <ENTER> to continue")
    

def Travel_toPort():
    global Game_Date

    Port_Desired = ""
    DaysAtSea = random.randrange(2, 7, 1)

    print(f"{cr.Fore.WHITE}Where would you like to go? {cr.Fore.GREEN}H{cr.Fore.WHITE}ong Kong, {cr.Fore.GREEN}B{cr.Fore.WHITE}atavia, {cr.Fore.GREEN}C{cr.Fore.WHITE}alcutta, {cr.Fore.GREEN}J{cr.Fore.WHITE}ambi, {cr.Fore.GREEN}M{cr.Fore.WHITE}uscat, {cr.Fore.GREEN}P{cr.Fore.WHITE}enang, {cr.Fore.GREEN}R{cr.Fore.WHITE}angoon, {cr.Fore.GREEN}S{cr.Fore.WHITE}urat")
    
    while (Port_Desired != "H") and (Port_Desired != "B") and (Port_Desired != "C") and (Port_Desired != "J") and (Port_Desired != "M") and (Port_Desired != "P") and (Port_Desired != "R") and (Port_Desired != "S") and (Port_Desired != "Q") :
        Port_Desired = input("Where would you like to go? ["+Trade_Port.GetPortCharList()+",Q] ")
        if (len(Port_Desired) > 0) :
            Port_Desired = Port_Desired[0].upper()

    match Port_Desired:
        case "H":
            newTradePort = 0
        case "B":
            newTradePort = 1
        case "C":
            newTradePort = 2
        case "J":
            newTradePort = 3
        case "M":
            newTradePort = 4
        case "P":
            newTradePort = 5
        case "R":
            newTradePort = 6
        case "S":
            newTradePort = 7
        case "Q":
            newTradePort = Trade_Port.GetPort()
            
    if (newTradePort == Trade_Port.GetPort()):
        print("We're already there!")
        Port_Desired = input("Press <ENTER> to continue")
    else :
        Game_Date.IncrementDate(DaysAtSea)
        Trade_Items.SetPrices()
        Trade_Port.SetPort(newTradePort)
        Disaster = random.randrange(1, 10, 1)
        if (Disaster > 7):
            Ship_UnderAttack()
        elif (Disaster < 2):
            Trade_Port.SetPort(random.randrange(1, 8, 1))
            print("Storm! We've been blown off course")
            Port_Desired = input("Press <ENTER> to continue")


def Buy_Cargo():
    Payment_State = 0
    bIndex = Select_TradeItem()
    if bIndex != 9 :
        Can_Afford = (Player_Gold.GetGoldOnHand() // Trade_Items.GetItemPrice(bIndex))
        print(f"Buy {Trade_Items.GetItemName(bIndex)}!")

        print(f"You can afford {Can_Afford} {Trade_Items.GetItemName(bIndex)}.")
        if (Can_Afford > Player_Ship.GetCurrentCapacity()) :
            print(f"You can only hold {Player_Ship.GetCurrentCapacity()} more {Trade_Items.GetItemName(bIndex)}.")

        Want_Buy = Get_Integer("How much do you want to buy? ")

        if (Want_Buy > 0) and (Want_Buy <= Can_Afford) :
            if (Player_Ship.AddItem(bIndex, Want_Buy) == False):
                print("Unable to complete the transaction.  Check capacity!")
                Want_Buy = input("Press <ENTER> to continue")
            else :
                Payment_State = (Player_Gold.SpendGold(Want_Buy * Trade_Items.GetItemPrice(bIndex)))
                if (Payment_State == 0) :
                    print("payment transfered")
                else :
                    print("payment declined")

        else :
            print("Invalid Amount Selected")
            Want_Buy = input("Press <ENTER> to continue")


   

def Sell_Cargo():
    sIndex = Select_TradeItem()
    Can_Sell = Player_Ship.GetItemQty(sIndex)
    print(f"Sell {Trade_Items.GetItemName(sIndex)}!")
    print(f"You have {Player_Ship.GetItemQty(sIndex)} of {Trade_Items.GetItemName(sIndex)} to sell.")

    Want_Sell = Get_Integer("How much do you want to sell? ")
    if (Want_Sell > 0) and (Want_Sell <= Can_Sell) :
        if (Player_Ship.RemoveItem(sIndex, Want_Sell) == False):
            print("Unable to complete the transaction.  Check capacity!")
            Want_Sell = input("Press <ENTER> to continue")
        else:
            Player_Gold.AddGold(Want_Sell * Trade_Items.GetItemPrice(sIndex))
    else:
        print("Invalid Amount Selected")
        Want_Sell = input("Press <ENTER> to continue")


def Visit_Bank():
    Bank_Amount = 0
    Bank_Action = ""

    while (Bank_Action != "D") and (Bank_Action != "W") and (Bank_Action != "B") and (Bank_Action != "R") and (Bank_Action != "Q") :
        print(f"Would you like to {cr.Fore.GREEN}D{cr.Fore.WHITE}eposit, {cr.Fore.GREEN}W{cr.Fore.WHITE}ithdraw, {cr.Fore.GREEN}B{cr.Fore.WHITE}orrow or {cr.Fore.GREEN}R{cr.Fore.WHITE}epay?")
        Bank_Action = input("[D,W,B,R,Q] ")
        if (len(Bank_Action) > 0) :
            Bank_Action = Bank_Action[0].upper()

    match Bank_Action:
        case "D":
            Bank_Amount = Get_Integer("How much would you like to deposit? ")
            if (Player_Gold.DepositGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "W":
            Bank_Amount = Get_Integer("How much would you like to withdraw? ")
            if (Player_Gold.WithdrawGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "B":
            Bank_Amount = Get_Integer("How much would you like to borrow? ")
            if (Player_Gold.BorrowGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  1000 Max!")
                Bank_Action = input("Press <ENTER> to continue")

        case "R":
            Bank_Amount = Get_Integer("How much would you like to repay? ")
            if (Player_Gold.RepayGold(Bank_Amount) == False):
                print("Unable to complete the transaction.  Insufficient Funds!")
                Bank_Action = input("Press <ENTER> to continue")

        case "Q":
                Bank_Action = input("Press <ENTER> to continue")


def Store_Cargo():
    sIndex = Select_TradeItem()
    onShip = int(Player_Ship.GetItemQty(sIndex))
    WarehouseSpace = Player_WHouse.GetCurrentCapacity()
    
    if (onShip > WarehouseSpace):
        Can_Store = WarehouseSpace
    else:
        Can_Store = onShip

    print(f"Store {Trade_Items.GetItemName(sIndex)}!")
    print("You can store", Can_Store, Trade_Items.GetItemName(sIndex),".")

    qty2Store = Get_Integer("How much do you want to store? ")

    while (qty2Store < 0) and (qty2Store > Can_Store):
        qty2Store = int(input("How much do you want to store? "))

    if (Player_Ship.RemoveItem(sIndex,qty2Store) == False):
        print("Unable to complete the transaction.  Check Ship cargo availability!")
    else:
        if (Player_WHouse.StoreItem(sIndex,qty2Store) == False):
            print("Unable to complete the transaction.  Check Warehouse capacity!")
        else:
            print("Stored", qty2Store,Trade_Items.GetItemName(sIndex))

    continueGame = input("Press <ENTER> to continue")


def Retrieve_Cargo():
    rIndex = Select_TradeItem()
    inWhouse = Player_WHouse.GetItemQty(rIndex)
    ShipSpace = Player_Ship.GetCurrentCapacity()
    
    if (inWhouse > ShipSpace):
        Can_Retrieve = ShipSpace
    else: 
        Can_Retrieve = inWhouse

    print(f"Retrieve {Trade_Items.GetItemName(rIndex)}!")
    print("You can retrieve", Can_Retrieve, Trade_Items.GetItemName(rIndex),".")

    qty2Retrieve = Get_Integer("How much do you want to retrieve? ")
    while (qty2Retrieve < 0) and (qty2Retrieve > Can_Retrieve):
        print("You can retrieve", Can_Retrieve, Trade_Items.GetItemName(rIndex),".")
        qty2Retrieve = int(input("How much do you want to retrieve ?"))

    print(f"Retrieve {Trade_Items.GetItemName(rIndex)}!")

    if (Player_WHouse.RetrieveItem(rIndex,qty2Retrieve) == False):
        print("Unable to complete the transaction.  Check Warehouse capacity!")
    else:
        if (Player_Ship.AddItem(rIndex,qty2Retrieve) == False):
            print("Unable to complete the transaction.  Check Ship cargo availability!")
            print("Returning cargo")
            Player_WHouse.StoreItem(rIndex,qty2Retrieve)
        else:
            print("Retrieved", qty2Retrieve,Trade_Items.GetItemName(rIndex))

    continueGame = input("Press <ENTER> to continue")


def Use_Warehouse():
    xfer_Amount = 0
    xfer_Item = 0
    Whse_Action = ""

    while (Whse_Action != "S") and (Whse_Action != "R") and (Whse_Action != "Q"):
        print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}S{cr.Fore.WHITE}tore or {cr.Fore.GREEN}R{cr.Fore.WHITE}etrieve items from the warehouse?")
        Whse_Action = input("[S,R,Q] ")
        if (len(Whse_Action) > 0) :
            Whse_Action = Whse_Action[0].upper()

    match Whse_Action:
        case "S":
            Store_Cargo()
        case "R":
            Retrieve_Cargo()


def Repair_Ship():
    dAmount = Player_Ship.GetDamage()
    repCost = (dAmount * 10)

    print("Repairing a ship costs 10 gold per damage point.")
    print("Your ship has "+str(dAmount)+" damage points.")
    print("It will cost "+str(repCost)+" to fully repair your ship.")
    Want_Repair = Get_Integer("How much DAMAGE do you want to repair? ")

    if ((Want_Repair * 10) > Player_Gold.GetGoldOnHand()):
        print("Unable to complete the transaction.  Insufficient Funds!")
        Want_Repair = input("Press <ENTER> to continue")
    else :
        if (Want_Repair > Player_Ship.GetDamage()):
            print("Unable to complete the transaction.  Check damage!")
            Want_Repair = input("Press <ENTER> to continue")
        else :
            Player_Gold.SpendGold(Want_Repair * 10)
            Player_Ship.Repair(Want_Repair)
   

def Play():

    Clear_Screen()
    Print_GameStatus() 

    print("\n")
    User_Action = ""
    if (Trade_Port.GetPort() == 0):  # Hong Kong has more services
    
        while (User_Action != "B") and (User_Action != "S") and (User_Action != "V") and (User_Action != "W") and (User_Action != "R") and (User_Action != "T"):
            print(f"{cr.Fore.WHITE}Would you like to {cr.Fore.GREEN}B{cr.Fore.WHITE}uy, {cr.Fore.GREEN}S{cr.Fore.WHITE}ell, {cr.Fore.GREEN}V{cr.Fore.WHITE}isit the Bank, use the {cr.Fore.GREEN}W{cr.Fore.WHITE}arehouse, {cr.Fore.GREEN}R{cr.Fore.WHITE}epair your ship, or {cr.Fore.GREEN}T{cr.Fore.WHITE}ravel to a new port?")
            User_Action = input("[B,S,V,W,R,T] ")
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
            User_Action = input("[B,S,T] ")
            if (len(User_Action) > 0) :
                User_Action = User_Action[0].upper()
  
        match User_Action:
            case "B":
                Buy_Cargo()
            case "S":
                Sell_Cargo()
            case "T":
                Travel_toPort()
    
# End Play()



def main():
  
    Config_Game()
    
    while (Player_Gold.GetGoldOnHand() < 10000000):
        Play()


if __name__ == "__main__":
    main()

