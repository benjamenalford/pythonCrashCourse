import csv
file_path = "data/seeClickFix.csv"

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

        total_rows += 1
        if (len(closed_at) == 0):
            empty_closed_count += 1

            if(status_list.count(status) < 1):
                status_list.append(status)

    print("total rows: " + str(total_rows))
    print("total empty rows: " + str(empty_closed_count) + " percent of total: " +
          str(round(empty_closed_count / total_rows, 2)))
    for s in status_list:
        print(s)
