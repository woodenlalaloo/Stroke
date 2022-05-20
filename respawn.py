respawnPrompt = input("Type 1 to respawn. Type 2 to exit.")
if respawnPrompt == "1":
    print("Respawning...")
    exec(open("cutscene1.py").read())
if respawnPrompt == 2:
    print("Exiting...")
    quit()
