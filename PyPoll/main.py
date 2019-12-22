# Dependencies
import csv

#define input file location
electiondata = "Resources/election_data.csv"

#define output file location
output = "Resources/election_analysis.txt"

# initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Read input and convert it into a list of dictionaries
with open(electiondata) as election_data:
    reader = csv.DictReader(election_data)

    # For each row...
    for row in reader:

        # Run the loader animation
        #print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to text file
with open(output, "w") as txt_file:

    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

# Determine the winner by looping through the counts
    for candidate in candidate_votes:

    # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
        if (votes > winning_count):
             winning_count = votes
             winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
