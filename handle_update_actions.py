from init_global_variables_update import *
import requests
import subprocess
from tkinter import ttk
from threading import Thread
import concurrent.futures



def update_to_new_version(display_progress_bar):
    display_progress_bar()
    update_btn = ttk.Button(win, width=12, text="Update now")
    update_btn["state"] = "disabled"
    update_btn.place(x=210, y=100)


def downloading():
    global download_url
    print("download now...")
    filename = "silent_print.exe"
    file_path = os.path.join(current_folder, filename)
    schema = "http://"
    download_url = schema + download_url

    try:
        request = requests.get(download_url, stream=True)
        if request.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in request.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())

            return True
        
        notify_message("Download failed: status code {}".format(request.status_code))
        return False
    except:  # HTTP status code 4XX/5XX
        notify_message("Download failed: status code {}".format(request.status_code))
        return False

 
def download_new_version():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(downloading)
        return f1.result()
    


def opening_new_version():
    filename = "silent_print.exe"
    path_to_new_version_exe = os.path.join(current_folder, filename)
    subprocess.run(path_to_new_version_exe)


def install_new_version():
    print("installing now...")

    try:
        t = Thread(target=opening_new_version)
        t.start()

        return True
    except:
        notify_message("Installing failed")
        return False     



def update_version_to_config():
    print("config now...")

    try:
        config.set('VERSION','version', server_version)
        with open('temp/CONFIG.INI', 'w') as configfile:
            config.write(configfile)
        
        return True
    except:
        return False        
            

