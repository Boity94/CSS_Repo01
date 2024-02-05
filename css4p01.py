#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:11:04 2024

@author: boitumelo_mabakachaba
"""

# Import necessary libraries
import pandas as pd

# Load the dataset
df = pd.read_csv("movie_dataset.csv")

# Display the first few rows to get an overview of the data
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Handle missing values by either dropping or filling them
# For example, dropping rows with any missing values:
df = df.dropna()

df.info()

# Rename columns to remove spaces
df.columns = df.columns.str.replace(" ", "_")


# Perform exploratory data analysis (EDA) to extract insights
# Example: Display basic statistics
print(df.describe())

# Your further analysis and insights extraction here...

# Save the cleaned dataset if needed
df.to_csv("cleaned_movie_dataset.csv")


############################################################################################################
"""
#ANSWERING PROJECT QUESTIONS
"""
############################################################################################################

"""
#READ THE NEW SAVED CLEANED DATA

"""

# Load the dataset
df = pd.read_csv("cleaned_movie_dataset.csv")


# Assuming 'Rating' is the column representing movie ratings
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

# Display the details of the highest-rated movie
print(highest_rated_movie)



# Assuming 'Revenue' is the column representing movie revenue
average_revenue = df["Revenue_(Millions)"].mean()

# Display the average revenue
print(average_revenue)


# Assuming 'Release_Year' is the column representing the movie release year
# and 'Revenue' is the column representing movie revenue
filtered_df = df[(df["Year"] >= 2015) & (df["Year"] <= 2017)]
average_revenue_2015_2017 = filtered_df["Revenue_(Millions)"].mean()

# Display the average revenue for movies from 2015 to 2017
print(average_revenue_2015_2017)


# Assuming 'Release_Year' is the column representing the movie release year
movies_2016 = df[df["Year"] == 2016]

# Display the count of movies released in 2016
print(len(movies_2016))


# Assuming 'Director' is the column representing the movie director
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Display the count of movies directed by Christopher Nolan
print(len(nolan_movies))


# Assuming 'Rating' is the column representing the movie ratings
highly_rated_movies = df[df['Rating'] >= 8.0]

# Display the count of movies with a rating of at least 8.0
print(len(highly_rated_movies))


# Assuming 'Director' is the column representing the movie director
# and 'Rating' is the column representing the movie ratings
nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()

# Display the median rating of movies directed by Christopher Nolan
print(median_rating_nolan_movies)


# Assuming 'Release_Year' is the column representing the movie release year
# and 'Rating' is the column representing the movie ratings
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()

# Display the year with the highest average rating
print(year_highest_average_rating)


# Assuming 'Release_Year' is the column representing the movie release year
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

# Calculate the percentage increase
percentage_increase = ((len(movies_2016) - len(movies_2006)) / len(movies_2006)) * 100

# Display the percentage increase
print(percentage_increase)

# Assuming 'Actors' is the column representing the movie actors
all_actors = df['Actors'].str.split(', ', expand=True).stack()

# Find the most common actor
most_common_actor = all_actors.value_counts().idxmax()

# Display the most common actor
print(most_common_actor)

# Assuming 'Genre' is the column representing the movie genres
all_genres = df['Genre'].str.split(', ').explode()

# Find the number of unique genres
unique_genres_count = all_genres.nunique()

# Display the number of unique genres
print(unique_genres_count)



############################################################################
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have numerical features like 'Rating', 'Revenue', 'Metascore', etc.
numerical_features = df[['Rating', 'Revenue_(Millions)', 'Metascore', 'Runtime_(Minutes)']]

# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

# Create a heatmap for visualization
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()



