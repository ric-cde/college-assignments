# Design and implement a Clock class that measures hours, minutes and seconds.
# Think about:
# •How many variables you need in order to represent a class?
# •How would you initialize an instance of a clock?
# •How can you set the time if time is given in the format “hh:mm:ss”?
# •How can you “print” a clock?

class Clock:
    def __init__(self, hrs, mins, secs):
        self.__hours = hrs
        self.__minutes = mins
        self.__seconds = secs

    def change_time(self, time_input):
        try:
            time_input = time_input.split(":")
            if (int(time_input[0]) > 24) or (int(time_input[1]) > 60) or (int(time_input[2]) > 60):
                raise Exception("Format: hr:mm:ss")
            else:
                self.__hours = time_input[0]
                self.__minutes = time_input[1]
                self.__seconds = time_input[2]
        except(Exception):
            print("Wrong format (hr:mm:ss required). Cancelling...")

    def __str__(self):
        return(f"{self.__hours} hours, {self.__minutes} minutes, {self.__seconds} seconds")


sample = Clock('15', '20', '03')
print(sample)

sample.change_time(input("What time is it? "))
print(sample)

# def get_time():
#     time_input = input("What time is it? ").split(":")
#     user_time = Clock(time_input[0], time_input[1], time_input[2])
#     if (int(time_input[0]) > 24) or (int(time_input[1]) > 60) or (int(time_input[2]) > 60):
#         raise Exception("Format: hr:mm:ss")
#     return user_time

# print(get_time())