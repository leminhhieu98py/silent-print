from tkinter.constants import NO
from tkinter import *
from init_global_variables_update import *
from display_components_update import *



# Display functions only
if(server_version and download_url):
    config_display_screen()
    display_frame()
    display_version_label(server_version)

if __name__ == '__main__':
    if(server_version and download_url):
        win.mainloop()

