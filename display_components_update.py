import time
from init_global_variables_update import *
from handle_update_actions import *
from tkinter import *
from tkinter import ttk


def config_display_screen():
    windowWidth = 350
    windowHeight = 170 if have_new_version else 100
    screenWidth = win.winfo_screenwidth()
    screenHeight = win.winfo_screenheight()
    xCordinate = int((screenWidth/2) - (windowWidth/2))
    yCordinate = int((screenHeight/2) - (windowHeight/2))
    win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
    win.resizable(width=0, height=0)
    win.iconbitmap("temp/print.ico")
    win.title("Update Silent Print")


def display_frame():
    global directory_frame
    height = 140 if have_new_version else 70
    directory_frame = ttk.LabelFrame(win, text='Update version', width=310, height=height)
    directory_frame.place(x=20, y=10)


def display_progress_bar():
    progress = ttk.Progressbar(win, orient = HORIZONTAL, length = 275, mode = 'determinate')
    progress.place(x=40, y=70)

    # Default progressbar
    display_update_status("Downloading...")
    progress['value'] = 10
    win.update_idletasks()
    time.sleep(2)
    progress['value'] = 30
    win.update_idletasks()

    if download_new_version():
        display_update_status("Installing...")
        progress['value'] = 70
        win.update_idletasks()
    else:
        time.sleep(3)
        win.destroy()

    if install_new_version():
        display_update_status("Configuring...")
        progress['value'] = 90
        win.update_idletasks()
    else:
        time.sleep(3)
        win.destroy()

    if update_version_to_config():
        display_update_status("Complete")
        progress['value'] = 100
        win.update_idletasks()
        time.sleep(3)
        notify_message("Update successfully")
        win.destroy()
    else:
        notify_message("Configuring failed")
        time.sleep(3)
        win.destroy()



def display_update_status(label):
    status_label = Label(directory_frame, height=2, width=30, padx="8px", text= label, anchor=W)
    status_label.place(x=5, y=75)


def display_version_label(label):
    text = ("You have a new version: " + label) if have_new_version else "Everything is up to date"
    version_label = Label(directory_frame, height=2, width=30, padx="8px", text= text, anchor=W)
    version_label.place(x=5, y=0)

    if(have_new_version):
        update_btn = ttk.Button(win, width=12, text="Update now", command= lambda: update_to_new_version(display_progress_bar), style="Accent.TButton")
        update_btn.place(x=210, y=100)
