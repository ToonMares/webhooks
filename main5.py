
print("It's on!")

from dhooks import Webhook
import time

message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))

while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Sent.")