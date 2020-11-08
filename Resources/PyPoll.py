# The data that we need to extract:
# 1. Total no of Votes cast.
# 2. A list of Candidates who received Vote.
# 3. Total no of votes for each Candidate.
# 4. % of votes for each candidate.
# 5. Winner based on the popular vote.

import csv
import os

# Assign a variable for the file to load and the path. This is direct path.
#file_to_load = 'Resources\election_results.csv'
# Assign a variable to load the file from a path 
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to Save the file to another path
file_to_save = os.path.join ("analysis", 'election_analysis.txt')

# To open the file alternatively with "with"

with open(file_to_load) as election_data:

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')
   
    # To do: Read and perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    #print(headers)
    for row in file_reader:
         print(row)


    #print(election_data)
# # Close the file.
# election_data.close()
# print('File opend and closed')

# Create a filename variable to a direct or indirect path to the file. 

# #print(file_to_save)
# # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# Using the with statement open the file as a text file.

# with open(file_to_save , 'w') as txt_file:  

# # Write some data to this file

# # # outfile.write("Hello World")
# #     txt_file.write("Hello again")

#     # # Write three counties to the file.
#     #  txt_file.write("Arapahoe\n ")
#     #  txt_file.write("Denver\n\")
#     txt_file.write("Counties in the Election\n ")
#     txt_file.write("--------------------------------------------------\n--------------------------------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
# txt_file.close()