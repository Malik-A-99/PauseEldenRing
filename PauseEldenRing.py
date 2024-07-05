#MAKE SURE TO RUN THIS SCRIPT AFTER RUNNING ELDEN RING OR IT WILL NOT WORK

import psutil as ps
import keyboard
import time

pid = 0

processes = ps.process_iter()
for process in processes:
    if process.name() == "eldenring.exe":
        pid = process.pid

print(pid)
EldenRing = ps.Process(pid)
print(EldenRing)

def main():
    print("Starting Loop!")
    while True:
        if keyboard.is_pressed('`'):
            print("Pausing the game!")
            time.sleep(0.2)
            EldenRing.suspend()

            while True:
                if keyboard.is_pressed('`'):
                    print("Resuming the game!")
                    EldenRing.resume()
                    break

                time.sleep(0.2)
        time.sleep(0.2)

main()