#!/usr/bin/python

import pandas as pd

mydf = pd.read_csv('data/number-of-severe-floods-in.csv', names = ["Year", "Severity"], skiprows=1)

print("Dataframe content:")
print(mydf)

print("Select minimum value row:")
min = mydf['Severity'].min()
min_df = mydf.loc[mydf['Severity'] == min ]
print(min_df)


print("Select maximum value row")
max = mydf['Severity'].max()
max_df = mydf.loc[mydf['Severity'] == max]
print(max_df)

severity = mydf["Severity"].mean()
print("Flood severity mean: " + str( severity))
print("With greather than severity mean: ")

mydf["Gts"] = mydf["Severity"] > severity
print(mydf)

print("Data with greather than severity mean \"True\"")
gts_mydf = mydf[mydf['Gts']]
print(gts_mydf)

