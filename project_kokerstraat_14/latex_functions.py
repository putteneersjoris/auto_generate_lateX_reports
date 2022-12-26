from datetime import datetime,timezone, timedelta




def create_main(filename, sections, project_name, sensordata, begindate, enddate):
    with open(filename, "w", encoding="utf8") as f:
        
        f.write("\\documentclass{article} \n")
        f.write("\\usepackage{graphicx} \n")
        f.write("\\usepackage[utf8]{inputenc}  \n")
        f.write("\\usepackage[rightcaption]{sidecap}  \n")
        f.write("\\usepackage{hyperref} \n")
        f.write("\\usepackage{subcaption} \n")
        f.write("\\usepackage[verbose]{placeins} \n")
        f.write("\\usepackage{subfiles} % Best loaded last in the preamble \n")
        f.write("\\hypersetup{colorlinks=true, linkcolor=black, filecolor=blue, urlcolor=blue} \n")
        f.write("\\urlstyle{same} \n")
        f.write("\\author{territory data | Joris Putteneers} \n")

        # make the procedurtal title
 
        # make the content for the title dependatnt on the amount so that its grammar is correct
        title_content =''
        if len(sensordata) == 1:
            title_content += sensordata[0]

        if len(sensordata) == 2:
            title_content += sensordata[0] + " and " +  sensordata[1]

        if len(sensordata) >= 3:
            title_content += sensordata[0]
            for i in range(1,len(sensordata)-1):
                title_content += ", " + sensordata[i] 
            title_content +=" and " + sensordata[-1]
        

        title = "\\title{"
        title += f"{project_name}" 
        title += '\\\\ \\large ' + 'weekly progress report: visualisation of ' + f"{title_content}"
        title += "}"
        f.write(title )

        # f.write(title)

        # calculate the date, and the current week
        date_now_week = datetime.now().strftime("%V")
        date_begin_week = datetime.utcfromtimestamp(begindate).strftime("%V")
        date_end_week = datetime.utcfromtimestamp(enddate).strftime("%V")
        currentweek = int(date_now_week) - int(date_begin_week)

        
        # calc the total amount of weeks that the project runs
        a = datetime.utcfromtimestamp(begindate)
        b = datetime.utcfromtimestamp(enddate)
        delta = b - a
        totalweek = round(delta.days/7) 
        
        # get current day
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        def get_day_extension(day):
            extension= ''
            day_extensions = {"1":"st ", "2":"nd ", "3":"rd "}
            if day[0] == "0":
                day = day.replace('0','') #values are 01, 04,22 etc.. we remove the first 0
  
            if day in day_extensions:
                extension = day_extensions[day] #set the right extension 1st, 2nd, 3th etc
            else:
                extension = 'th '

            return day + extension

        today_day = datetime.now(timezone.utc).strftime("%d") 
        today_month = datetime.now(timezone.utc).strftime("%m") 
        today_year = datetime.now(timezone.utc).strftime("%Y")
        today = get_day_extension(today_day) + "of " + months[int(today_month)-1] + " " + today_year

        previous_date_utc = datetime.now(timezone.utc) - timedelta(days=7)
        previous_date_day = previous_date_utc.strftime("%d") 
        previous_date_month = previous_date_utc.strftime("%m") 
        previous_date_year = previous_date_utc.strftime("%Y") 
        previous_date =  get_day_extension(previous_date_day) + "of " + months[int(previous_date_month)-1] + " " + previous_date_year

        begin_measuring_date = datetime.utcfromtimestamp(begindate).strftime("%d-%m-%Y")
        end_measuring_date = datetime.utcfromtimestamp(enddate).strftime("%d-%m-%Y")

        date = "\\date{" 
        date += "project start date "+ f"{begin_measuring_date} " + "\\\\"
        date += f"weekly report: {currentweek} /  "
        date += f" {totalweek} "
        date += "\\\\"
        date += f" {previous_date} - {today} " + "\\\\"
        date += "project end date "+ f"{end_measuring_date} " 
        date += "}\n"
        f.write(date)

        f.write("\\begin{document}  \n")
        f.write("\\maketitle  \n")
        f.write("\\tableofcontents \n")
        f.write("\\newpage \n")

        # content of the main.tex file

        for section in sections:
                if section == "data":
                    f.write("\\section{data} \n")
                    f.write("\\subfile{reports/current_report/content/data} \n")

                if section == "graph":
                    f.write("\\section{graph} \n")
                    f.write("\\subfile{reports/current_report/content/graph} \n")

                if section == "additional_files":
                    f.write("\\section{additional files} \n")
                    f.write("\\subfile{reports/current_report/content/additional_files} \n")

                if section == "contact":
                    f.write("\\section{contact} \n")
                    f.write("\\subfile{reports/current_report/content/contact} \n")


        f.write("\\end{document} \n")

        print('main.tex file created succesfully')

        f.close()

