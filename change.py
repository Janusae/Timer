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
time = [ask_hour,ask_minute,ask_second,0]
while True:
          while time[3] < 99999:
                    time[3] += 1
                    print(time)
                    if time[3] == 10000:
                              time[3] = 0
                              time[2] +=1
                    print(time)
                    if time[2] == 60:
                              time[2] = 0
                              time[1] += 1
                    if time[1] == 60:
                              time[1] = 0
                              time[0] += 1
                              
