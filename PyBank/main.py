import os
import csv

# Relative path to the input CSV file
path1 = os.path.join(os.getcwd(), 'module_3')
input_csv_file = os.path.join(path1, 'PyBank', 'resources', 'budget_data.csv')

# Read the CSV file and store the data in a list of dictionaries
with open(input_csv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = list(csvreader)

# Calculate the total number of months
total_months = len(data)

# Calculate the net total amount of "Profit/Losses"
net_total = sum(int(row['Profit/Losses']) for row in data)

# Calculate the changes in "Profit/Losses" over the entire period
changes = [int(data[i]['Profit/Losses']) - int(data[i-1]['Profit/Losses']) for i in range(1, total_months)]

# Calculate the average of those changes
average_change = sum(changes) / (total_months - 1)  # Subtract 1 to exclude the first month

# Find the greatest increase and decrease in profits
greatest_increase = max((row for row in data[1:]), key=lambda x: int(x['Profit/Losses']) - int(data[data.index(x) - 1]['Profit/Losses']))
greatest_decrease = min((row for row in data[1:]), key=lambda x: int(x['Profit/Losses']) - int(data[data.index(x) - 1]['Profit/Losses']))

# Display the results
print(f"Total Months: {total_months}")
print(f"Net Total Amount of Profit/Losses: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${int(greatest_increase['Profit/Losses']) - int(data[data.index(greatest_increase) - 1]['Profit/Losses']):.2f})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${int(greatest_decrease['Profit/Losses']) - int(data[data.index(greatest_decrease) - 1]['Profit/Losses']):.2f})")

# Relative path to the output CSV file
output_csv_file = os.path.join(path1, 'PyBank', 'analysis', 'budget_data_res.csv')

# Write the results to the output CSV file
with open(output_csv_file, 'w', newline='') as csvfile:
    fieldnames = ['Total Months', 'Net Total Amount of Profit/Losses', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({
        'Total Months': total_months,
        'Net Total Amount of Profit/Losses': net_total,
        'Average Change': average_change,
        'Greatest Increase in Profits': f"{greatest_increase['Date']} (${int(greatest_increase['Profit/Losses']) - int(data[data.index(greatest_increase) - 1]['Profit/Losses']):.2f})",
        'Greatest Decrease in Profits': f"{greatest_decrease['Date']} (${int(greatest_decrease['Profit/Losses']) - int(data[data.index(greatest_decrease) - 1]['Profit/Losses']):.2f})"
    })