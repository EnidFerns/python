import time
import webbrowser
import sys
url = 'https://www.youtube.com/watch?v=sHbvLOtwaOs'

alarm_time = input('alarm: ')
current_time = time.strftime('%I:%M:%S')
while(current_time != alarm_time):    #repeatedly check for current time and the alarm time
    print('Current time is: ' + current_time)
    current_time = time.strftime('%I:%M:%S')
    time.sleep(1)       #wait for one second
    if current_time == alarm_time:    #when the time matches, open the browser
        print('Opening the ' + url + ' now...')
        webbrowser.open(url)
   