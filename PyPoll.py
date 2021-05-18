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

#The with-statment reads and wirtes to a file without needing to use the open() and close() everytime
with open(file_to_load) as election_data:

    #To do: read and analyze data here
    # use the reader function to read data 
    file_reader =  csv.reader(election_data)
    #prints header row
    headers = next(file_reader)
    print(headers)





