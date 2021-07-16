import keyboard
while(True):
    if keyboard.read_key() == "w":
        print("w is pressed")
    if keyboard.read_key() == "a":
        print("a is pressed")
    if keyboard.read_key() == "d":
        print("d is pressed")    
    if keyboard.read_key() =="esc":
        break