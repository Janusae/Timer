import datetime
now = datetime.datetime.now()
while True:
                    
          ask_hour , ask_minute , ask_second = input("set your timer like (hour:minute:second): ").split(":")
          try:
                    time = [int(ask_hour),int(ask_minute),int(ask_second),10000]
          except ValueError:
                    print("You just can inter number!")
                    ask_hour , ask_minute , ask_second = input("set your timer like (hour:minute:second): ").split(":")
          else:
                    break
while True:
          while True:
                    time[3] -= 1
                    
                    if time[3] == 0 and time[2] != 0:
                              time[3] = 10000
                              time[2] -= 1 
                    elif time[2] == 0 and time[1] == 0 and time[0] == 0:
                              break
                    elif time[2] == 0 and time[1] != 0:
                              time[2] = 59
                              time[1] -= 1
                    elif time[2] == 0 and time[1] == 0:
                              time[2] = 59
                              time[1] = 59
                              time[0] -= 1
                    print(F"{time[0]}:{time[1]}:{time[2]}")
          break
import winsound
file_name = "telephone-ring-02.wav"
winsound.PlaySound(file_name , winsound.SND_FILENAME)

