from global_variables import *


# CONFIG PRINTER -------------------------------------------------
def select_printer_a4(selection):
    global printer_a4
    printer_a4 = selection
    save_printer_to_config(printer_a4, "printer_a4")


def select_printer_a5(selection):
    global printer_a5
    printer_a5 = selection
    save_printer_to_config(printer_a5, "printer_a5")


def select_printer_a6(selection):
    global printer_a6
    printer_a6 = selection
    save_printer_to_config(printer_a6, "printer_a6")


def save_printer_to_config(printer, config_selection):
    config.set("CONFIG", config_selection, printer)
    with open('temp/CONFIG.INI', 'w') as configfile:
        config.write(configfile)


