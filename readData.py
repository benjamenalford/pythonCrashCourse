import csv
file_path = "data/seeClickFix.csv"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    my_csv_file_reader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(my_csv_file_reader)
    print(csv_header)
    for row in my_csv_file_reader:
        print(row)
