import os
import csv

# Use OS to get path to csv file
path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "Election_Analysis.txt")

# Open csv file
with open(path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    poll_data = list(reader)
    
    #Define header variables
    voter_id = 0
    county = 1
    candidate = 2
    
    # Remove Header
    poll_data.pop(0)

    # Calculate total votes
    total_votes = len(poll_data)

    results = {}

    for row in poll_data:
        # If candidate exists, increment vote count
        if row[candidate] in results:
            results[row[candidate]] += 1
        # Add to candidate set
        else:
            results[row[candidate]] = 1

# Multiline String Literal
output_string =f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

max_vote = 0
winner = ''

for name in results:
    # Find percentage won for each candidate
    percent_won = round(results[name] / total_votes * 100, 2)
    
    # Append text to output_string
    output_string += f"{name}: {percent_won}% ({results[name]})\n"

    # Find winner
    if results[name] > max_vote:
        max_vote = results[name]
        winner = name

# Append text to output_string
output_string += f"""-------------------------
Winner: {winner}
-------------------------"""

# Write to file
with open(output_path,'w') as output_file:
    output_file.write(output_string)

print(output_string)