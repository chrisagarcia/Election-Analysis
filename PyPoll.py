
# what we need:
#   -total number of votes cast
#       *create a candidate_votes{} dictionary
#       *for loop that runs through to find candidates
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

# initializing an accumulator for votes
total_votes = 0

# list to hold names + candidate_votes dictionary
candidate_options = []
candidate_votes = {}

# open file with the election data calling it election_data
with open(file_to_load) as election_data:

    # assigning submodule csv.reader to file_reader variable
    file_reader = csv.reader(election_data)
    # printing and skipping the header row
    headers = next(file_reader)
    print(', '.join(headers))

    # for-loop to read data
    for row in file_reader:

        # find candidate names + init the dict
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # increment candidate_votes by 1 when passed over
        candidate_votes[candidate_name] += 1

        # accumulate total votes
        total_votes += 1

    print(f'total votes cast: {total_votes}\n')

    # winner summary variable set
    winning_candidate = ''
    winning_count = 0
    winning_percentage = 0

    # loop through the candidates in candidate_options[]
    candidate_percent = []
    for i in candidate_options:

        # find and print the percentage of total votes
        votes = candidate_votes[i]
        candidate_percent = 100 * float(votes) / float(total_votes)
        print(f'{i} :: {candidate_percent: .1f}% ({votes:,})\n---------------------------------------')

        # find and declare a winner
        if (votes > winning_count) and (candidate_percent > winning_percentage):
            winning_count = votes
            winning_percentage = candidate_percent
            winning_candidate = i

    winner_summary = (
        '\n\n\n'
        f'________WINNER_ALERT_______________________\n'
        f'Winner::             {winning_candidate}\n'
        f'Winning Vote Count:: {winning_count:,}\n'
        f'Winning Percent::    {winning_percentage:.1f}%\n'
        f'___________________________________________'
    )
    print(winner_summary)


# write to file
with open(file_to_save, 'w') as outfile:

    outfile.write('Counties in the Election\n-------------------------\n')
    counties =['Arapahoe', 'Denver', 'Jefferson']
    outfile.write(', '.join(counties))


