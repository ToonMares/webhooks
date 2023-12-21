import os
import time
from dhooks import Webhook

webhook_url = Webhook("WEBHOOK_HERE")

# Get the computer's name
computer_name = os.getenv('COMPUTERNAME')

# Get the current time
current_time = time.strftime("%I:%M %p")  # Format time as 6:09 PM

# Get the screen resolution (requires Windows-specific solution)
import ctypes
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
resolution = f"{screen_width}x{screen_height}"

# Create the message
message = f"{computer_name} has opened the file at {current_time} with the resolution of {resolution}"

# Sending the message to Discord
while True:
    webhook_url.send(message)
    print("Sent message!")
    time.sleep(60)  # Sending message every 60 seconds
