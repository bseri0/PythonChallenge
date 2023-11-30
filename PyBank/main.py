import os
import csv

print("CUR DIR:  " + str(os.getcwd()))

# Relative path to the input CSV file
path1 = os.path.join(os.getcwd(), 'module_3')
print("path1:" + path1)
input_csv_file = os.path.join(path1, 'PyBank', 'resources', 'budget_data.csv')
print("Input CSV path:" + input_csv_file)

# Read the CSV file and store the data in a list of dictionaries
with open(input_csv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = list(csvreader)

# Calculate the number of months
months = len(data)

# Calculate the total profit/losses
summ = sum(int(row['Profit/Losses']) for row in data)

# Calculate the average profit/losses per month
avg = summ / months

# Find the minimum and maximum values in the `Profit/Losses` column
min_row = min(data, key=lambda x: int(x['Profit/Losses']))
max_row = max(data, key=lambda x: int(x['Profit/Losses']))

# Print the results
print(f"Months: {months}")
print(f"Sum: {summ}")
print(f"The Average: {avg}")
print(f"The minimum value: {min_row}")
print(f"The maximum value: {max_row}")

# Relative path to the output CSV file
output_csv_file = os.path.join(path1, 'PyBank', 'analysis', 'budget_data_res.csv')

# Write the results to the output CSV file
with open(output_csv_file, 'w', newline='') as csvfile:
    fieldnames = ['Months', 'Sum', 'Average', 'Minimum Value', 'Maximum Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({
        'Months': months,
        'Sum': summ,
        'Average': avg,
        'Minimum Value': min_row['Profit/Losses'],
        'Maximum Value': max_row['Profit/Losses']
    })