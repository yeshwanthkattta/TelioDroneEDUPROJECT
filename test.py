from djitellopy import Tello

me = Tello()
me.connect(False)              # Avoid waiting for state packets
battery = me.query_battery()  # Manual battery check
print("Battery:", battery, "%")
