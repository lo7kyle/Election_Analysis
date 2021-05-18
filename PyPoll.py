#Pseudocode
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

import os
import csv
# Opening and Reading CSV File
#Assign a variable for the file to load and the path
#Indirect path to the file if we dont know the path. use Import OS
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initializing total votes to 0
total_votes = 0
#Empty list for candidates
candidate_options = []
#Empty dictionary of Candidates with their counted votes
candidate_votes = {}
# Winning Candidate counter and tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#The with-statment reads and wirtes to a file without needing to use the open() and close() everytime
with open(file_to_load) as election_data:

    #To do: read and analyze data here
    # use the reader function to read data 
    file_reader =  csv.reader(election_data)
    #Reads and prints header row
    headers = next(file_reader)
    #print(headers)
    #Loops through each row in the csv file
    for row in file_reader:
        #increments total_votes by 1
        total_votes +=1
        #Loops through candidates from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
        #add candidate name to candidate options list
            candidate_options.append(candidate_name)
        # Start tracking candidate's vote count by assigning candidate as a key
            candidate_votes[candidate_name] = 0
        # adds a vote to the candidates name when their name shows up from the looping    
        candidate_votes[candidate_name] +=1

    # looping through dictionary via candidate names (keys) to retrieve (values) votes
    for candidate_name in candidate_votes:
        #Retrieve Votes = the value of the the keys
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes
        vote_percentage = (float(votes)/ float(total_votes)) * 100
        #print out candiate name and the vote percentage
        #print(f'{candidate_name}: recieved {round(vote_percentage,1)}% of the vote.\n' )
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #If statements that compares each candidates votes to determine winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f'-----------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count}\n'
        f'Winning Percentage: {winning_percentage: .1f}%\n'
        f'-----------------------------\n'
            )
    print(winning_candidate_summary)    

# print (total_votes)
# print(candidate_options)
# print(candidate_votes)








