totalHours = float(0)
totalMinutes = float(0)
totalSeconds = float(0)
totalMilliSeconds = float(0)

while True:
    time = input('Enter time worked in the format HH:MM:SS.MS or type Done if thats all the values ')
    if time != 'Done':
        hours, minutes, seconds = time.split(':')
        seconds, milliseconds = seconds.split('.')

        hours = float(hours)
        minutes = float(minutes)
        seconds = float(seconds)
        milliseconds = float(milliseconds)

        totalHours += hours
        totalMinutes += minutes
        totalSeconds += seconds
        totalMilliSeconds += milliseconds

    elif time == 'Done':
        print('Thanks for entering the values!')
        break
    else:
        print('please enter something meaningful')

milliseconds_to_seconds = totalMilliSeconds/100 #seconds with remaining milliseconds as decimals
totalSeconds += milliseconds_to_seconds

seconds_to_mins = (totalSeconds)//60 #
remainingSeconds = totalSeconds % 60
totalMinutes += seconds_to_mins
min_to_hours = (totalMinutes)//60
remainingMinutes = totalMinutes % 60
totalHours += min_to_hours

print('Total time is ',totalHours,':',remainingMinutes,':',round(remainingSeconds,2))
input("") # to display the output and wait for the user instead of rapid quitting