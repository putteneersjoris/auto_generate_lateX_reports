import os
from latex_functions import *

content = ["data","graph","additional_files", "contact" ]
data =  ["temperature", "decibel", "humidity"]

create_main("./reports/current_report/main.tex", content , "Kokerstraat 14", data)
create_data_section("./reports/current_report/content/data.tex", data)
create_graph_section("./reports/current_report/content/graph.tex", data)
create_contact_section("./reports/current_report/content/contact.tex")
create_additional_files_section("./reports/current_report/content/additional_files.tex")
