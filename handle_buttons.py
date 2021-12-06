from global_variables import *


# CONFIG PRINTER -------------------------------------------------
def select_printer_1(selection):
    global printer_1
    printer_1 = selection
    save_printer_to_config(printer_1, "printer_1")


def select_printer_2(selection):
    global printer_2
    printer_2 = selection
    save_printer_to_config(printer_2, "printer_2")


def select_printer_3(selection):
    global printer_3
    printer_3 = selection
    save_printer_to_config(printer_3, "printer_3")


def save_printer_to_config(printer, config_selection):
    config.set("CONFIG", config_selection, printer)
    with open('temp/CONFIG.INI', 'w') as configfile:
        config.write(configfile)


