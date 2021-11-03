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

# Tell Tello to forward, right, and up at a speed of 20cm/s
print("Go x,y,z: (50,-50,50)")
tello.go_xyz_speed(50,-50,50, 20)

# Tell Tello to go backwards, left, and down at a speed of 20cm/s
print("Go x,y,z: (-50,50,-50)")
tello.go_xyz_speed(-50,50,-50, 20)

# Issue the land command
print("Landing")
tello.land()

# Tell us the flight has finished
print("Flight Completed!")
