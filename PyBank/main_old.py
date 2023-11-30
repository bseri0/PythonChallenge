import os
import csv
import pandas as pd
import contextlib

print("CUR DIR:  " + str(os.getcwd()))
# Relative path to the input CSV file
path1 = os.path.join(os.getcwd(),'module_3')
print("path1:" + path1)
input_csv_file = os.path.join(path1,'PyBank','resources', 'budget_data.csv')
print("Input CSV path:" + input_csv_file)
# Relative path to the output CSV file
output_csv_file = os.path.join(path1,'PyBank','analysis', 'budget_data_res.csv')

with contextlib.redirect_stdout(open(output_csv_file, 'w')):

    # Read the CSV file data set into a pandas DataFrame
    df = pd.read_csv(input_csv_file)

    # Print the DataFrame
    print(df.to_string())

    # Calculate the number of months
    months = len(df.groupby('Date'))

    # Calculate the total profit/losses
    summ = sum(df['Profit/Losses'])

    # Calculate the average profit/losses per month
    avg = summ / months

    # Calculate the minimum and maximum values in the `Profit/Losses` column
    min_row = df.loc[df['Profit/Losses'].idxmin()]
    max_row = df.loc[df[['Profit/Losses']].idxmax()]

    # Print the results
    print(f"Months: {months}")
    print(f"Sum: {summ}")
    print(f"The Average : {avg}")
    print(f"The minimum value: {min_row}")
    print(f"The maximum value: {max_row}")