import os
import csv

candidate_votes = {}
percent = []

#Access Election Data
filepath = os.path.join("PyPoll", "Resources", "election_data.csv")
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        candidate = row[2]
        if candidate in candidate_votes.keys():
            candidate_votes[candidate]+=1
        else:
            candidate_votes[candidate]=1

#Total votes
total_votes = sum(candidate_votes.values())
#print(total_votes)

#Percentage of Votes and Number of Votes for Candidate
for i in candidate_votes:
    percent = round(float(candidate_votes[i])/total_votes * 100, 2)
    #print(f"{i} : {percent}% {candidate_votes[i]}")

#Winner
    for key in candidate_votes.keys():
        if candidate_votes[key] == max(candidate_votes.values()):
            winner = key

    
#create analysis file
election_file = os.path.join("PyPoll", "Analysis", "election_data.txt")
with open (election_file, 'w') as outputfile:
    outputfile.write(f"Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total Votes: {total_votes}\n")
    outputfile.write("-------------------------\n")
    for i in candidate_votes:
        percent = round(float(candidate_votes[i])/total_votes * 100, 2)
        outputfile.write(f"{i} : {percent}% {candidate_votes[i]}\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Winner: {winner}\n")
    outputfile.write("-------------------------\n")

