from datetime import datetime, timedelta

class Item:
    def __init__(self, description, duration = timedelta(minutes=0), start = None, end = None, bucket = "default"):
        self.description = description
        self.completed = False
        self.start = start
        self.end = end
        self.bucket = bucket

        if duration.seconds > 0:
            # Assume being added to queue because minute duration is provided
            # [?] Need to check for edge case of adding with 0 minutes deliberately?
            # [!] Will need later validation & test for no 0 duration when adding task from UI
            self.duration = duration
            self.scheduled = False
        else:
            # Assume being added to schedule (no edge case from above); calculate duration from start/end
            # [!] Validate & test start/end are provided if duration is 0
            self.duration = end - start
            self.scheduled = True

    def schedule(self, start):
        # [!] Need check on if scheduled ALREADY is true and throw exception
        self.scheduled = True
        self.start = start
        # [!] Need check on if duration is 0 and throw exception
        self.end = start + self.duration

print("--- Daily Schedule Planner ---")

# Initial test runs
test = Item("Test schedule item", timedelta(minutes=30))
test.schedule(datetime(2019,10,3,6,0))
print(test.end.time())

