from djitellopy import tello

from time import sleep

me = tello.Tello()

me.connect(False)              # Avoid waiting for state packets
battery = me.query_battery()  # Manual battery check
print("Battery:", battery, "%")

me.takeoff()
me.send_rc_control(0, 0, 0, 0)
sleep(2)
me.send_rc_control(0, 60, 0, 0)

sleep(2)


me.send_rc_control(40, 0, 0, 0)


sleep(4.5)


me.send_rc_control(0, 50, 0, 0)
sleep(2)
me.send_rc_control(50, 0, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(6)


me.land()
