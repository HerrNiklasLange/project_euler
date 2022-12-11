def week_day(day, n): #updates the day of the week
    x = 0
    if day + n > 6:
        x = day + n - 7
    else:
        x = day + n
    return int(x)

def sunday(day, n):
    is_sunday = False
    if day[n] == "sun":
        is_sunday = True
    return is_sunday
def march(weekday, n):
    sun_count = 0
    day = week_day(weekday, n)
    if sunday(weekday, day):
        sun_count += 1
    return int(sun_count)

def mai_jul_oct_dec(weekday):
    sun_count = 0
    day = week_day(weekday, 2)
    if sunday(weekday, day):
        sun_count += 1
    return int(sun_count)

def rest(weekday):
    sun_count = 0
    day = week_day(weekday, 3)
    if sunday(weekday, day):
        sun_count += 1
    return int(sun_count)


sun_count = 0
current_day = 5
weekday = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
month = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")

x = 0
for index in range(1901, 2001):
    extra_day = 0
    if index % 4 == 0:
        extra_day += 1
    for index1 in range(0,12):
        if month[index1] == month[4] or month[index1] == month[6] or month[index1] == month[9] or month[index1] == month[11]:
            current_day = week_day(current_day, 2)
            print(weekday[current_day])
            if sunday(weekday, current_day):
                sun_count += 1
        elif month[index1] == month[2]:
            current_day = week_day(current_day, extra_day)
            print(weekday[current_day])
            if sunday(weekday, current_day):
                sun_count += 1
        else:
            current_day = week_day(current_day, 3)
            print(weekday[current_day])
            if sunday(weekday, current_day):
                sun_count += 1

print(sun_count)
# 1 january 1901 tue  1 
# 1 feb 1901 fri    4
# 1 mar 1901 fri    4 !!!! +1 every 4
# 1 apr 1901 mon    0
# 1 mai 1901 wed    2
# 1 jun 1901 sat    5
# 1 jul 1901 mon    0
# 1 aug 1901 thu    3
# 1 sep 1901 sun    6
# 1 oct 1901 tue    1
# 1 nov 1901 fri    4
# 1 dec 1901 sun    6

#+2  mai, jul, oct, dec
#0/1 mar
#rest + 3