

import os

def clear_screen():
    """This can be used to clear screen"""
    os.system("clear" if os.name == 'nt' else "clc")
    print("Months:\n 1- Jan, 2-Feb, 3-Mar, 4- Apr, 5-May, 6-Jun, 7-Jul, 8-Aug, 9-Sept, 10-Oct, 11-Nov, 12-Dec")

def leap_year(year: int):
    if year%4 == 0:
        if (year%100 != 0) or (year%100 == 0 and year%400 == 0):
            return True
    
    return False

year = int(input("Enter the year? "))
month = int(input("Enter the month? "))

if month <= 0 or month > 12:
    print("Please enter valid month number, between 1-12")

month_day_dic ={1: [31, "Jan"], 2:[28, "Feb"], 3: [31, "Mar"], 4:[30, "Apr"], 5: [31, "May"], 6: [30, "Jun"], 7: [31, "Jul"], 8:[31,"Aug"], 9: [30, "Sep"], 10: [31, "Oct"], 11: [30, "Nov"], 12: [31, "Dec"]}

if month != 2:
    print(f"Number of Days in Month {month_day_dic[month][1]} : {month_day_dic[month][0]}")
else:
    is_leap_year = leap_year(year)
    if not is_leap_year:
        print(f"Number of Days in Month {month_day_dic[month][1]} : {month_day_dic[month][0]}")
    else :
        print(f"Number of Days in Month {month_day_dic[month][1]} : 29")