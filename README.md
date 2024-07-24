![alt text](https://github.com/Malik-A-99/PauseEldenRing/blob/main/preview.jpg?raw=true)

# Pause Elden Ring
This script allows you to suspend and resume the eldenring.exe process by pressing the key, "`" (back tick)
This script needs the keyboard, psutil, and time library.
This script currently works on Windows only.
---
# DISCLAIMER
1. This script reads the processes that are currently being run on your windows machine until it finds the specified process that you wish to suspend!
2. This script also reads the keyboard inputs and waits for the user to press the back tick [  `  ] key!
---
**INSTALLATION:**
1. Download and install python from the microsoft store (or from the website, https://www.python.org/downloads/)
2. Extract the files to its own folder
3. Once you are in the folder, run `install.bat`
4. After that, you can open command prompt in that folder by typing `cmd` in the url bar at the top.
5. Once command prompt is open in the appropriate directory, type, `python3 PauseEldenRing.py`
6. You can then pause the game by pressing [ ` ]
---
**NOTES:**
- This script will continuously check to see if `eldenring.exe` is running or not.
- This script will only suspend the process, `eldenring.exe`. You can change the code to suspend any application by changing `eldenring.exe` to whichever process you want to suspend/resume.
- This has not been tested with modded versions of the game (seamless co-op, etc.) Use at your own risk!
- This script has been tested with flawless widescreen.
---
**UNINSTALL:**
1. Run `uninstall.bat` and answer both prompts with `y`. This will remove the libraries associated with the script. This will make the script un-usable.
2. After you run uninstall.bat you can delets the files and folder to completely remove everything.
