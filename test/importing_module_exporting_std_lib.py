import calendar
import datetime


today = datetime.date.today()
print(today)

c = calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.isleap(2020))

print(c)

from my_module import find_index , test


courses= ['EEE','CSE','MATH']

index = find_index(courses, 'MATH')
print(index)