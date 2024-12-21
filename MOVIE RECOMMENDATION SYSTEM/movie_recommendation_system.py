# -*- coding: utf-8 -*-
"""Movie Recommendation  System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wLJRm-zP1JLuGfXagdFnkeyNuxu2aFgg

### **Introduction**

In today’s digital world, users have access to countless movies and TV shows on streaming platforms. Choosing the right content from such large collections can be challenging. Recommendation systems help by providing personalized suggestions, making it easier for users to find what they like.

A **Movie Recommendation System** uses machine learning to analyze user preferences, past activity, and movie details to suggest movies that match their interests. Platforms like Netflix and Amazon Prime use these systems to improve user experience and engagement.

This project focuses on building a movie recommendation system using techniques like Content-Based Filtering and Collaborative Filtering. It aims to:
1. Analyze movie data to identify important features.
2. Recommend movies based on user preferences.
3. Evaluate the system’s accuracy and performance.

The goal is to show how machine learning can make data-driven recommendations and improve the movie selection process for users.

there are three types of recommendation systems

**1)content based recommendation system.** : recomends movies to users based on the movies or content they have watched before.

**2)popularity based recommendation system.** : suggests movies which are very popular. example,top 10 movies in UK on Amazon Prime and Netflix.

**3)collobarative recommendation system.** : Groups peoples based on their watching pattern.that is peoples with same taste in movies will be recommended same movies. example, if person A and person B likes movie Star wars and person B likes the movie say xyz then recommendation system will suggest movie xyz to person A.(of course data there is not only two records,its greater in volume😂.)

The steps to follow in this project are outlined below:

**1)Data Collection:** Gather movie-related data such as titles, genres, and descriptions.

**2)Data Preprocessing:** Clean and organize the data to make it suitable for analysis.

**3)Feature Extraction:** Convert textual data (e.g., genres, descriptions) into numerical data (feature vectors).

**4)Calculate Similarity Scores:** Compute similarity scores between movies to determine how similar they are. This is achieved using a similarity measure, such as cosine similarity.

**5)User Input:** Allow the user to input a movie name.
Using the cosine similarity algorithm, which measures the similarity between vectors, the system identifies movies similar to the one entered by the user. Based on this comparison, the system generates a list of recommended movies for the user.

**IMPORTING NECESSARY LIBRARIES AND DEPENDENCIES**

**Spell Correction with `difflib`:**  
When a user provides input (like a movie name), there is a possibility of spelling mistakes. To handle this, we use `difflib.get_close_matches()` to find the closest match for the user's input from the movie titles available in our dataset. This helps us retrieve the most relevant movie despite minor errors in the input.

**Vectorizer Feature:**  
The vectorizer feature is used to transform textual data (like movie titles or descriptions) into numerical data, called feature vectors. These vectors represent the text in a way that makes it suitable for machine learning algorithms.

**Cosine Similarity:**  
Cosine similarity calculates a confidence score that measures how similar two movies are based on their feature vectors. This score helps us recommend movies that are closely related to the user's input or preferences.
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""**Data collection and Preprocessing**"""

#loading data from csv file to pandas dataframe
movies_data = pd.read_csv('/content/movies.csv')

#print first five rows and last five rows of dataset
movies_data.head()

print last five rows and last five rows of dataset
movies_data.tail()

"""all columns in the table are self explnatory which tells about the movies description and features

**Summary of Dataset.**
"""

movies_data.describe()

"""**Size of Dataset**"""

movies_data.shape

"""**Feature Selection**

here i have selected a couple of features from orignal dataset which i think are important accourding to me.
"""

selected_feature = ['genres','keywords','overview','popularity','runtime','vote_average','cast']
print(selected_feature)

"""**Data Preprocessing : Replacing null values**

: here we Replace null values with null string
"""

for feature in selected_feature:
  movies_data[feature] = movies_data[feature].fillna('')

#concatinating all the above selected features
combined_features = movies_data['genres']+ ' ' + ['keywords'] +' ' + ['overview'] +' ' + ['popularity'] +' ' + ['runtime'] +' ' +['vote_average']+' ' + [ 'cast']

print(combined_features)

"""Feature Extraction : converting textual data into numerical data"""

vectorizer = TfidfVectorizer()

feature_vector = vectorizer.fit_transform(combined_features)

print(feature_vector)

"""**Cosine Similarity for Similarity Score in Movie Datasets**


Cosine Similarity is a metric used to measure how similar two vectors are by calculating the cosine of the angle between them. It's commonly used in text-based recommendation systems (like movies) to compare feature vectors derived from textual data, such as movie plots, genres, or cast.


### Steps to Calculate Similarity Score Using Cosine Similarity:

1. **Convert Text Data to Numerical Vectors:**
   - Use a vectorizer (e.g., `TfidfVectorizer` or `CountVectorizer`) to transform text data (e.g., movie descriptions or genres) into feature vectors.

2. **Compute Cosine Similarity:**
   - Use `cosine_similarity` from `sklearn` to calculate the pairwise similarity between all feature vectors.

3. **Extract Similarity Scores:**
   - For a given movie, retrieve its similarity scores with all other movies from the similarity matrix.

4. **Sort Similarity Scores:**
   - Sort the similarity scores in descending order to find the most similar movies.

5. **Recommend Movies:**
   - Use the top similarity scores to recommend the most relevant movies to the user.
"""

similarity = cosine_similarity(feature_vector)

print(similarity)

print(similarity.shape)

"""user input"""

movie_name = input('Enter your favourite movie name :')

"""Creating a list of all movies presnt in the dataset."""

list_of_all_titles = movies_data['title'].tolist()

print(list_of_all_titles)

"""finding the closest match for input move name"""

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

"""in the above stament our result was a list of matching value so we all want is just one closest match so we use find_close_match[0] to get output which will be the first value in the list."""

close_match =  find_close_match[0]
print(close_match)

# finding the index of the movie with title

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

#getting a list of similar movies using similarity score
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

len(similarity_score)

"""**sorting the movies based on their similarity score**

here we are arranging movies from higher similarity score to lower similarity score .and we use similariy score and x is nothing but similarity_score
"""

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

# print the name of similar movies based on the index
#in this step we are going to use index of movie similar to title we used in previous step.
print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<20):
    print(i, '.',title_from_index)
    i+=1

"""Movie Recommendation System"""

movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<20):
    print(i, '.',title_from_index)
    i+=1