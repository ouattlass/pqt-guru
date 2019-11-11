#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
import datetime
import os
import json

my_birthday: datetime = datetime.datetime(1986, 12, 31)
today: datetime = datetime.datetime.today()

my_age_in_days = today - my_birthday
my_age_in_second = (my_age_in_days.total_seconds())

# age in days
print('My age in Days:', my_age_in_days.days, ' Days')

# age in years
my_age_in_Years = (my_age_in_second/(365 * 24 * 3600))
print('My age in Years:', my_age_in_Years, ' Years')

# age in months
my_age_in_month = (my_age_in_Years * 12)
print('My age in Months:', my_age_in_month, ' Months')

# age in hours
my_age_in_hours = my_age_in_second / 3600
print('My age in Hours:', my_age_in_hours, ' Hours')

# age in minutes
my_age_in_minute = my_age_in_second / 60
print('My age in Minutes:', my_age_in_minute, ' Minutes')


# age in Second
print('My age in Second:', my_age_in_second, ' Second')

# print *
print('Age in Stars....')
print('*' * int(my_age_in_Years), end='')

# driving licence
message = "you can drive :)" if my_age_in_Years >= 18 else "you can't drive :("
print(F'\n{message}')




