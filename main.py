# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Reading the data
data = pd.read_csv("players_stats_by_season_full_details.csv")

# Creating the "images" folder if it does not exist
os.makedirs("images", exist_ok=True)

# Questions and graphs:

# Qualitative Question 1: Which nationalities produce the tallest players on average?
nationality_avg_height = data.groupby('nationality')['height_cm'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
nationality_avg_height.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Nationalities with Tallest Players (Average Height)')
plt.ylabel('Average Height (cm)')
plt.xlabel('Nationality')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/qualitative_q1.png')
plt.close()

# Follow-Up: How do the heights of players from these nationalities compare in boxplot form?
top_nationalities = nationality_avg_height.index
data_filtered = data[data['nationality'].isin(top_nationalities)]
plt.figure(figsize=(12, 6))
sns.boxplot(data=data_filtered, x='nationality', y='height_cm', palette='viridis')
plt.title('Height Distribution by Nationality (Top 10)')
plt.ylabel('Height (cm)')
plt.xlabel('Nationality')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/qualitative_q1_followup.png')
plt.close()

# Qualitative Question 2: Which teams consistently draft the heaviest players?
draft_team_avg_weight = data.groupby('draft_team')['weight_kg'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
draft_team_avg_weight.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Top 10 Teams Drafting the Heaviest Players')
plt.ylabel('Average Weight (kg)')
plt.xlabel('Draft Team')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/qualitative_q2.png')
plt.close()

# Follow-Up: What are the weight distributions of players drafted by these teams?
top_draft_teams = draft_team_avg_weight.index
data_filtered_teams = data[data['draft_team'].isin(top_draft_teams)]
plt.figure(figsize=(12, 6))
sns.boxplot(data=data_filtered_teams, x='draft_team', y='weight_kg', palette='coolwarm')
plt.title('Weight Distribution by Draft Team (Top 10)')
plt.ylabel('Weight (kg)')
plt.xlabel('Draft Team')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/qualitative_q2_followup.png')
plt.close()

# Quantitative Question 1: Is there a correlation between minutes played (MIN) and points scored (PTS)?
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='MIN', y='PTS', alpha=0.6, edgecolor=None)
plt.title('Correlation between Minutes Played and Points Scored')
plt.xlabel('Minutes Played (MIN)')
plt.ylabel('Points Scored (PTS)')
plt.tight_layout()
plt.savefig('images/quantitative_q1.png')
plt.close()

# Follow-Up: How does this correlation vary across leagues?
plt.figure(figsize=(12, 6))
sns.lmplot(data=data, x='MIN', y='PTS', hue='League', scatter_kws={'alpha':0.5}, height=6, aspect=1.5)
plt.title('Correlation between Minutes Played and Points Scored by League')
plt.xlabel('Minutes Played (MIN)')
plt.ylabel('Points Scored (PTS)')
plt.tight_layout()
plt.savefig('images/quantitative_q1_followup.png')
plt.close()

# Quantitative Question 2: What is the relationship between height and weight?
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='height_cm', y='weight_kg', alpha=0.6, color='green', edgecolor=None)
plt.title('Relationship between Height and Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.tight_layout()
plt.savefig('images/quantitative_q2.png')
plt.close()

# Quantitative Question 3: Which season had the highest average points scored by players?
season_avg_points = data.groupby('Season')['PTS'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
season_avg_points.plot(kind='bar', color='purple', edgecolor='black')
plt.title('Top 10 Seasons with Highest Average Points Scored')
plt.ylabel('Average Points (PTS)')
plt.xlabel('Season')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/quantitative_q3.png')
plt.close()

# Follow-Up: How did the average points trend over all seasons?
season_avg_points_all = data.groupby('Season')['PTS'].mean()
plt.figure(figsize=(12, 6))
season_avg_points_all.plot(color='red')
plt.title('Average Points Scored by Season (Trend)')
plt.ylabel('Average Points (PTS)')
plt.xlabel('Season')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/quantitative_q3_followup.png')
plt.close()
