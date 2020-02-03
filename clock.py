#example clock program
#https://www.youtube.com/watch?v=bm8bgb_3OX8
#import time for time.sleep(x) function
import time

#implement graphics clock
from turtle import *
setup()
t1 = Turtle()

hours = 3
minutes = 2
seconds = 45

#now build loop
while True:
    #zfill to show 2 digits no matter what
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), font=("arial",25,"normal"))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours = 1