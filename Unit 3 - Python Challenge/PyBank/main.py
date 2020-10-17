import os
import csv

month = []
revenue = []
revenue_ch = []
monthly_ch = []

#import budget data
filepath = os.path.join("PyBank", "Resources", "budget_data.csv")
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

#months
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    total_months = (len(month))
    #print(total_months)

#revenue
    revenue_int = map(int, revenue)
    total_revenue = sum(revenue_int)

#revenue change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_ch.append(profit_loss)
    Total = sum(revenue_ch)
    monthly_ch = round(Total / len(revenue_ch), 2)

#Greatest increase
    profit_increase = max(revenue_ch)
    x = revenue_ch.index(profit_increase)
    month_increase = month[x+1]

#Greatest decrease
    profit_decrease = min(revenue_ch)
    y = revenue_ch.index(profit_decrease)
    month_decrease = month[y+1]


"""
print("Financial Analysis")
print(f"Total Number of Month:" + str(total_months))
print(f"Total Revenue:" + str(total_revenue))
print(f"Average Change:" + str(monthly_ch))
print(f"Greatest Increase in Profits: {month_increase} {profit_increase}")
print(f"Greatest Decrease in Profits: {month_decrease} {profit_decrease}")
"""

#Create Analysis file
budget_file = os.path.join("Pybank", "Analysis", "budget_data.txt")
with open (budget_file, 'w') as outputfile:
    outputfile.write("Financial Analysis\n")
    outputfile.write("----------------------------\n")
    outputfile.write(f"Total Months: {total_months}\n")
    outputfile.write(f"Total: ${total_revenue}\n")
    outputfile.write(f"Average Change: ${monthly_ch}\n")
    outputfile.write(f"Greatest Increase in Profits: {month_increase} (${profit_increase})\n")
    outputfile.write(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})\n")


