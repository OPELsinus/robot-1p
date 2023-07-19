import datetime

# Get the current date
current_date = datetime.date.today()

# Calculate the previous quarter's start and end dates
if current_date.month <= 3:
    previous_quarter_start = datetime.date(current_date.year - 1, 10, 1)
    previous_quarter_end = datetime.date(current_date.year - 1, 12, 31)
else:
    previous_quarter_start = datetime.date(current_date.year, (current_date.month - 3), 1)
    previous_quarter_end = datetime.date(current_date.year, (current_date.month - 1), 1) - datetime.timedelta(days=1)

print("Previous Quarter's Start Date:", previous_quarter_start)
print("Previous Quarter's End Date:", previous_quarter_end)
