import os
import csv


#Set the path to the csv file
budget_csv = os.path.join("PyBank","Resources","budget_data.csv")
total = 0 



    
print(f'Financial Analysis')

print("-----------------------------")

with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile)

    total_months = open(budget_csv)
    rows = total_months.readlines()
    total_months.close()
    print("Total Months: " + str(len(rows)-1))

# The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        if csvreader.line_num == 1:
            continue
        total = total + int(row[1])
     
    print("Total: $" + str(total))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
average = total / (len(rows)-1)
print("Average Change: $" + str(average))

# The greatest increase in profits (date and amount) over the entire period
date = str(budget_csv[0])
profit_losses = str(budget_csv[1])
greatest_increase = max(profit_losses)     
print("Greatest Increase in Profits: " + row[0] + " " + str(greatest_increase))

# The greatest decrease in profits (date and amount) over the entire period

greatest_decrease = min(profit_losses)
print("Greatest Decrease in Profits: " + row[0] + " " + str(greatest_decrease))