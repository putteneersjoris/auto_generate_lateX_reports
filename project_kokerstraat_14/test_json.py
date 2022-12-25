import json

from datetime import datetime,timezone

# now_utc = round(datetime.now(timezone.utc).timestamp())       
# print(now_utc)


current_week = datetime.now(timezone.utc).strftime("%V") #get current week
# week = datetime.now(timezone.utc).strftime("%Y-%m-%d") #get current week
print("current_week= " + str(current_week))


begin_week = datetime.utcfromtimestamp(1670276613).strftime("%V")
print("beginweek= " + str(begin_week))
print ( "week " + str(int(current_week) - int(begin_week) ))






# get day
current_day = datetime.now(timezone.utc).strftime("%Y-%m-%d") #get current week
print("the enddate is " + str(current_day))

# import datetime


# today = datetime.date.today()
# print('today = ' +  str(today))



# # get next monday
# today + datetime.timedelta(days=-today.weekday(), weeks=1)
# # datetime.date(2009, 10, 26)
# today_week = today - datetime.timedelta(days=today.weekday())
# print('today_week = ' +  str(today_week))