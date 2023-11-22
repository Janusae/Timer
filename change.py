import datetime
time = [8,58,50,0]
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
                              
