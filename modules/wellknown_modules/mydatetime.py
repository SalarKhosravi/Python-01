
# Importing the datetime module
import datetime

# Get the current date and time
print('---------------------------------------------------')
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)


# Extracting specific parts of the date and time
print('---------------------------------------------------')
year = current_datetime.year  # Get the current year
month = current_datetime.month  # Get the current month
day = current_datetime.day  # Get the current day
hour = current_datetime.hour  # Get the current hour
minute = current_datetime.minute  # Get the current minute
second = current_datetime.second  # Get the current second
print("Year:", year, "Month:", month, "Day:", day)
print("Hour:", hour, "Minute:", minute, "Second:", second)

# Working with dates - creating a specific date
print('---------------------------------------------------')
specific_date = datetime.date(2023, 5, 17)
print("Specific date:", specific_date)



# Formatting dates
print('---------------------------------------------------')
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date 1:", formatted_date)

formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M")
print("Formatted date 2:", formatted_date)

formatted_date = current_datetime.strftime("%Y-%m-%d %H")
print("Formatted date 3:", formatted_date)



# Date arithmetic - adding and subtracting days
print('---------------------------------------------------')
tomorrow = current_datetime + datetime.timedelta(days=1)  # Adds 1 day
yesterday = current_datetime - datetime.timedelta(days=1)  # Subtracts 1 day
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)



# Calculating the difference between dates
print('---------------------------------------------------')
date1 = datetime.date(2023, 11, 1)
date2 = datetime.date(2024, 11, 15)
difference = date2 - date1
print("Difference between dates:", difference.days, "days")



# Parsing a date string into a datetime object
print('---------------------------------------------------')
date_string = "2023-11-03 15:45:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
formatted_date = parsed_date.strftime("%Y-%m-%d %H")

print("formatted date:", formatted_date)
print("Parsed date:", parsed_date)



# Useful constants
print('---------------------------------------------------')
print("Minimum date:", datetime.datetime.min)  # Earliest representable date
print("Maximum date:", datetime.datetime.max)  # Latest representable date
print("Today's date:", datetime.date.today())  # Today's date without time



