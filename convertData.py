import csv
file_path = "data/seeClickFix.csv"
issue_list = []

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    my_csv_file_reader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(my_csv_file_reader)
    #['id', 'status', 'summary', 'description', 'lat', 'lng', 'address', 'created_at', 'acknowledged_at', 'closed_at', 'url']
    print(csv_header)  # print the header
    # print the index of where this column is by asking for the index from list
    print(csv_header.index('summary'))

    empty_closed_count = 0
    total_rows = 0
    status_list = []

    for row in my_csv_file_reader:
        closed_at = row[csv_header.index('closed_at')]
        status = row[csv_header.index('status')]

        #issue_list.append({"closed_at": closed_at, "status": status})
        issue = {}
        for key in csv_header:
            issue[key] = row[csv_header.index(key)]

        issue_list.append(issue)

for issue in issue_list:
    print(issue["address"])
