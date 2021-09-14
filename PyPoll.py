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
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    print(headers)