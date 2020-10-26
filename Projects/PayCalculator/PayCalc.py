pay = float(input('Enter hourly pay e.g: 10.10€ '))

time = input('Enter time worked in the format HH:MM:SS.MS ')
hours,minutes,seconds=time.split(':')
seconds,milliseconds = seconds.split('.')

hours = float(hours)
minutes = float(minutes)
seconds = float(seconds)
milliseconds = float(milliseconds)

milliseconds_to_seconds = milliseconds/100
seconds_to_mins = (seconds+milliseconds_to_seconds)/60
min_to_hours = (minutes+seconds_to_mins)/60
totalhours = hours + min_to_hours
totalpay = totalhours * pay

#print('Hours:',hours,' Minutes: ',minutes,' Seconds:',seconds,' Milli-Seconds:',milliseconds)
#print('Milliseconds to seconds:',milliseconds_to_seconds,'\nSeconds to mins:',seconds_to_mins,'\nMins to Hours :',min_to_hours,'\nTotal hours :',totalhours)
print('Your pay is ',round(totalpay,2),'€')
input("") # inorder to wait and display the the result