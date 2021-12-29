"""

Python has a module named datetime to work with dates and times.

"""


# Example 1: Get Current Date and Time
import datetime
datetime_obj = datetime.datetime.now()
print(datetime_obj)

"""
Here, we have imported datetime module using import datetime statement.

One of the classes defined in the datetime module is datetime class. We then used now() method to create a 
datetime object containing the current local date and time.
"""


# Example 2: Get Current Date
# In this program, we have used today() method defined in the date class to get a date object containing the
# current local date.
import datetime
date_obje = datetime.date.today()
print(date_obje)

# We can use dir() function to get a list containing all attributes of a module.

import datetime
print(dir(datetime))



"""
Commonly used classes in the datetime module are:

---date Class
---time Class
---datetime Class
---timedelta Class

"""



# datetime.date Class
# You can instantiate date objects from the date class. A date object represents a date (year, month & day).

# Example 3: Date object to represent a date

import datetime
dt = datetime.date(2021, 12, 21)
print(dt)


"""
If you are wondering, date() in the above example is a constructor of the date class. 
The constructor takes three arguments: year, month and day.

The variable a is a date object.
"""


# We can only import date class from the datetime module

from datetime import date
a = date(2021, 12, 21)
print(a)


# Example 4: Get current date
# You can create a date object containing the current date by using a classmethod named today().

from datetime import date
today = date.today()
print('Current date =', today)


# Example 5: Get date from a timestamp
# We can also create date objects from a timestamp. A Unix timestamp is the number of seconds between a particular
# date and January 1, 1970 at UTC. You can convert a timestamp to date using fromtimestamp() method.


from datetime import date
timestamp = date.fromtimestamp(3)
print("Date =", timestamp)


# Example 6: Print today's year, month and day
# We can get year, month, day, day of the week etc. from the date object easily.


from datetime import date

# date object of today's date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)



# datetime.time
# A time object instantiated from the time class represents the local time.

# Example 7: Time object to represent time

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print('a =', a)

# time(hour, minute and second)
b = time(11, 34, 56)
print('b =', b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print('c =', c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print('d =', d)




import calendar
for i in calendar.day_name:
        print(i)