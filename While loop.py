Command = ""
while Command != "end" :
    Command = input(">  ")
    if Command =="start":
        print("Car is started /././././././")
    elif Command == "stop":
        print("Car stoped ///")
    elif Command == "help":
        print("""
        start-- start the car 
        stop--- spot the car 
        help---- for help
        end----- end for ending the game 
        """)
    elif Command == "end":
        print("THE GAME END")
        break
    else:
     print("Sorry invalid input ")