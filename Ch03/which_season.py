import sys

print("Welcome to the which season program")

month_string = input("input the month number (e.g. January==1): ")
day_string = input("input the day of the month (e.g. 19): ")

month = int(month_string)
day = int(day_string)

if ((month == 1 or month == 2 or month == 3 or month == 12) and day > 20):
    	season = 'winter'
elif ((month == 4 or month==5 or month==6) and day > 19):
	season = 'spring'
elif ((month ==7 or month==8 or month==9) and day > 20):
	season = 'summer'
elif (month == 9 and day > 21):
    season = 'autumn'
else:
	sys.exit(-1)

print("Season is", season)