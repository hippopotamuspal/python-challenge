# Call in CSV
import os
import csv

# Ensure the script directory is correct
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Current Working Directory:", os.getcwd())

# Make the path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row first 
    csv_header = next(csvreader)
    
    # Declare value of total months by declaring rows as list variable and finding length of rows
    rows = list(csvreader)
    total_months = len(rows)

    print(f"Total Months: {total_months}")

    # On to the total amount of profit and losses. Create a variable to count for me and declare it initially equal to zero
    NetRevenue = 0
    # Find net total amount by iterating through each row
    for row in rows:
        NetRevenue += int(row[1])
    # Print net total amount
    print(f"Total: ${NetRevenue}")

# Open the CSV file again
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row first 
    csv_header = next(csvreader)
    # Set up dict for Changes and Change Dates
    ChangeDates = {}
    
    # I need a way to read the first row to set an initial value for ValuePrevious
    ValuePrevious = int(rows[0][1])
    
    # Iterate to find each value and
    for row in rows:
        # Set value of current cell
        ValueCurrent = int(row[1])
        # Find change
        ValueChange = ValueCurrent - ValuePrevious
        # Make sure 1st row doesn't subtract from itself and go into dict
        if ValueChange != 0:
            # Store date with change amount
            ChangeDates[row[0]] = ValueChange

        # Update previous current value
        ValuePrevious = ValueCurrent

    # Print Average
    ChangeValues = list(ChangeDates.values())
    ChangeAverage = sum(ChangeValues) / len(ChangeValues)
    print(f"Average Change: ${ChangeAverage:.2f}")        
        
    # Time to find greatest positive and negative change by using a for loop to run through the ChangeValues dict
    GreatestIncrease = -100000000000000000
    GreatestDecrease = 100000000000000000

    for date, change in ChangeDates.items():
        if change > GreatestIncrease:
            GreatestIncrease = change
            GreatestIncreaseDate = date   
        if change < GreatestDecrease:
            GreatestDecrease = change
            GreatestDecreaseDate = date

    # Print Greatest Increase and Decrease
    print(f"Greatest Increase in Profits: {GreatestIncreaseDate} (${GreatestIncrease})")
    print(f"Greatest Decrease in Profits: {GreatestDecreaseDate} (${GreatestDecrease})")


    # Set variable for output file
    output_file = os.path.join("budget_data_final.csv")

    #  Open the output file
    with open(output_file, "w", newline='') as newfilebaby:
        writer = csv.writer(newfilebaby)

        #Write total Months
        writer.writerow(["Total Months",total_months])

        # Write net total
        writer.writerow(["Total",NetRevenue])

        # Write average change
        writer.writerow(["Average Change",{ChangeAverage}])

        #Skip Line
        writer.writerow([])

        #Write Headers for Increases,Decreases
        writer.writerow(["Greatest Increase or Decrease","Date","Amount"])

        #Write Greatest Increase/Decrease
        writer.writerow(["Greatest Increase",f"{GreatestIncreaseDate}",f"${GreatestIncrease}"])
        writer.writerow(["Greatest Decrease",f"{GreatestDecreaseDate}",f"${GreatestDecrease}"])