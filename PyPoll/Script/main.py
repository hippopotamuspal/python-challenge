# Call in CSV 
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Current Working Directory:", os.getcwd())

# Construct the path to the CSV file
csvpath = os.path.join(script_dir, "..", "Resources", "election_data.csv")

# with open(csvpath) as csvfile:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    header = next(csvreader)

    # Set dictionary to be used
    VoteCountUnique = {}
    
    # Count # of Votes cast in loop by initiating VoteCount at 0
    TotalVoteCount = 0

    # Count votes for each candidate  
    for row in csvreader:
        # Get candidate name 
        candidate = row[2]
        # Add a vote to the total vote counter
        TotalVoteCount += 1
        # Check if candidate is already a key in VoteCountUnique dict
        if candidate in VoteCountUnique:
            # If candidate is already in the dictionary, add one to their total
            VoteCountUnique[candidate] += 1
        else:
            # If candidate is NOT in dictionary, set 1 as total for Votes
            VoteCountUnique[candidate] = 1

    # Find percentages for each candidate by looping through candidates and dividing by total votes
    for candidate in VoteCountUnique:
        vote_percentage = (VoteCountUnique[candidate] / TotalVoteCount) * 100
        # Expand VoteCountUnique dict to include what percentages were calculated
        VoteCountUnique[candidate] = (VoteCountUnique[candidate], vote_percentage)
    
    
    print("--------------------------------")
    print("Election Results")
    print("--------------------------------")
    
    # Print the number of total  Votes cast
    print(f"Total Votes: {TotalVoteCount}")

    # Separate Next Results:
    print("-------------------------------")

    # Print Candidate Names, Percentages, & Vote Counts 
    for candidate, (votes, percentage) in VoteCountUnique.items():
        print(f"{candidate}: {percentage:.3f}% ({votes})")

    #Find top candidate then print
    TopVoteGetter = max(VoteCountUnique, key=VoteCountUnique.get)
    print("------------------------------")
    print(f"Winner: {TopVoteGetter}")

    # Set variable for output file
    output_file = os.path.join("election_summary_final.csv")

    #  Open the output file
    with open(output_file, "w", newline='') as yafile:
        writer = csv.writer(yafile)

        #Write total voted
        writer.writerow(["Total Votes",TotalVoteCount])
        writer.writerow([])

        # Write the header row
        writer.writerow(["Candidate","Percentage","Votes"])

        # Write in results
        for candidate, (votes, percentage) in VoteCountUnique.items():
            writer.writerow([candidate,f"{percentage:.2f}%", votes])
        
        # List Top Vote Getter
        writer.writerow([])
        writer.writerow(["Winner:", TopVoteGetter])                    