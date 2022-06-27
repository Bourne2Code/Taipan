import tkinter as tk
import tkinter.ttk as ttk

GameWindow = tk.Tk()
GameWindow.title("Taipan!")

window_width = 800
window_height = 800

# get the screen dimension
screen_width = GameWindow.winfo_screenwidth()
screen_height = GameWindow.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# GameWindow.geometry('600x400+50+50')
# set the position of the window to the center of the screen
GameWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
GameWindow.resizable(False, False)

label = tk.Label(
    text="Python rocks!",
    foreground="green",
    background="black"
    )
label.pack()
GameWindow.mainloop()
