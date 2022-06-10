import os
import random
#from colorama import Fore, Back, Style

global Company_Name
global Port_Names               # Constant? 
global TradedItems_Name         # Constant? 
global TradedItems_Price
global TradedItems_InShip
global TradedItems_InWarehouse
global Silver_OnHand
global Silver_InBank
global Ship_Capacity
global Current_Port

global User_Action

Port_Names = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
TradedItems_Name = ["Silk", "Tea", "Gunpowder", "Opium"]
TradedItems_Price = [20, 10, 50, 500]
Current_Port = 0

def Clear_Screen():
    os.system('cls')

def Config_Player():
    global Company_Name
    global Ship_Capacity
    global Silver_OnHand
    global Silver_InBank
    global TradedItems_InShip
    global TradedItems_InWarehouse

    Clear_Screen()
    print("Welcome to the East Empire Trading Simulation!\n")
    Company_Name = input("What shall we use for a company name?\n")
    Ship_Capacity = 15
    Silver_OnHand = 1000
    Silver_InBank = 0
    TradedItems_InShip = [0, 0, 0, 0]
    TradedItems_InWarehouse = [0, 0, 0, 0]

def Show_Status():
    global TradedItems_Name
    global TradedItems_Price
    global Silver_OnHand
    global Ship_Capacity
    global TradedItems_InShip

    Clear_Screen()
    Game_Banner = Company_Name + " in the port of " + Port_Names[Current_Port]
    
    print(Game_Banner.center(80)+"\n")
    print('\033[32m' + "CURRENT PRICES")
    for i in range(4):
        print(TradedItems_Name[i].ljust(10) + ": " + str(TradedItems_Price[i]).rjust(3))

    print('\033[32m' + "\nSHIP CARGO")
    for i in range(4):
        print(TradedItems_Name[i].ljust(10) + ": " + str(TradedItems_InShip[i]).rjust(3))


    FreeSpace_InShip = int(Ship_Capacity - TradedItems_InShip[0] - TradedItems_InShip[1] - TradedItems_InShip[2] - TradedItems_InShip[3])
    print(f"Availabile space in ship: {FreeSpace_InShip} of {Ship_Capacity}")
    print('\033[39m')
    print(f"Silver on hand: {Silver_OnHand}")


def Set_Prices():
    global TradedItems_Price
    TradedItems_Price = [random.randrange(5, 45, 1), random.randrange(2, 25, 1), random.randrange(5, 55, 1), random.randrange(300, 999, 1)]

def Travel_toPort():
    global Current_Port

    print('\033[39m')
    print(f"Ports: [H,B,C,J,M,P,R,S]")
    for i in range(7):
        print(Port_Names[i])

    Port_Desired = input("invalid selection. \nWhere would you like to go? [H,B,C,J,M,P,R,S]")[0].upper()
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
    global Silver_OnHand
    global Ship_Capacity
    global TradedItems_InShip

    print(f"Buy {TradedItems_Name[tI]}!")
    Can_Buy = Silver_OnHand // TradedItems_Price[tI]
    print(f"You can afford {Can_Buy} {TradedItems_Name[tI]}.")
    Want_Buy = int(input("How much do you want to buy?"))
    if (Want_Buy > Can_Buy):
        print("You cannot afford that much!")
    elif (Want_Buy > Ship_Capacity):
        print("Your ship cannot hold that much!")
    else:
        Silver_OnHand = (Silver_OnHand - Want_Buy * TradedItems_Price[tI])
        TradedItems_InShip[tI] = (TradedItems_InShip[tI] + Want_Buy)

def Sell_Cargo(tI):
    global TradedItems_Name
    global TradedItems_Price
    global Silver_OnHand
    global Ship_Capacity
    global TradedItems_InShip

    print(f"Sell {TradedItems_Name[tI]}!")

    Can_Sell = TradedItems_InShip[tI]
    print(f"You can sell {Can_Sell} {TradedItems_Name[tI]}.")
    Want_Sell = int(input("How much do you want to sell?"))
    if (Want_Sell > Can_Sell):
        print(f"You do not have that much {TradedItems_Name[tI]}!")
    else:
        Silver_OnHand = (Silver_OnHand + Want_Sell * TradedItems_Price[tI])
        TradedItems_InShip[tI] = (TradedItems_InShip[tI] - Want_Sell)


def Buy_SelectItem():
    global TradedItems_Name
    Clear_Screen()
    Show_Status()
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
    global TradedItems_Name
    Clear_Screen()
    Show_Status()
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



def Play():
    Clear_Screen()
    Show_Status()
    
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
            print("What?")

    Show_Status()


def main():
    global Silver_OnHand
    
    Clear_Screen()
    Config_Player()

    Set_Prices()
    while (Silver_OnHand < 10000000):
        Play()


if __name__ == "__main__":
    main()
