from djitellopy import Tello
import cv2
import time

print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

time.sleep(2)

print("Turn Video Stream On")
tello.streamon()

frame_read = tello.get_frame_read()

print("Takeoff!")
tello.takeoff()

print("Picture Taken in 3 seconds")
time.sleep(1)
print("Picture Taken in 2 seconds")
time.sleep(1)
print("Picture Taken in 1 second")
time.sleep(1)

# read a single image from the Tello video feed
print("SNAP! Picture Taken")
tello_video_image = frame_read.frame

print("Save tello-picture.jpg to Thonny files folder")
# use opencv to write image
cv2.imwrite("tello-picture.jpg", tello_video_image)

print("Land")
tello.land()

print("Turn Video Stream Off")
tello.streamoff()
