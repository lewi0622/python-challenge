import os
import csv

# Use OS to get path to csv file
path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "Financial_Analysis.txt")

# Open csv file
with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    budget_data = list(reader)
    
    # Get number of months
    months = len(budget_data)

    total = 0
    min_val = {}
    max_val = {}

    for index, row in enumerate(budget_data):
        # Sum profit/loss total
        total += int(row['Profit/Losses'])

        # Capture initial values
        if index == 0:           
            min_val['value'] = max_val['value'] = int(row['Profit/Losses'])
        else:
            if int(row['Profit/Losses']) < min_val['value']:
                min_val['value'] = int(row['Profit/Losses'])
                min_val['month'] = row['Date']
            if int(row['Profit/Losses']) > max_val['value']:
                max_val['value'] = int(row['Profit/Losses'])
                max_val['month'] = row['Date']

    # Average change 
    average = round(total/months,2)

# Multiline String Literal
output_string =f"""Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${average}
Greatest Increase in Profits: {max_val['month']} (${max_val['value']})
Greatest Decrease in Profits: {min_val['month']} (${min_val['value']})
"""
# Terminal output
print(output_string)

# Write to file
with open(output_path,'w') as output_file:
    output_file.write(output_string)
