# generate latex files
python generate_weekly_report.py
# compile weekly report twice -> to compile overview
for x in {1..2}; do pdflatex -output-directory=reports/current_report/ reports/current_report/main.tex; done

# python send_weekly_report.py
#rename folder structure