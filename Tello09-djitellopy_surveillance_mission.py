from djitellopy import Tello
import cv2
import time
from threading import Thread

speed = 40
command_time_seconds = 3


# Have the Tello fly Up and Down
def flight_pattern():
    print("Takeoff!")
    tello.takeoff()

    if not tello.is_flying:
        
        tello.takeoff()

    time.sleep(1)

    tello.move_up(100)
    tello.rotate_clockwise(360)
    tello.rotate_counter_clockwise(360)
    tello.move_down(50)

    time.sleep(1)
    up_flag = True
    t1 = time.time()

    while True:
        if time.time() - t1 > 3:
            t1 = time.time()
            if up_flag == True:
                up_flag = False
                # Up
                tello.send_rc_control(0, 0, 0, speed)
            else:
                up_flag = True
                tello.send_rc_control(0, 0, 0, -speed)


print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

time.sleep(2)

print("Turn Video Stream On")
tello.streamon()

# read a single image from the Tello video feed
print("Read Tello Image")
frame_read = tello.get_frame_read()

# create a thread to run the function
flight_pattern_thread = Thread(target=flight_pattern, daemon=True)
flight_pattern_thread.start()

time.sleep(2)


print('Press:  q  to quit')
while True:
    # read a single image from the Tello video feed
    tello_video_image = frame_read.frame

    # use opencv to write image
    if tello_video_image is not None:
        cv2.imshow("TelloVideo", tello_video_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


tello.land()
time.sleep(1)

tello.streamoff()
cv2.destroyWindow('TelloVideo')
cv2.destroyAllWindows()