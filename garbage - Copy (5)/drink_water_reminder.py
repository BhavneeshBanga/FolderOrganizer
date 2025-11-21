import time
from plyer import notification

for i in range(10):
    notification.notify(title="REMINDER",message="Drink Water Reminder",timeout=10)
    time.sleep(18)

    