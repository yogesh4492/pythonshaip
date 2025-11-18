import datetime

d=datetime.datetime.now()
print(d)
print(d.date())
cureent_date=d.date()

print(cureent_date.strftime("%A"))
print(cureent_date.strftime("%a"))
print(cureent_date.strftime("%B"))
print(cureent_date.strftime("%b"))