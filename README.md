# Election_Analysis
Using python to perform a simple audit of an election

## Project Overview

A Colorado Board of Elections employee has tasked me with the following audit of a recent local congressional election:
	1. Calculate the total number of votes casts.
	2. Get a complete list of candidates who received votes.
	3. Calculate the total number of votes each candidate received.
	4. Calculate the percentage of votes for each candidate
	5. Determine the winner of the election based on popular vote

## Resources
	* Data Source: election_results.csv
	* Software Python 3.7.4, Visual Studio Code, 1.56.2
	
### Code:
'''python:
# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
#used to store county as key and votes and values. list is used to store counties
county_options = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
# used as empty variables to hold results and used for comparision
highest_county = ""
turnout_count = 0
turnout_percentage =0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file. This for-loop iterates through every row and adds
    # into empty dictionary 
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row. found in column B index 1
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties. add county to list
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count. initialize county as 0
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count. start incrementing county by 1 when counted
        county_votes[county_name] += 1

# Just checking to see if values were extracted in terminal
# print(county_options)
# print(county_votes)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    #This For-loop loops the dictionary for the values that was stored in it from previous loop
    for county_name in county_votes:
        # 6b: Retrieve the county vote count. Get the  turnout (values) of each county
        county_turnout = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(county_turnout) / float(total_votes) * 100

         # 6d: Print the county results to the terminal. prints (county, percentage, total votes)
        county_results = (
            f'{county_name}: {county_percentage:.1f}% ({county_turnout:,})\n')
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_turnout > turnout_count) and (county_percentage>turnout_percentage):
            turnout_count = county_turnout
            highest_county = county_name
            turnout_percentage = county_percentage

    # 7: Print the county with the largest turnout to the terminal.

    highest_county_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {highest_county}\n"
        f"-------------------------\n"
        )
    print(highest_county_results)
    # 8: Save the county with the largest turnout to a text file.
    
    txt_file.write(highest_county_results)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

'''

## Results
![Results of the Election Audit](https://github.com/lo7kyle/stock-analysis/blob/main/Resources/Nested%20Loop%202018_Time.PNG)

### Election-Audit Results/Outcomes: 

*There were a total of __369,711__ votes casted

* Refer to the **_Image_** above to see total percentage votes for each county and which county had the highest total votes

* Denver had the highest turnout at **82.8%** with (306,055 Votes)

* From the results above we see that **Diana DeGette** won in a landslide with **73.8%** (272,892 Votes) of the votes.

## Summary

Election-Audit Summary: With this script we can calculate the total vote counts of any county of any candidate. As long as we know the candidate (key) and their respective votes (values), we can do many more analysis than just finding the total percentage. We can use this script to store these dictionaries into an even larger dataframe such as for the whole state of Colorado. Since this script is modular we can adjust one number (column) to perform many analyses. One change to the script would be to export the data as another CSV that can be added into a larger data set. Another thing to change can be to look at the Voter ID to make sure each voter has a unique voter ID so that there wouldn't be a double count. 

## Analysis

This challenge of creating a script to audit a local congressional election was extremely informative and teaches me the power of importing data from a CSV and writing the results into a nicely simple .TXT file. Previously we would have done the analysis in excel, however the functions of excel is limited only to a particular data set. With Python we can merely adjust which columns we want to look at and perform a simple analysis that VBA can't offer without a more complex code. In this challenge we looked at both candiate and county votes and used the same logic and analysis to find out the total votes and percentages just by adjusting which column of data we wanted. In coding, if we can copy and paste an algorithm to perform different taks, that code would be considered robust. We used the logic of extracting data from a csv into a dictionary and looping through the dictionary to do our analyses. This skillset of learning how to copy and paste code and apply it to different analysis will save a lot of time when trying to do bigger more complex analysis. The analysis of this script was simple, however there are many ways to audit an election that can account for many different parameters such as ways of voting (mail ins, electronics, etc..) and even unique voter ID to make check the integrity of the person who voted isn't being duplicated. 

## Challenges
There were many concepts in this challenge that I am still learning to grasp. I am still learning the difference between getting values vs getting keys. I still confuse the two and have to practice more on extracting data in a dictionary. I understand there are many ways to extract the data desired such as using the range() or len() functions, but since we didn't use it in this challenge I still get confused on when to use that method. Another challenge I ran across was understanding how dictionaries work in a list (list of dictionaries). When incrementing the candidate votes dictionary I used [] instead of the {} to pass the parameter of the candidate's name when counting a vote towards them. Again, I believe this all can be solved with more exposure and practice. 
