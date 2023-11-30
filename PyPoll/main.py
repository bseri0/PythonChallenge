import os
import csv

# Relative path to the input CSV file
path1 = os.path.join(os.getcwd(), 'module_3')
input_csv_file = os.path.join(path1, 'PyPoll', 'resources', 'election_data.csv')

# Relative path to the output CSV file
csv_file_path = os.path.join(path1, 'PyPoll', 'analysis', 'election_results.csv')

# Read CSV file
with open(input_csv_file, "r") as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip the header row
    header = next(reader)

    # Create a dictionary to store the number of votes for each candidate
    votes = {}
    for row in reader:
        candidate = row[2]
        if candidate not in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1

# Calculate total votes
total_votes = sum(votes.values())

# Determine the winner based on popular vote
winner = max(votes, key=votes.get)

# Write election results to CSV file
with open(csv_file_path, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["-------------------------"])

    # Iterate over the candidate names and print the candidate name, votes percentage, and votes count
    for candidate, vote_count in votes.items():
        votes_percentage = (vote_count / total_votes) * 100
        writer.writerow([f"{candidate}: {votes_percentage:.2f}% ({vote_count})"])

    # Include the winner based on popular vote in the CSV file
    writer.writerow(["-------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-------------------------"])

print("Election results printed to CSV file.")