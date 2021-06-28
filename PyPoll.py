# What we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election by popular vote
import os
import csv 

# Assign the file path to a variable 
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join('analysis','election_analysis.txt')
# Open the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")