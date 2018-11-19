from datetime import date
import re
import time 

d0 = date(2018, 9, 21)
dx = date.today()
diff = str(dx - d0).split()[0]
tillGoal = 90 - int(diff)
print("started date: ", d0)
print("today's date: ", dx)
print("Days so far: ", diff)
print("\nOnly ", tillGoal ," days left! Keep going!")

time.sleep(5)