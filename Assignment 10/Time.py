import datetime

class Time:
    def __init__(self, hour, minute, second):
        #properties
        self.hour = hour
        self.minute = minute
        self.second = second
    #methods
    def time(self):
        return f"{self.hour}:{self.minute}:{self.second}"
    
    def chronometer(self):
        ...

    def time_zone(self):
        ...


time = datetime.datetime.now()
formatted_time = time.strftime("%H:%M:%S")
hour, minute, second = formatted_time.split(":")

clock = Time(hour, minute, second)
print("The exact time is:",clock.time())
