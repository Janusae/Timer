
def set_clock():
    from datetime import time
    hour , minute , second = input("Inter your time like(hour:minute:second): ").split(":")
    global time_one
    time_one = time(int(hour),int(minute),int(second))
    print(time)
set_clock()
def move_clock(time):
    import datetime
    test = datetime.datetime.now()
    print(test)
    clock_one =time(test.hour , test.minute , test.second)
    print(clock_one)
move_clock(time_one)