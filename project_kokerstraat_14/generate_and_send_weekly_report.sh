# generate latex files
python generate_weekly_report.py
# compile weekly report twice -> to compile overview
for x in {1..2}; do pdflatex -output-directory=reports/current_report/ reports/current_report/main.tex; done

# rename main.pdf to project_week.pdf
python rename_main.py
# python send_weekly_report.py
python send_weekly_report.py
# rename folder structure, just store it onder a different name so we dont lose it
python rename_folder.py
