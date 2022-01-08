# Retreive the data
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

# import csv

# file_to_load = 'Resources/election_results.csv'
# with open(file_to_load) as election_data:
#     print(election_data)

# import os
# file_to_load = os.path.join("Resources", "election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data)

#import csv
# import os
# file_to_load = os.path.join("Resources", "election_results.csv")
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     for row in file_reader:
#         print(row)
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Arapahoe\nDenver\nJefferson")
# Add our dependencies.

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)