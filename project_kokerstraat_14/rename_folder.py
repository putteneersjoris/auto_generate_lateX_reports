import os
import shutil
import random


homedir = os.getcwd()

old_folder_name = "\\current_report\\"
new_folder_name = "\\test"

dir_to_change = homedir + "\\reports" 

shutil.copytree(dir_to_change + old_folder_name, dir_to_change + "\\week" + str(random.randint(1,10)))
# delete files in current_rport

# for content_file in os.listdir(dir_to_change + old_folder_name + "content"):
#     os.remove(dir_to_change + old_folder_name + "content\\" + content_file)



# for file in os.listdir(dir_to_change + old_folder_name):
#     if file.isfile() == True:
#         os.remove(file)