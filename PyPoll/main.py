import os
import csv

ELECTION_CSV = os.path.join("Resources", "election_data.csv")
RESULTS_CSV = os.path.join("Analysis", "results.csv")

CANDIDATE_LIST = []
VOTES = 0
CHARLIE = 0
DIANA = 0
RAYMON = 0


def calculate_percentages(votes, charlie, diana, raymon):
    """Calculates the percentage of votes for each candidate.

    Args:
        votes: The total number of votes.
        charlie: The number of votes for Charles Casper Stockham.
        diana: The number of votes for Diana DeGette.
        raymon: The number of votes for Raymon Anthony Doane.

    Returns:
        A dictionary of candidate percentages.
    """

    percentages = {}
    percentages["Charles Casper Stockham"] = round((charlie / votes) * 100, 3)
    percentages["Diana DeGette"] = round((diana / votes) * 100, 3)
    percentages["Raymon Anthony Doane"] = round((raymon / votes) * 100, 3)
    return percentages


def determine_winner(percentages):
    """Determines the winner of the election.

    Args:
        percentages: A dictionary of candidate percentages.

    Returns:
        The name of the winning candidate.
    """

    winner = max(percentages, key=percentages.get)
    return winner


def print_results(votes, percentages, winner):
    """Prints the election results to the console and a CSV file.

    Args:
        votes: The total number of votes.
        percentages: A dictionary of candidate percentages.
        winner: The name of the winning candidate.
    """

    # Print results to the console
    print(f"Total Votes: {votes}")
    print("-------------------------")
    for candidate, percentage in percentages.items():
        print(f"{candidate}: {percentage}%")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Print results to the CSV file
    with open(RESULTS_CSV, "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerow([f"Total Votes: {votes}"])
        writer.writerow("-------------------------")
        for candidate, percentage in percentages.items():
            writer.writerow([f"{candidate}: {percentage}%"])
        writer.writerow("-------------------------")
        writer.writerow(f"Winner: {winner}")
        writer.writerow("-------------------------")


def main():
    """The main function."""

    # Read the election data CSV file
    with open(ELECTION_CSV) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)

        # Iterate over the election data rows
        for row in reader:
            # Add the candidate to the candidate list
            if row[2] not in CANDIDATE_LIST:
                CANDIDATE_LIST.append(row[2])

            # Count the total votes
            VOTES += 1

            # Count the votes for each candidate
            if row[2] == "Charles Casper Stockham":
                CHARLIE += 1
            elif row[2] == "Diana DeGette":
                DIANA += 1
            elif row[2] == "Raymon Anthony Doane":
                RAYMON += 1

    # Calculate the percentage of votes for each candidate
    percentages = calculate_percentages(VOTES, CHARLIE, DIANA, RAYMON)

    # Determine the winner of the election
    winner = determine_winner(percentages)

    # Print the election results
    print_results(VOTES, percentages, winner)


if __name__ == "__main__":
    main()