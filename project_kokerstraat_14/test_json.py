# open up the json file


import json




# report_json_file = "latex_report_data.json" #get json from external file
# with open(report_json_file,'r') as report_file:
#     jsonObj = json.load(report_file)

#     for obj in jsonObj:
#         print(jsonObj[obj]["begin_measuring_date"]) # get begin_measuring_date
   


from datetime import datetime,timezone
now_utc = round(datetime.now(timezone.utc).timestamp())       
print(now_utc)


week = datetime.now(timezone.utc).strftime("%V") #get current week
week = datetime.now(timezone.utc).strftime("%Y-%m-%d") #get current week
print(week)
# 1646512524 json
# 1671576604 py

print(datetime.utcfromtimestamp(now_utc))


import datetime
today = datetime.date.today()
today + datetime.timedelta(days=-today.weekday(), weeks=1)
# datetime.date(2009, 10, 26)
t = print(today - datetime.timedelta(days=today.weekday()))