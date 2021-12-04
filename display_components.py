from tkinter import *
from tkinter import ttk
import pystray
from pystray import MenuItem as item
import PIL.Image

from handle_buttons import *
from global_variables import *



directory_frame = ""

def quit_window():
    icon.stop()
    win.destroy()


def show_window():
    win.after(0, win.deiconify())
    win.mainloop()


def hide_window():
    global icon
    win.withdraw()
    try:
        image = PIL.Image.open("temp/print.ico")
        menu = (item('Show application', show_window), item('Quit', quit_window))
        icon = pystray.Icon("name", image, "Silent print application", menu)
        icon.run()
    except Exception as e:
        pass


def display_frame():
    global directory_frame
    directory_frame = ttk.LabelFrame(win, text='Silent Print', width=380, height=110)
    directory_frame.place(x=10, y=10)


def config_app_screen():
    windowWidth = 400
    windowHeight = 130
    screenWidth = win.winfo_screenwidth()
    screenHeight = win.winfo_screenheight()
    xCordinate = int((screenWidth/2) - (windowWidth/2))
    yCordinate = int((screenHeight/2) - (windowHeight/2))
    win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
    win.resizable(width=0, height=0)
    win.iconbitmap("temp/print.ico")
    win.title("Silent Print Application")


def display_printer(label):
    e = StringVar()
    e.set(printer)
    optionmenu = ttk.OptionMenu(directory_frame, e, *printer_list, command=select_printer)
    optionmenu.place(x=10, y=10, width=360)


def display_guide_label():
    guide_label = Label(directory_frame, text='Chosen printer is used for next papers')
    guide_label.place(x=10, y=60)


win.protocol('WM_DELETE_WINDOW', hide_window)
