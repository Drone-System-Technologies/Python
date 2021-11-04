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

tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_forward(100)
tello.rotate_counter_clockwise(90)
tello.move_up(50)
tello.move_forward(100)
tello.flip_left()
tello.rotate_counter_clockwise(180)
tello.move_forward(100)
tello.move_down(50)
tello.rotate_clockwise(180)

# Issue the land command
print("Landing")
tello.land()

# Tell us the flight has finished
print("Flight Completed!")

