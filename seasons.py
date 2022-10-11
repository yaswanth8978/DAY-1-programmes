day=input("enter the month and enter the date")

month=day.split()[0].lower()
date=day.split()[1]

if month in ('september','october','november'):
	print("the season is spring")
elif month in ('january', 'febraury', 'december'):
	print("the season is fall")
elif month in ('march', 'april', 'may'):
	print("the season is summer")
elif month in ('june','july','august'):
    print("the season is winter")
