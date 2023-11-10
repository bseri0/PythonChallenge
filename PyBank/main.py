import os
import csv
import pandas as pd
import sys

sys.stdout = open('C:\\Users\\user\\OneDrive\\Desktop\\files_apps\\RU-PSEG-dsbc\\module_3\\PyBank\\analysis\\budget_data_res.csv', 'w')
 # Read the CSV file data set into a pandas DataFrame
df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\files_apps\RU-PSEG-dsbc\module_3\PyBank\resources\budget_data.csv")
print("Current WD is:: " + os.getcwd())
a = os.path.join('..', os.path.join(os.getcwd(),'main.py'))
print(a)
# Print the DataFrame
print("This is the DF:" + df.to_string()) 
#df[['Date','year']] = df['Date'].str.split('-',expand=True)
#print(df)
#calc the HW q's
months = len(df.groupby('Date'))
summ = sum(df['Profit/Losses'])
#percentage change = (profit last value - profit first value) / point last value * 100
#avg_chg = df.apply(lambda x: (x['Profit/Losses'].values[-1] - x['Profit/Losses'].values[0]) / x['Profit/Losses'].values[-1] * 100)
avg_chg = pd.Series(['Profit/Losses'])

print("Months:  " + str(int(months)))
print("Sum:  " + str(summ))
avg = summ/months
print("The Avg : " + str(avg))
# Calculate the average per month
pf_lss_grp = df.groupby('Date')['Profit/Losses']
pf_lss_list = [pf_lss_grp]
#print(str(pf_lss_list))
minn = df['Profit/Losses'].idxmin()
min_row = df.iloc[minn]
maxx = df[['Profit/Losses']].idxmax()
max_row = df.iloc[maxx]
print("the min value: " + str(min_row))
print("The max value: " + str(max_row))
# Print the average
sys.stdout.close()
