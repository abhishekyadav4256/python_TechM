import time

lights = ["Red", "Green", "Yellow"]

while True:
    for light in lights:
        if light == "Red":
            print("Red Light - Stop")
            time.sleep(3)
        elif light == "Green":
            print("Green Light - Go")
            time.sleep(3)
        elif light == "Yellow":
            print("Yellow Light - Caution")
            time.sleep(2)
