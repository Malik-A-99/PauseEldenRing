import psutil as ps
import keyboard
import time

def checkForEldenRingProcess():
    processes = ps.process_iter()
    for process in processes:
        if process.name() == "eldenring.exe":
            return process.pid

while True:
    pid = checkForEldenRingProcess()
    if pid == None:
        pass
    else:
        break
    time.sleep(0.5)

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
