import pandas as pd
import numpy as np
#loading the data 
df=pd.read_parquet("yellow_tripdata_2022-01.parquet")
print(df)
#checking missing values
print(df.isnull().sum())

# fixing bugs -01  
# airport_fee              71503
# lets know what values exist in this column other than null or missing

# Show unique values and their frequencies (excluding NaNs)
print(df["airport_fee"].value_counts(dropna=True))
# op 
# 0.00    2232427
#  1.25     158950
# -1.25       1051
# 0.00 and 1.25 is valid repalce -1.25 with +1.25
df.loc[df["airport_fee"] < 0 ,'airport_fee']=1.25
# the values which are less than 0 is replaced with 1.25
# now check
print("afther replacing")
print(df["airport_fee"].value_counts)
print(df["airport_fee"].unique)

# all the neg values are cleaned but there are null values present
# calculating  mean and null  values are palcing by mean value

# null_values=df["airport_fee"].mean()
# print(null_values) 

# i got 0.9 as mean values so it is less than 0 so i will not consider the mean ,
# i will directly replace the null values with "0.0"

df["airport_fee"].fillna(0.0, inplace=True)
# checking is there any null values left
print("\n MISSING VALUES",df.isnull().sum())
 #cleaned -01

# now   02
# congestion_surcharge     71503
print(df["congestion_surcharge"].value_counts(dropna=True))
#  2.50    2194746
#  0.00     187045
# -2.50      10631
#  0.75          5
#  1.00          1

# replacing the neg values by 2.50
df.loc[df["congestion_surcharge"] < 0 ,'congestion_surcharge']=2.
print("afther replacing")
print(df["congestion_surcharge"].value_counts)
print(df["congestion_surcharge"].unique)
# no neg values but having null Values 

# calculate  mean and null  values are palcing by mean value

null_values=df["congestion_surcharge"].mean()
print(null_values) 
# got mean=2.3023187113676986 now point after 1 digit 

null_values = round(2.3023187113676986, 1)
# filling 2.3

df['congestion_surcharge'] = df['congestion_surcharge'].fillna(null_values)

print(df.isnull().sum())
#cleaned -02
# df.loc[df["congestion_surcharge"].fillna]

#  NOW  03
# store_and_fwd_flag       71503
print("\n correcting store_and_fwd_flag data")
print(df['store_and_fwd_flag'].isnull().sum())
# TO FIND MISSING VALUE DROPNA =FALSE 
print(df['store_and_fwd_flag'].value_counts(dropna=False))
# WE ARE GOING TO FILL THESE NULL VALUES WITH 'N' becz majorty is 'N'
df['store_and_fwd_flag'] = df['store_and_fwd_flag'].fillna('N')

print(df['store_and_fwd_flag'].value_counts())
print('\n after cleaning')

print(df.isnull().sum())


# now 04
# RatecodeID               71503
print(df['RatecodeID'].value_counts(dropna=True))

# 1.0     2296363
# 2.0       66623
# 5.0       13561
# 99.0       8732
# 3.0        4014
# 4.0        3118
# # 6.0          17
# 99 is invalid

# Step 1: Fill missing RatecodeID values
df['RatecodeID'].fillna(1, inplace=True)

#replace  0 with 99
df.loc[df["RatecodeID"] ==99,'RatecodeID']=1

print(df['RatecodeID'].value_counts())


# Step 2: Convert to integer
df['RatecodeID'] = df['RatecodeID'].astype(int)

ratecode_map = {
    1: 'Standard Rate',
    2: 'JFK',
    3: 'Newark',
    4: 'Nassau/Westchester',
    5: 'Negotiated Fare',
    6: 'Group Ride'
}

df['Ratecode_Label'] = df['RatecodeID'].map(ratecode_map)

# Step 4: Check for any unmapped/null labels
print("Missing Ratecode_Label:", df['Ratecode_Label'].isnull().sum())
 
# now final 
# passenger_count          71503
print(df['passenger_count'].value_counts(dropna=True))
df['passenger_count'] = df['passenger_count'].fillna(1)
print(df['passenger_count'].value_counts())

# print(df['passenger_count'].fillna(99,inplace=True))
print(df.isnull().sum())
print("the data is cleaned")
df.to_csv("cleaned_yellow_tripdata.csv", index=False)
