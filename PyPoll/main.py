import os
import csv
import operator         # useful for finding winner

path = os.path.join('Resources/03-Python_Homework_PyPoll_Resources_election_data.csv')

# Initialize variables, lists, and dictionaries
totalvotes = 0
candidates = []
vote_count = {}
vote_percent = {}

# Read csv file
with open(path, newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    next(reader)
    
    for row in reader:

        # Count total votes
        totalvotes += 1

        # Make list of candidates and count votes in vote_count dictionary
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count[row[2]] = 1          # Add candidate as the "key" and vote as the "value"
        elif row[2] in candidates:
            vote_count[row[2]] += 1
        

        # Calculate voting percentages based off the values in the vote_count dictionary
        # Add those to the vote_percent dictionary, using same keys
        # Also add the vote count to the end of each key's value for ease of printing
    for key, value in vote_count.items():
        vote_percent[key] = str(round(((value/totalvotes) * 100), 3)) + "% ("+str(value) + ")"
        

    # Find winner from the vote_count dictionary
    winner = max(vote_count.items(), key=operator.itemgetter(1))[0]


# Results to terminal
print('Election Results\n--------------------------------')
print(f'Total Votes: {totalvotes}\n--------------------------------')
for key, val in vote_percent.items():
    print(key, ": ", val)
print(f'--------------------------------\nWinner: {winner}\n--------------------------------')


# Export text file
output_path = ("Resources/Python PyPoll - Prerna Gupta.txt")

with open(output_path, 'w') as txtfile:
    print('Election Results\n--------------------------------\n',
    f'Total Votes: {totalvotes}\n--------------------------------',
        file=txtfile)
    for key, val in vote_percent.items():
        print(key, ": ", val,
        file=txtfile)
    print(f'--------------------------------\nWinner: {winner}\n--------------------------------',
        file=txtfile)