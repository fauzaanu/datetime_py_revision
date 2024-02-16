# Reading the docs for Lib/datetime.py
import datetime

if __name__ == "__main__":
    #  The rules for time adjustment across the world are more political than rational, change frequently, and there is no standard suitable for every application aside from UTC
    #  use UTC for all internal timekeeping, and only convert to local time when interacting with humans

    # CONSTANTS
    # minyear = datetime.MINYEAR
    # maxyear = datetime.MAXYEAR

    # TYPES
    # datetime.date : always aware
    # datetime.time : may be aware or naive
    # datetime.datetime : may be aware or naive
    #
    # datetime.timedelta
    #
    # datetime.tzinfo
    # datetime.timezone

    # html datetime input field would send the following:
    # 2018-06-29T08:15:00

    # time = "2018-06-29T08:15:00"
    # dt = datetime.datetime.fromisoformat(time)
    # print(dt)
    # print(type(dt))

    starttime = "2018-06-29T08:15:00"
    endtime = "2018-06-29T08:30:00"
    dt1 = datetime.datetime.fromisoformat(starttime)
    dt2 = datetime.datetime.fromisoformat(endtime)
    minutes = (dt2 - dt1).seconds / 60
    print(minutes)
