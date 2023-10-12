import os
import csv

#Set the path to the csv file
poll_csv = os.path.join("PyPoll","Resources","election_data.csv")

total_votes = 0
print("Election Results")

print("-----------------------------")
# The total number of votes cast
    
   
print("Total Votes: ")
print("-----------------------------")
# A complete list of candidates who received votes
candidates = []

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row[2] != row[2]:
            candidates = row[2]
            print(candidates)

# The percentage of votes each candidate won

# The total number of votes each candidate won

print("-----------------------------")
# The winner of the election based on popular vote

print("Winner:  ")
print("-----------------------------")


