import os
import json
from latex_functions import *


report_json_file = "latex_report_data.json" #get json from external file
with open(report_json_file,'r') as report_file:
    jsonObj = json.load(report_file)

    for obj in jsonObj:
        print(jsonObj[obj]["begin_measuring_date"]) # get begin_measuring_date
   

        content =jsonObj[obj]["content"] #["data","graph","additional_files", "contact" ]
        data = jsonObj[obj]["data"]  #["temperature", "decibel", "humidity"]
        project_name = obj

        create_main("./reports/current_report/main.tex", content , obj, data)
        create_data_section("./reports/current_report/content/data.tex", data)
        create_graph_section("./reports/current_report/content/graph.tex", data)
        create_contact_section("./reports/current_report/content/contact.tex")
        create_additional_files_section("./reports/current_report/content/additional_files.tex")
