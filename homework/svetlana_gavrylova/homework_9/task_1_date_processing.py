import datetime

given_date = "Jan 15, 2023 - 12:05:33"
date_format = "%b %d, %Y - %H:%M:%S"
date = datetime.datetime.strptime(given_date, date_format)
print(f'The {given_date} date in Python format: {date}')
print(f'The month from this date: {date.strftime("%B")}')

new_format = "%d.%m.%Y, %H:%M"
print(f'The date in the new format: {date.strftime(new_format)}')
