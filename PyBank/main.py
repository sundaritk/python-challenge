#Import packages
import os
import csv
import sys

#define input file location
bankbudget = os.path.join("Resources", "budget_data.csv")

# define output file location
budgetanalysis = os.path.join("Resources", "budget_analysis.txt")

# initialize variables
totl_mon = 0
mon_of_chg = []
rev_chg_lst = []
grtest_inc = ["", 0]
grtest_dec = ["", 9999999999999999999]
totl_rev = 0


#open csv and use it to create lists of header items
with open(bankbudget) as RevData:
    reader = csv.DictReader(RevData)

    # extract first row to avoid appending to rev_chg_lst
    first_row = next(reader)
    totl_mon= totl_mon+ 1
    totl_rev = totl_rev + int(first_row["Profit/Losses"])
    prev_rev = int(first_row["Profit/Losses"])
    for row in reader:
   
        # calculate total
        totl_mon= totl_mon+ 1
        totl_rev = totl_rev + int(row["Profit/Losses"])

        # calculate revenue change
        rev_chg = int(row["Profit/Losses"]) - prev_rev
        prev_rev = int(row["Profit/Losses"])
        rev_chg_lst = rev_chg_lst + [rev_chg]
        mon_of_chg= mon_of_chg+ [row["Date"]]

        # calculate the greatest increase
        if rev_chg > grtest_inc[1]:
            grtest_inc[0] = row["Date"]
            grtest_inc[1] = rev_chg

        # calculate the greatest decrease
        if rev_chg < grtest_dec[1]:
            grtest_dec[0] = row["Date"]
            grtest_dec[1] = rev_chg

# calculate the Average Revenue Change
rev_avg = sum(rev_chg_lst) / len(rev_chg_lst)

#Print the results and Save Output file as text file

output = (
        f"\nFinancial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {totl_mon}\n"
        f"Total Revenue: ${totl_rev}\n"
        f"Average Revenue Change: ${rev_avg}\n"
        f"Greatest Increase in Revenue: {grtest_inc[0]} (${grtest_inc[1]})\n"
        f"Greatest Decrease in Revenue: {grtest_dec[0]} (${grtest_dec[1]})")

print(output)

with open(budgetanalysis, "w") as txt_file:
    txt_file.write(output)

