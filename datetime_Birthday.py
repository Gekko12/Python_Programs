"""
Program that uses datetime module within a class, takes a birthday as input and prints
the age and the number of days, hours, minutes and seconds until the next birthday.
"""
from datetime import *


class Birthday:
    def __init__(self, birthday):
        self.birthday = birthday
        if self.b_date_validity() == -1:
            exit(0)

    @staticmethod
    def today_date():
        """This function returns today's date with time also"""
        return datetime.today()

    def age(self):
        """This function returns the age of the user if birth date is valid"""
        today = (str(self.today_date()).split()[0]).split(sep="-")
        # print(today)
        y, m, d = str(self.birthday).split(sep="-")
        # print(y, m, d)
        b_date = (str(datetime(int(y), int(m), int(d))).split()[0]).split(sep="-")
        year = int(today[0]) - int(b_date[0])
        month = int(today[1]) - int(b_date[1])
        day = int(today[2]) - int(b_date[2])
        if month < 0 or (month == 0 and day < 0):
            year = year - 1
        return year

    def next_birthday(self):
        """This function returns the number of days, hours, minutes and seconds until the next birthday"""
        today = self.today_date()
        y, m, d = self.birthday.split(sep="-")
        y = int(y) + self.age()
        # print(y, m, d)
        date_ = datetime(y, int(m), int(d))
        if today > date_:
            y += 1
        next_birthday = datetime(y, int(m), int(d))
        differ = next_birthday - today
        # print(differ)
        days, hours, minutes, seconds = 0, 0, 0, 0
        # print(len(str(differ).split()))
        if len(str(differ).split()) == 1:
            hours, minutes, seconds = str(differ).split(sep=":")
        else:
            days = str(differ).split()[0]
            hours, minutes, seconds = (str(differ).split()[2]).split(sep=":")
        return days, hours, minutes, seconds

    def b_date_validity(self):
        """This function will check for the validity of birth date ie. inputted"""
        try:
            y, m, d = str(self.birthday.split()[0]).split(sep="-")
            datetime(int(y), int(m), int(d))
            return 0
        except Exception as e:
            print("Invalid BirthDate !!!!, Error: ", e)
            return -1


def main():
    b_date = input("Enter your birth date in yyyy-mm-dd format : ")
    birth = Birthday(b_date)
    print("Today's date : ", birth.today_date())
    print("Your age is ", birth.age(), "years")
    days, hours, minutes, seconds = birth.next_birthday()
    print("Time left for your next birthday :- ", end="")
    print(days, "days, ", hours, "hours,", minutes, "minutes,", seconds, "seconds")


if __name__ == '__main__':
    main()
