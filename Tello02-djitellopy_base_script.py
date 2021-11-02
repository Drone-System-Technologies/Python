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

print("Hover for 10 seconds")
time.sleep(10)

print("Landing")
tello.land()
print("Flight Completed!")
