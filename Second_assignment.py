today_day = int(input("Enter today's day: "))
today_month = int(input("Enter today's month: "))
today_year = int(input("Enter today's year: "))
My_birthday_day = int(input("Enter your birthday day: "))
My_birthday_month = (input("Enter your birthday month: "))
My_birthday_year = int(input("Enter your birthday year: "))

birthday_tuple = (My_birthday_day, My_birthday_month, My_birthday_year)

q = My_birthday_day
month_name_to_number = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}
My_birthday_month_num = month_name_to_number[My_birthday_month]
def is_leapyear(any_year):
    if (any_year % 4 == 0 and any_year % 100 != 0) or (any_year % 400 == 0):
        return True
    else:
        return False
    
# Strategy: count days year by year, then handle the leftover months and days

def days_in_year(year):
    return 366 if is_leapyear(year) else 365

days_in_month_normal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_month_leap   = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month_list(year):
    return days_in_month_leap if is_leapyear(year) else days_in_month_normal

def days_from_start_of_year(day, month, year):
    """How many days into the year is this date?"""
    month_days = days_in_month_list(year)
    #for the current particular year
    total = 0
    for i in range(1, month):       # add up all completed months
        total += month_days[i]
    total += day                    # add the current day
    return total

# Step 1: count all the full years between birth year and today's year
days_old = 0
for year in range(My_birthday_year, today_year):
    days_old += days_in_year(year)

# Step 2: we overcounted — we didn't start from Jan 1 of birth year,
#         we started from the actual birthday. So subtract those early days.
days_old -= days_from_start_of_year(My_birthday_day, My_birthday_month_num, My_birthday_year)

# Step 3: add the days we've lived through so far in today's year
days_old += days_from_start_of_year(today_day, today_month, today_year)
# ──────────────────────────────────────────────────────────────────────────

month_list = [("January", 13),("February", 14),
              ("March", 3),("April", 4),
              ("May", 5),("June", 6),
              ("July", 7),("August", 8),
              ("September", 9),("October", 10),
              ("November", 11),("December", 12)]
My_zeller_year = My_birthday_year
if My_birthday_month in ("January", "February"):
    My_zeller_year -=1
else:
    My_zeller_year = My_birthday_year
for i in range(len(month_list)):
      if My_birthday_month == month_list[i][0] :
            m = month_list[i][1]
#year of century
K = (My_zeller_year) % 100
#zero based century
J = (My_zeller_year// 100)

h = (q + (13*(m+1)//5)+K+ (K//4) + (J//4) +5*J) % 7

result = [
     (0, "Saturday"),(1, "Sunday"),
     (2, "Monday"), (3, "Tuesday"),
     (4, "Wednesday"), (5, "Thursday"),
     (6, "Friday")
]
print(My_birthday_year)
print(2001 % 100)
print(K)
print(h)
print(f"The day of the week of which you were born is {result[h][1]}")
print(f"You are {days_old} days old.")

upcoming_birthday = ( month_name_to_number[My_birthday_month], My_birthday_day, today_year)
till_december = 0
days_before_birthday = 0
if (today_month, today_day, today_year) < upcoming_birthday :
    if is_leapyear(today_year) is True:
        remainder = days_in_month_leap[today_month]-today_day
        for i in range(today_month+1,  month_name_to_number[My_birthday_month]):
            days_before_birthday += days_in_month_leap[i]
        days_before_birthday += remainder
        days_before_birthday += My_birthday_day
    else:
        remainder = days_in_month_normal[today_month]-today_day
        for i in range(today_month+1,  month_name_to_number[My_birthday_month]):
            days_before_birthday += days_in_month_normal[i]
        days_before_birthday += remainder
        days_before_birthday += My_birthday_day
elif (today_month, today_day, today_year) == upcoming_birthday:
    days_before_birthday = 0
else:
    if is_leapyear(today_year) is True:
        remainder = days_in_month_leap[today_month]-today_day
        if today_month == 12:
            till_december = remainder + days_from_start_of_year(My_birthday_day, My_birthday_month_num, today_year+1)
        else:
            for i in range(today_month+1, 13):
                till_december += days_in_month_leap[i]
            days_before_birthday = remainder+till_december + days_from_start_of_year(My_birthday_day,My_birthday_month_num,today_year+1)
    else:
        remainder = days_in_month_normal[today_month]-today_day
        if today_month == 12:
            till_december = remainder + days_from_start_of_year(My_birthday_day, My_birthday_month_num, today_year+1)
        else:
            for i in range(today_month+1, 13):
                till_december += days_in_month_normal[i]
            days_before_birthday = remainder+till_december + days_from_start_of_year(My_birthday_day,My_birthday_month_num,today_year+1)

print(f"The number of days before mthe birthday is: {days_before_birthday}")






