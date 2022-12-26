# rename main.pdf to kokerstraat_14_week3.pdf

import os
import json
from datetime import datetime
filename = "main.pdf"

homedir = os.getcwd()

report_json_file = "latex_report_data.json" #get json from external file
new_filename = ''
with open(report_json_file,'r') as report_file:
    jsonObj = json.load(report_file)
    for obj in jsonObj:
        new_filename=obj.replace(" ","_")

        begindate = jsonObj[obj]["begin_measuring_date"]
        enddate = jsonObj[obj]["end_measuring_date"]
        date_now_week = datetime.now().strftime("%V")
        date_begin_week = datetime.utcfromtimestamp(begindate).strftime("%V")
        date_end_week = datetime.utcfromtimestamp(enddate).strftime("%V")
        currentweek = "_week" + str(int(date_now_week) - int(date_begin_week))

print("folder has been renamed")
os.chdir(os.getcwd() + "\\reports\\current_report\\")
os.rename(filename, new_filename + currentweek +".pdf")


os.chdir(homedir)



