# import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the csv file
df = pd.read_csv('listings.csv')
print(df.head()) #check the first 5 rows

# check the column names/ features
print(df.columns)

# check for missing values
print(df.isnull().sum())

# Handle The Missing Values

#1. convert 'last_review' to datetime and handle errors
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
print(df['last_review'].dtypes)

#2. fill the missing values
df.fillna({'reviews_per_month': 0.0, 'price': 0.0}, inplace=True)

#3. drop columns with missing records
df.dropna(subset=['neighbourhood_group', 'license'], inplace=True)
df.drop(['license', 'neighbourhood_group'], axis=1, inplace= True)

# Remove all duplicates
df.drop_duplicates(inplace=True)

# Verify the data cleaning process
print(df.info())

# Check the basic statistical properties of the data
print(df.describe())

# Check for the correlation between 
# different variables
plt.figure(figsize=(10, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(data=corr, linewidth=0.5, annot=True)
plt.show()

# Visualize the distribution of prices
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=50)
plt.title('Distribution of listing prices')
plt.xlabel('Price($)')
plt.ylabel('Frequency')
plt.show()

# Analyse the distribution of room 
#types
plt.figure(figsize=(8, 5))
sns.countplot(x='room_type', data=df)
plt.title('Room type distribution')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()

#Visualise the relationship between 
#price and room type
plt.figure(figsize=(10, 6))
sns.boxplot(x='room_type', y='price', hue='room_type', data=df)
plt.title('Price vs Room Type')
plt.xlabel('Room Type') 
plt.ylabel('Price')
plt.legend(title='Room Type')
plt.show()

# Plot the number of reviews over
# time
df['last_review'] = pd.to_datetime(df['last_review'])
reviews_over_time = df.groupby(df['last_review'].dt.to_period('m')).size()
plt.figure(figsize=(12, 6))
reviews_over_time.plot(kind='line', color='red')
plt.title('Number of reviews over time')
plt.xlabel('Date')
plt.ylabel('Number of reviews')
plt.show()

# Visualise the listing distribution 
# across latitude and longitude with
# different room types
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='room_type')
plt.title('Room type distribution across neighbours')
plt.legend(loc='lower right', title='Room Type')
plt.xlabel('Longitude')
plt.ylabel('latitude')
plt.show()

# Visualise the frequency of listing 
# with respect to the price and 
# minimum number of nights
plt.figure(figsize=(10, 6))
sns.boxplot(x='minimum_nights', y='price', hue='minimum_nights', data=df, palette='husl')
plt.title('Price vs minimum night')
plt.xlabel('minimum nights')
plt.ylabel('price')
plt.legend(title='minimum_nights')
plt.show()