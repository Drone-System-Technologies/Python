# This script shows how to send/receive commands to/from Tello using UDP
# This script shows how to receive battery status from Tello
# This script shows how to print message received from Tello

# Import the built-in socket and time modules
import socket
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# Create a UDP connection to send the command
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to a local port on our computer where Tello can send messages
sock.bind(('', 9000))

# Function to send messages to Tello
def send(message):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

# Function to listen for messages from Tello and prints them to the screen
def receive():
  try:
    response, ip_address = sock.recvfrom(128)
    print("Received message: " + response.decode(encoding='utf-8') + " from Tello with IP: " + str(ip_address))
  except Exception as e:
    print("Error receiving: " + str(e))

# Send Tello into command mode
send("command")

# Receive response from Tello
receive()

# Delay 3 seconds before we send the next command
time.sleep(3)

# Ask Tello about battery status
send("battery?")

# Receive battery response from Tello
receive()

# Close the UDP socket
sock.close()