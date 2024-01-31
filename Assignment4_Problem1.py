import pandas as pd
import matplotlib.pyplot as plt
 
#Reading/loading the provided CSV File
file_path = 'data.csv'
df = pd.read_csv(file_path)

#Showing the basic statistical description about the data.
print(df.describe())


#Checking for null values and Replacing the null values with the mean
df.fillna(df.mean(), inplace=True)

#Selecting at least two columns and aggregate the data using: min, max, count, mean
columns_to_aggregate = df.columns 
aggregated_data = df[columns_to_aggregate].agg(['min', 'max', 'count', 'mean'])
print(aggregated_data)

#Filtering the dataframe to select the rows with calories values between 500 and 1000
filtered_df1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]

#Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
filtered_df2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]

#Creating a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
df_modified = df.drop('Maxpulse', axis=1)

#Deleting  the “Maxpulse” column from the main df dataframe
df.drop('Maxpulse', axis=1, inplace=True)

#Converting the datatype of Calories column to int datatype
df['Calories'] = df['Calories'].astype(int)

#Using pandas creating a scatter plot for the two columns (Duration and Calories).
df.plot.scatter(x='Duration', y='Calories', title='Scatter Plot: Duration vs Calories')
plt.show()