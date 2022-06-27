from tkinter import *
from tkinter import ttk

Port_Names = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]
TradedItems_Name = ["Silk", "Tea", "Gunpowder", "Opium"]
TradedItems_Price = [20, 10, 50, 500]
Current_Port = 0


GameWindow = Tk()
GameWindow.title("Taipan!")

window_width = 800
window_height = 800

# get the screen dimension
screen_width = GameWindow.winfo_screenwidth()
screen_height = GameWindow.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
GameWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#GameWindow.resizable(False, False)

GameFrame = ttk.Frame(GameWindow, borderwidth=5, relief="ridge", padding="10")
GameFrame.grid(column=0, row=0, sticky=(N, W, E, S))

GameWindow.columnconfigure(0, weight=1)
GameWindow.rowconfigure(0, weight=1)

Current_Port_Name = StringVar()
Current_Port_Name = Port_Names[Current_Port]

ttk.Label(GameFrame, textvariable=Current_Port_Name).grid(column=1, row=1, sticky=(W, E))
#Port_Indicator.grid_rowconfigure(1, weight=1)
#Port_Indicator.grid_columnconfigure(1, weight=2)

#meters="2"
#meters = StringVar()
ttk.Label(GameFrame, text=Current_Port_Name).grid(column=2, row=2, sticky=(W, E))



GameWindow.mainloop()