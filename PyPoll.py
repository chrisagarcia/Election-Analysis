
# what we need:
#   -total number of votes cast
#       *create a candidate_votes{} dictionary
#       *for loop that runs thru to find candidates
#           it can maybe use (last_row - first_row + 1) for each candidate's vote_total

#   -list of candidates with votes
#       *use the dictionary and if statement (if candidate_votes['candidate'] > 0:)

#   -vote totals
#   -%votes for each
#       *vote_total/ (total_rows - 1-header row-)

#   -winner based on popular vote
#       *x=0
#       *for i in candidate_votes.values():
#       *   if i > x:
#       *       x = int(i)
# -----------------------------------------------------------------------------------------------
import csv
import os

# assigning the csv file path with os.path submodule and .join to a variable
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')


# open file with the election data calling it election_data
with open(file_to_load) as election_data:

    # assigning submodule csv.reader to file_reader variable
    file_reader = csv.reader(election_data)
    # printing and skipping the header row
    headers = next(file_reader)
    print(headers)


# write to file
with open(file_to_save, 'w') as outfile:

    outfile.write('Counties in the Election\n-------------------------\n')
    counties_list = ['Arapahoe', 'Denver', 'Jefferson']
    for i in counties_list:
        outfile.write(i)
        outfile.write('\n')


