print("It's working!")

from dhooks import Webhook
import time

message = "User is on!"
webhookurl = Webhook("WEBHOOK_HERE")
delay = int(1)

time.sleep(delay)
webhookurl.send(message)
print("Sent 1 time!")