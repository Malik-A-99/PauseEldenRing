import psutil as ps
import keyboard
import time
import customtkinter as ctk
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def pauseMenu():
    posX = int((screensize[0]/2)-160)
    posY = int((screensize[1]/2)-120)

    print(posX, posY)

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')

    root = ctk.CTk()
    root.geometry('320x240+' + str(posX) + '+' + str(posY))

    label = ctk.CTkLabel(root, text='Game has been paused!')
    label.place(relx=0.5, rely=0.4, anchor = ctk.CENTER)

    button = ctk.CTkButton(root, text='~Resume~', command=root.destroy)
    button.place(relx=0.5, rely=0.6, anchor = ctk.CENTER)

    root.wm_attributes('-topmost', 1)
    root.overrideredirect(True)
    root.mainloop()


def checkForEldenRingProcess():
    processes = ps.process_iter()
    for process in processes:
        if process.name() == "eldenring.exe":
            return process.pid
        else:
            pass

while True:
    pid = checkForEldenRingProcess()
    if pid == None:
        print('exe is not running!')
        pass
    else:
        break
    time.sleep(0.5)

print(pid)
EldenRing = ps.Process(pid)
print(EldenRing)

def main():
    print("Staring the script")
    while True:
        try:
            if keyboard.is_pressed('`'):
                print("Suspending the process!")
                time.sleep(0.15)
                EldenRing.suspend()
                
                pauseMenu()
                time.sleep(0.2)
                
                EldenRing.resume()
                print("Resuming the process!")

                # while True:
                #     if keyboard.is_pressed('`'):
                #         print("Resuming the process!")
                #         EldenRing.resume()
                #         pause.menu.destroy()
                #         break

                #     time.sleep(0.15)
        except:
            print('Process is not running anymore, quitting application... ')
            exit()
        time.sleep(0.15)

main()