def create_data_section(filename, sensordata):
    with open(filename, "w", encoding="utf8") as f:
        for data in sensordata:

            f.write(f"\\subsection{{{data}}} \n")
            temperature = f"the {data} was measured every 2 minutes over the course of 1 week. "
            minimum_temperature = f"the minimal {data} was reached on monday 8-12-2022 with a degree of 11°C on sensor 12 "
            maximum_temperature = f"the maximum {data} was reached on wednseday 11-12-2022 with a degree of 21°C on sensor 5."
            f.write(temperature  + minimum_temperature  + maximum_temperature )
            f.write("\\\\ \n")
            f.write("\\begin{figure}[hbt!] \n")
            f.write("\\begin{subfigure}{0.5\\textwidth} \n")
            f.write("\\includegraphics[width=0.99\linewidth]{reports/current_report/images/max_" + f"{data}.png" + "}  \n")
            f.write("\\caption{max " + f"{data}" + "}  \n")
            f.write("\\end{subfigure} \n")
            f.write("\\begin{subfigure}{0.5\\textwidth} \n")
            f.write("\\includegraphics[width=0.99\linewidth]{reports/current_report/images/min_" + f"{data}.png" + "}  \n")
            f.write("\\caption{min " + f"{data}" + "}  \n")
            f.write("\\end{subfigure} \n")
            f.write("\\caption{comparison between the minimum and maximum  " + f"{data}" + "}  \n")
            f.write("\\end{figure} \n")
            f.write("\\FloatBarrier \n")
            data_average = f"the average {data} during week 1 (5th of December until the 12th of December) was 17 °C. \\\\"
            data_overview = f"an overview of the {data}images can be seen here:"
            
            f.write(data_average + data_overview)
            f.write("\\begin{figure}[hbt!] \n")
            f.write("\\centering \n")
            f.write("\\includegraphics[width=\\textwidth]{reports/current_report/images/montage_"+ f"{data}.jpg" + "}  \n")
            f.write("\\caption{mosaic of the "+ f"{data}" + " measuruments} \n")
            f.write("\\end{figure} \n")
            f.write("\\FloatBarrier \n")

        print('data.tex file created succesfully')
        extra = "a live visualisation of the data can be seen \href{https://data.hasdata.xyz/}{here}. an animation of the week's data can be seen \href{https://data.hasdata.xyz/}{here}. "
        f.write(extra)
        
        f.close()

def create_graph_section(filename, sensordata):
    with open(filename, "w", encoding="utf8") as f:
        for data in sensordata:
            f.write(f"\\subsection{{{data}}} \n")
            f.write("\\begin{figure}[hbt!] \n")
            f.write("\\begin{subfigure}{0.3\\textwidth} \n")
            f.write("\\includegraphics[width=0.9\linewidth]{reports/current_report/images/max_graph_"+ f"{data}.png" + "}  \n")
            f.write("\\caption{max "+f"{data}" + "}  \n")
            f.write("\\end{subfigure} \n")
            f.write("\\begin{subfigure}{0.3\\textwidth} \n")
            f.write("\\includegraphics[width=0.9\linewidth]{reports/current_report/images/min_graph_"+ f"{data}.png" + "}  \n")
            f.write("\\caption{min "+f"{data}" + "}  \n")
            f.write("\\end{subfigure} \n")
            f.write("\\begin{subfigure}{0.3\\textwidth} \n")
            f.write("\\includegraphics[width=0.9\linewidth]{reports/current_report/images/average_graph_"+ f"{data}.png" + "}  \n")
            f.write("\\caption{max "+f"{data}" + "}  \n")
            f.write("\\end{subfigure} \n")
            f.write("\\caption{comparison between the minimum and maximum "+f"{data}" + "}  \n")
            f.write("\\end{figure} \n")
            f.write("\\FloatBarrier  \n")
            average_temp = f"the average {data} during week 1 (5th of December until the 12th of December) was 17 °C."
            average_overview = f"an overview of the {data} images can be seen here:"
            f.write(average_temp + average_overview)
            f.write("\\begin{SCfigure}[0.5][hbt!]\n")
            f.write("\\includegraphics[width=0.6\\textwidth]{reports/current_report/images/combined_graph_"+ f"{data}.png" + "}  \n")
            f.write("\\caption{vectorfield "+f"{data}" + "}  \n")
            f.write("\\end{SCfigure} \n")
            f.write("\\FloatBarrier  \n")

        f.close()


def create_additional_files_section(filename):
    with open(filename, "w", encoding="utf8") as f:
        f.write("\\subsection{3d models} \n")
        threeD_models = "3d models can be downloaded \href{https://data.hasdata.xyz/}{here}.Pointcloud models can be downloaded \href{https://data.hasdata.xyz/}{here}."
        f.write(threeD_models)

        print('additional_files.tex file created succesfully')
        f.close()

def create_contact_section(filename):
    with open(filename, "w", encoding="utf8") as f:
        contact = "for any questions or inquiries, please contact Joris Putteneers on ++032497371892 or joris@territorydata.xyz"
        f.write(contact)
        print('contact.tex file created succesfully')

        f.close()

