from djitellopy import Tello

# Create the Tello Object
print("Create Tello Object")
tello = Tello()

# Issue command to connect
print("Connect to Tello")
tello.connect()

# Get battery level
battery_level = tello.get_battery()
print(f"Battery Percentage: {battery_level}")


# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)  # downward detection only

# Tell Tello to take off
print("Takeoff!")
tello.takeoff()

pad = tello.get_mission_pad_id()

# detect and react to pads until we see pad #1
while pad != 1:
    
    if pad == 3:
        tello.rotate_clockwise(90)
        tello.move_forward(50)

    if pad == 4:
        tello.rotate_counter_clockwise(90)
        tello.move_forward(50)
        
    if pad == 2:
        tello.rotate_counter_clockwise(90)
        tello.move_forward(50)

    pad = tello.get_mission_pad_id()

tello.rotate_clockwise(90)

# graceful termination
tello.disable_mission_pads()
tello.land()
tello.end()

# Tell us the flight has finished
print("Flight Completed!")

