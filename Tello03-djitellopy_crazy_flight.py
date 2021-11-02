from djitellopy import Tello
import time

print("Create Tello Object")
tello = Tello()

print("Connect to Tello")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Percentage: {battery_level}")

print("Takeoff!")
tello.takeoff()

tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_forward(100)
tello.rotate_counter_clockwise(90)
tello.move_up(100)
tello.move_forward(100)
tello.flip_left()
tello.rotate_counter_clockwise(180)
tello.move_forward(100)
tello.move_down(100)
tello.rotate_clockwise(180)

print("Landing")
tello.land()
print("Flight Completed!")
