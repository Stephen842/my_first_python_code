class WeekdayError(Exception):
    pass

class Weeker:
    __names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekdayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def sub_days(self, n):
        self.__current = (self.__current - n) % 7

try:
    weekday = Weeker("Mon")
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.sub_days(23)
    print(weekday)
    weekday = Weeker("Monday")
except WeekdayError:
    print("sorry, I cant serve your request")

