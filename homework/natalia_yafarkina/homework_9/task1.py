import datetime


my_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
human_date_mon = python_date.strftime('%B')
print(human_date_mon)
human_date = python_date.strftime('%d.%m.%y, %H:%M')
print(human_date)
