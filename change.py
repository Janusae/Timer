import datetime
now = datetime.datetime.now()
while True:
          try:
                    ask_hour = int(input("Inter your hours: "))
                    ask_minute = int(input("Inter your minutes: "))
                    ask_second = int(input("Inter your second: "))
                    
          except ValueError:
                    print("You just can inter number")
                    ask_hour = int(input("Inter your hours: "))
                    ask_minute = int(input("Inter your minutes: "))
                    ask_second = int(input("Inter your second: "))
                    break
time = [ask_hour,ask_minute,ask_second,10000]
while True:
          while True:
                    time[3] -= 1
                    print(time)
                    if time[3] == 0:
                              time[3] = 10000
                              time[2] -=1
                    print(time)
                    if time[2] == 0:
                              time[2] = 59
                              time[1] -= 1
                    if time[1] == 0:
                              time[1] = 59
                              time[0] -= 1
                              
