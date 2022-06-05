import tkinter as tk
window = tk.Tk()
window.title("Taipan!")
# window.geometry('600x400+50+50')

window_width = 800
window_height = 800

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)

label = tk.Label(
    text="Python rocks!",
    foreground="green",
    background="black"
    )
label.pack()
window.mainloop()
