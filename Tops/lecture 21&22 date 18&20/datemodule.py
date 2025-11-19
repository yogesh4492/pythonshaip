import datetime

d=datetime.datetime.now()
print(d)# full date and time with the hour minute seconds and milisecond
print(d.date())# only the date with month and year
cureent_date=d.date()

print(cureent_date.strftime("%A"))# dayname like wednesday
print(cureent_date.strftime("%a"))# day like wed in short form
print(cureent_date.strftime("%B"))# Month like full November
print(cureent_date.strftime("%b"))# month like short Nov
print(cureent_date.strftime("%c"))# print like wed nov 19 00:00:00 2025
print(cureent_date.strftime("%D"))# print like first month/date/year(short) like 11/19/25
print(cureent_date.strftime("%d"))# print like date like current date is 19
print(cureent_date.strftime("%e"))# print same as above
print(cureent_date.strftime("%F"))#print dte in year-month-date(format)
print(cureent_date.strftime("%g"))#year in short like 25,26
print(cureent_date.strftime("%G"))#Year in full like 2025-2026
print(cureent_date.strftime("%h"))# month in capital word
print(cureent_date.strftime("%m"))# month in number
print(cureent_date.strftime("%x"))#print as same as %D
print(cureent_date.strftime("%y"))#year in short two digit like 25
print(cureent_date.strftime("%Y"))# year in 4 digit like 2025
