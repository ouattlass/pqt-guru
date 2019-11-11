#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
import time
import webbrowser

new_site = "http://bbc.com"
interval = 10 * 60  # interval (minxsec) between page refreshes
breaks_wanted = 3  # how many times the page should be reloaded


# dot not modify anything under this line
breaks_taken = 0
print(F"Newsbreak  V1.0 started at {time.ctime()})")
print(F"Interval is : {interval} s")
while breaks_taken < breaks_wanted:
    time.sleep(interval)
    webbrowser.open("http://bbc.com")
    breaks_taken += 1



