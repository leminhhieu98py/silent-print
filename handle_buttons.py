from global_variables import *
from print import *


# CONFIG PRINTER -------------------------------------------------
def select_printer(selection):
    global printer
    printer = selection
    save_printer_to_config(printer)


def save_printer_to_config(printer):
    config.set("CONFIG", "printer", printer)
    with open('temp/CONFIG.INI', 'w') as configfile:
        config.write(configfile)


