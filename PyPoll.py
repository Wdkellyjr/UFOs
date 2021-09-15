# Assign a variable for the file to load and path.
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load =os.path.join("Resources", "election_results.csv")
#Open the election results and read the file
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)

#Create a filename variale to a direct or indirect path to the file
file_to_save =os.path.join("analysis", "election_analysis.txt")
#Using the with statement open the file as a text file
outfile = open(file_to_save, "w")
#Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()

file_to_save = os.path.join("analysis" ,"election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe,")
    txt_file.write("Denver,")
    txt_file.write("Jefferon,")

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe, Denver, Jefferson")

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapaho\nDenver\nJefferson")

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nDenver\nJefferson")

    file_to_load = 'Resources/election_results.csv'
    with open(file_to_load) as election_data:
        print(election_data)

#Add our dependencies
#import csv
#import os
# Assign a variable to load a file from a path
#file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    #file_reader = csv.reader(election_data)
    #Print each row is the CSV file.
    #for row in file_reader:
        #print(row)

#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total voter counter
total_votes = 0

#Candidate Options
candidate_options = []


# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)

    #Print each row n the CSV file.
    for row in file_reader:
            #2. Add to the total vote count
            total_votes += 1

            # Print the candidate name from each row
            candidate_name = row[2]

            # If the candidate does not match any existing canidate...
            if candidate_name not in candidate_options:
                # Add it to the list of candidates.
                candidate_options.append(candidate_name)

# 3. Print the total votes
    print(candidate_options)

#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total voter counter
total_votes = 0

#Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)

    #Print each row n the CSV file.
    for row in file_reader:
            #2. Add to the total vote count
            total_votes += 1

            # Print the candidate name from each row
            candidate_name = row[2]

            # If the candidate does not match any existing canidate...
            if candidate_name not in candidate_options:

                # Add it to the list of candidates.
                candidate_options.append(candidate_name)

                # 2. Begin tracking that candicate's votes count.
                candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count,
            candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # TO do: print out each candidate's name, vote count, and percenatge of 
    # # votes to the terminal.

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = 
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

