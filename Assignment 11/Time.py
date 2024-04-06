class Time:
    #properties
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        

    #methods
    def show(self):
        self.fix()
        print("The time is:",self.hour,":",self.minute,":",self.second)

    def sum(self, other):
        new_hour = self.hour + other.hour
        new_minute = self.minute + other.minute
        new_second = self.second + other.second
        result = Time(new_hour, new_minute, new_second)
        return result
    
    def sub(self,other):
        new_hour = self.hour - other.hour
        new_minute = self.minute - other.minute
        new_second = self.second - other.second
        result = Time(new_hour, new_minute, new_second)
        return result

    def sec_to_time(self):
        self.hour = self.second // 3600
        remaining_seconds = self.second % 3600
        self.minute = remaining_seconds // 60
        self.second = remaining_seconds % 60
        result = Time(self.hour, self.minute, self.second)
        return result

    def time_to_sec(self):
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        return total_seconds
    
    def GMT_to_teheran(self):
        tehran_hour = self.hour + 3
        tehran_minute = self.minute + 30
        tehran_second = self.second 
        if tehran_minute >= 60:
            tehran_minute -= 60
            tehran_hour += 1
        if tehran_hour >= 24:
            tehran_hour -= 24
        return Time(tehran_hour, tehran_minute, tehran_second)

    def fix(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >=60:
            self.minute -=60
            self.hour += 1

        while self.second < 0:
            self.second += 60
            self.minute -= 1

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1

#function
def inputs():
    a = int(input("Give me the first hours: "))
    b = int(input("Give me the first minutes: "))
    c = int(input("Give me the first seconds: "))
    time1 = Time(a,b,c)
    a = int(input("Give me the second hours: "))
    b = int(input("Give me the second minutes: "))
    c = int(input("Give me the second seconds: "))
    time2 = Time(a,b,c)
    return time1, time2


#Main  
print("Hello there, select one of the options below: ")

while True:
    print("\n1: combine, 2: subtraction, 3: seconds to time, 4: time to seconds, 5: GMT to Teheran time, 6: exit")
    answer = input("Give me your choice: ")

    if answer == "1":
       time1, time2 = inputs()
       answer = time1.sum(time2)
       answer.show()


    elif answer == "2":
        time1, time2 = inputs()
        answer = time1.sub(time2)
        answer.show()

    elif answer == "3":
        answer = int(input("Give me a number of seconds: "))
        answer = Time(0,0,answer)
        answer.sec_to_time()
        answer.show()

    elif answer == "4":
        hour = int(input("Enter the hour: "))
        minute = int(input("Enter the minute: "))
        second = int(input("Enter the second: "))
        answer = Time(hour,minute,second)
        print("The number of your seconds is: ", answer.time_to_sec())

    elif answer == "5":
        hour = int(input("Enter the GMT hour: "))
        minute = int(input("Enter the GMT minute: "))
        second = int(input("Enter the GMT second: "))
        gmt_time = Time(hour, minute, second)
        tehran_time = gmt_time.GMT_to_teheran()
        print("The corresponding Tehran time is:")
        tehran_time.show()
        
        

    elif answer == "6":
        print("Have a good day, Bye.")
        break


    else:
        print("Wrong input.")
