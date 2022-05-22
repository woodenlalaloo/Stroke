from clear import clear
from time import sleep
respawnPrompt = input("Type 1 to respawn. Type 2 to exit.")
if respawnPrompt == "1":
    print("Respawning...")
    sleep(4)
    clear()
    exec(open("cutscene1.py").read())
if respawnPrompt == 2:
    print("Exiting...")
    sleep(3)
    clear()
    quit()
