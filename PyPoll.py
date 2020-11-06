# The data that we need to extract:
# 1. Total no of Votes cast.
# 2. A list of Candidates who received Vote.
# 3. Total no of votes for each Candidate.
# 4. % of votes for each candidate.
# 5. Winner based on the popular vote.

# Add the dependencies
import csv
import os

# Assign a variable to load the file from a path 
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to Save the file to another path
file_to_save = os.path.join ("analysis", 'election_analysis.txt')

# 1. Initialize a total vote counter

total_votes = 0

# To open the election_result.csv and read through the file

    ## Declaring a list to capture the names of the candidates
candidate_options = []

    ## Declaring a dict to capture the vote count for each of the candidates
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    #Add all the rows to get the total vote count
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.

for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    Vote_percentage = float(votes)/float(total_votes)*100

    #print(f"{candidate_name} : received {Vote_percentage:.2f} % of total votes. ")  

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    
    print(f"{candidate_name}: {Vote_percentage:.1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count

    if (votes > winning_count) and (Vote_percentage > winning_percentage):
    # Set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = Vote_percentage
 # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# print(f"{candidate_name}: {Vote_percentage:.1f}% ({votes:,})\n")

#print(f"{winning_candidate} : received {winning_percentage:.4f} % of total votes and total votes for the candidate was {winning_count}  ")
#3 . print the total votes count
# print(candidate_votes)
# print(total_votes)
