from djitellopy import Tello
import time

# Create the Tello Object
print("Create Tello Object")
tello = Tello()

# Issue command to connect
print("Connect to Tello")
tello.connect()

# Get battery level
battery_level = tello.get_battery()
print(f"Battery Percentage: {battery_level}")

# Tell Tello to take off
print("Takeoff!")
tello.takeoff()

# Tell Tello to fly left at 20 cm/s
print("Fly Left")
tello.send_rc_control(-20, 0, 0, 0)
time.sleep(4)

print("Stop and Sleep 1/2 second")
tello.send_rc_control(0, 0, 0, 0)
time.sleep(0.5)

# Tell Tello to fly right at 20 cm/s
print("Fly Right")
tello.send_rc_control(20, 0, 0, 0)
time.sleep(4)

print("Stop and Sleep 1/2 second")
tello.send_rc_control(0, 0, 0, 0)
time.sleep(0.5)

# Tell Tello to fly up at 20 cm/s
print("Fly Up")
tello.send_rc_control(0, 0, 20, 0)
time.sleep(3)

# Tell Tello to fly forward at 20 cm/s
print("Fly Forward")
tello.send_rc_control(0, 20, 0, 0)
time.sleep(3)

# Tell Tello to rotate clockwise at 50 cm/s
print("Rotate Clockwise")
tello.send_rc_control(0, 0, 0, 50)
time.sleep(3)

# Tell Tello to rotate counter-clockwise at 50 cm/s
print("Rotate Counter-Clockwise")
tello.send_rc_control(0, 0, 0, -50)
time.sleep(3)

# Tel Tello to fly backwards at 20 cm/s
print("Fly Back")
tello.send_rc_control(0, -20, 0, 0)
time.sleep(3)

# Tell Tello to fly down at 20 cm/s
print("Fly Down")
tello.send_rc_control(0, 0, -20, 0)
time.sleep(3)

# Tell Tello to rotate clockwise at 100 cm/s
print("Rotate Clockwise")
tello.send_rc_control(0, 0, 0, 100)
time.sleep(3)

# Tell Tello to stop controls
print("Stop and Sleep 1/2 second ")
tello.send_rc_control(0, 0, 0, 0)
time.sleep(0.5)

# Issue the land command
print("Landing")
tello.land()

# Tell us the flight has finished
print("Flight Completed!")
