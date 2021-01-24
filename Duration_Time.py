"""
Program to find duration of event if start and end time is given by defining class Time
"""


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%.2d : %.2d : %.2d" % (self.hour, self.minute, self.second)

    def duration(self, other):
        """self is start time and other is end time"""
        s1 = time_to_int(self)
        s2 = time_to_int(other)
        differ = s2 - s1
        return int_to_time(differ)


def time_to_int(t):
    """ t is a Time (class) object"""
    seconds = (t.hour * 3600) + (t.minute * 60) + t.second
    return seconds


def div_mod(a, b):
    return a // b, a % b


def int_to_time(seconds):
    minute, time_second = div_mod(seconds, 60)
    time_hour, time_minute = div_mod(minute, 60)
    return Time(time_hour, time_minute, time_second)


start = Time(10, 30, 5)
end = Time(11, 45, 5)
print("Start : ", start)
print("End : ", end)
print("Duration : ", start.duration(end))
