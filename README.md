![## Steam Video Game Recommendation Project](Data\logo-henry-white-lg.png)

# Steam Video Game Recommendation Project

## Problem
Context: As a data scientist at Steam, a multinational video game platform, we are faced with the challenge of creating a video game recommendation system for users. Our recommendation model has shown promising metrics, but now we need to bring it to the real world and face problems with data maturity and lack of process automation.

Role: As a data scientist at Steam, our mission is to design a video game recommendation system that meets the needs of users and the company. The project encompasses everything from data collection and processing to machine learning model training and maintenance.

## Work Proposal
ETL (Extract, Transform, Load)

Transformations: In this MVP, we focused on reading the dataset in the correct format and removing unnecessary columns to optimize the API and model training.
Feature engineering: We created the sentiment_analysis column by applying sentiment analysis with NLP to user reviews. The values are 0 (bad), 1 (neutral), or 2 (positive). If analysis is not possible, 1 is assigned.
API development (FastAPI)

We propose exposing the data through an API using the FastAPI framework. The queries we implemented include:

1. developer(developer: str): Returns the number of items and the percentage of free content by year by developer.

2. userdata(User_id: str): Provides information on the money spent by the user, the recommendation percentage, and the number of items.

3. best_developer_year(year: int): Returns the top 3 developers with the MOST user-recommended games for the given year.

4. developer_reviews_analysis(developer: str): Provides statistics on user reviews categorized as positive or negative for a developer.

## Deployment

The deployment is done on Render, which allows the API to be accessible from any device with an internet connection.

## Exploratory Data Analysis (EDA)

EDA focuses on investigating relationships between variables, detecting outliers, and exploring interesting patterns in the dataset. The analysis includes generating word clouds to understand the most frequent words in game titles.

## Machine Learning Model

The machine learning model is able to recommend games to users:

User-Item Recommendation System: Takes a user and returns a list of recommended games for that user.
Project
Repository: The repository was verified to contain appropriate file names and an organized structure. The README.md provides a clear guide to the project.
Requirements compliance: It was checked whether the approval requirements mentioned in the work proposal were met.
Presentation Video
A video with a maximum duration of 7 minutes is essential to demonstrate the operation of the API and explain the machine learning model used.

# Conclusion

The approved MVP is ready to be consumed through RENDER and meets all of the mentioned criteria. This project allowed us to showcase our skills in ETL, FastAPI, EDA, and machine learning.