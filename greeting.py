print("********************Greeting according to Time***********************")
print("\n")
import time
print("Enter the time:")
timestamp=time.strftime('%H:%M:%S')
hours=int (time.strftime('%H'))
print(timestamp)
if(time.strftime('%H')<=20 & time.strftime('%H')>=23):
    print