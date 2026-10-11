import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
if(hour>0 and hour<=9):
  print("Good Morning")
elif(hour>=10 and hour<=18):
  print("Good AfterNoon")
if(hour>=19 and hour<=24):
  print("Good Night")
  
