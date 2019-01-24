import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv')


months =0
month_of_change = []
net_change = []
greatest_increase =['',0]
greatest_decrease =['',90000000]
total_net =0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    first_row = next(csvreader)
    months = months+1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        months = months+1
        total_net = total_net + int(row[1])
        net_change = int(row[1]) - previous_net 
    print(months) 
    print(total_net) 
    print(first_row) 
