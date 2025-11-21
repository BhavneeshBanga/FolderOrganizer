import json
import os
from datetime import datetime
nows = datetime.now().isoformat()

filename = "Daily_expenses_tracker.json"

if os.path.exists(filename):
    with open(filename, "r") as f:
        trackerr = json.load(f)
else:
    trackerr = []

amount = int(input("amount 💵 : "))
about = input("about 🤔 : ")


new_tracker = {"amount ":  amount, "about ": about , "Date":nows}

trackerr.append(new_tracker)
#dump the data
with open(filename, "w") as file:
    data = json.dump(trackerr, file, indent=4)
#display
for i, contact in enumerate(trackerr, start=1):
    print(f"{i}: {contact}")