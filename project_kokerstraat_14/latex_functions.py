def create_main(filename, sections, project_name, sensordata):
    with open(filename, "w", encoding="utf8") as f:
        
        f.write("\\documentclass{article} \n")
        f.write("\\usepackage{graphicx} \n")
        f.write("\\usepackage[utf8]{inputenc}  \n")
        f.write("\\usepackage[rightcaption]{sidecap}  \n")
        f.write("\\usepackage{hyperref} \n")
        f.write("\\usepackage{subcaption} \n")
        f.write("\\usepackage[verbose]{placeins} \n")
        f.write("\\usepackage{subfiles} % Best loaded last in the preamble \n")
        f.write("\\hypersetup{colorlinks=true, linkcolor=black, filecolor=blue, urlcolor=blue, pdfpagemode=FullScreen } \n")
        f.write("\\urlstyle{same} \n")
        f.write("\\author{territory data | Joris Putteneers} \n")

        # make the procedurtal title
        title = "\\title{"
        title += f"{project_name}" 
        title += "\\\\ \\large weekly progress report: visualisation of {" 

        for i in range(0, len(sensordata)-1):
            if i is not len(sensordata)-2:
                title +=sensordata[i] + ', '
            else:
                title +=sensordata[i]

        title += "} and "
        title += sensordata[-1]
        title += "} \n"
        
        f.write(title)
        f.write("\\date{5th of December 2022 - 12th of December 2022}  \n")

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

