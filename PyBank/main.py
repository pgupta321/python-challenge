import os
import csv
import statistics

path = os.path.join("Resources/03-Python_Homework_PyBank_Resources_budget_data.csv")

# Read csv file
with open(path, newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    next(reader)

    # Create a list of the file in order to grab the first profit amount (prev_profit) by its location
    # Need this value for the method to calculate monthly changes
    reader_list = list(reader)
    prev_profit = reader_list[1][1]

    # Create empty lists
    months = []
    profit_loss = []
    monthly_changes = []

    
    for row in reader_list:

        # Append column contents to lists
        months.append(row[0])
        profit_loss.append(int(row[1]))

        # Calculate and store values for monthly changes in profits
        change = float(row[1]) - float(prev_profit)     # Calculate difference
        monthly_changes.append(change)                  # Append difference to monthly_changes list
        
        # Assign current profit value to previous profit variable for use in next iteration
        prev_profit = row[1]


    # Calculate net total profits
    netTotal = sum(profit_loss)

    # Calculate average change
    # Delete first value in lieu of skipping the first data row
    del(monthly_changes[0])
    averageChange = round(statistics.mean(monthly_changes), 2)
    
    # Find greatest increase and greatest decrease in profits
    gi = max(monthly_changes)
    gd = min(monthly_changes)

    # Find list item number for months of greatest increase and greatest decrease
    for x in enumerate(monthly_changes):
        if x[1] == gi:
            gi_month_num = x[0] + 1     # The monthly change corresponds to the later month, so it needs + 1. 
        elif x[1] == gd:
            gd_month_num = x[0] + 1

    # Find months of greatest increase and decrease based on their line number in the file list
    for line_num, line in enumerate(reader_list):
        if line_num == gi_month_num:
            gi_month = line[0]
        elif line_num == gd_month_num:
            gd_month = line[0]
        
# Analysis Report to terminal
print("Financial Analysis \n---------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${netTotal}')
print(f'Average Change: ${averageChange}')
print(f'Greatest Increase in Profits: {gi_month} (${gi})')
print(f'Greatest Decrease in Profits: {gd_month} (${gd})')


# Export text file
output_path = ("Resources/Python PyBank - Prerna Gupta.txt")

with open(output_path, 'w') as txtfile:
    print("Financial Analysis \n---------------------------\n", 
        f'Total Months: {len(months)}\n', 
        f'Total: ${netTotal}\n',
        f'Average Change: ${averageChange}\n',
        f'Greatest Increase in Profits: {gi_month} (${gi})\n',
        f'Greatest Decrease in Profits: {gd_month} (${gd})',
        file=txtfile)