# Basketball Players Stats Analysis

This project analyzes basketball player statistics over multiple seasons, exploring both qualitative and quantitative aspects of the dataset. We leverage Python libraries like `pandas`, `matplotlib`, and `seaborn` to process and visualize the data.

---

## Dataset Overview

The dataset, `players_stats_by_season_full_details.csv`, contains detailed statistics for basketball players, including:

- **Performance Stats**: Points (PTS), Rebounds (REB), Assists (AST), etc.
- **Player Attributes**: Height, Weight, Nationality, Birth Year, etc.
- **Team and League Details**: Team, League, Season, and Draft information.

### Libraries Used
- `pandas` for data manipulation
- `matplotlib` and `seaborn` for visualization

---

## Questions and Analysis

### 1. **Qualitative Question 1**
**Question**: Which countries have the most players represented in the dataset?  
**Follow-Up**: How has the representation of players from the top three countries changed over time?

**Graphs**:
- **Bar Chart**: Number of players by nationality.
- **Line Chart**: Trends of player representation over seasons for the top three countries.

**Insights**:
- The United States dominates the dataset with 19,009 players, followed by Serbia (2,491), Croatia (1,483), Lithuania (1,284), and Spain (1,278).
- Players from Serbia, Croatia, and Lithuania tend to have slightly higher average heights compared to players from the United States, highlighting regional differences in player profiles.
- Over time, the representation of players from the United States has consistently increased, with the steepest rise post-2017. In contrast, Serbia and Croatia have seen moderate but steady growth.

---

### 2. **Qualitative Question 2**
**Question**: What is the distribution of players’ height across the dataset?  
**Follow-Up**: Are there differences in height distribution by league?

**Graphs**:
- **Histogram**: Height distribution for all players.
- **Box Plot**: Height distribution for players across different leagues.

**Insights**:
- The average height across players is approximately 197 cm, and the average weight is 95.4 kg.
- Players from Croatia and Serbia are the tallest on average, with heights around 199.8 cm and 199.6 cm, respectively.
- Players from Spain have the lowest average height (197.3 cm) and weight (94.2 kg) among the top five nationalities.

---

### 3. **Qualitative Question 3**
**Question**: Which teams had the highest average points per player in a season?  
**Follow-Up**: How does team performance in points relate to other metrics like assists or rebounds?

**Graphs**:
- **Bar Chart**: Teams with the highest average points per player.
- **Scatter Plot**: Relationship between average points, assists, and rebounds.

**Insights**:
- Points (PTS), Rebounds (REB), and Assists (AST) are strongly correlated, with coefficients of 0.71 to 0.76.
- Blocks (BLK) have a moderate correlation with rebounds (0.77), suggesting taller players who excel in rebounding often contribute to blocking as well.
- Steals (STL) and assists (AST) show a strong relationship (0.74), indicating that players who frequently handle the ball tend to create opportunities for teammates.

---

### 4. **Quantitative Question 1**
**Question**: How does player scoring vary by position (if available)?  
**Follow-Up**: Are certain positions more dominant in different leagues?

**Graphs**:
- **Box Plot**: Scoring variation by position.
- **Stacked Bar Chart**: Scoring contribution by position for each league.

**Insights**:
- The dataset shows a wide variance in points scored, ranging from 0 to 2,832 in a single season.
- The median player scores around 247 points per season, indicating a skewed distribution where a few players contribute disproportionately to scoring.

---

### 5. **Quantitative Question 2**
**Question**: How do player performance metrics like points, rebounds, and assists correlate with each other?  
**Follow-Up**: Is there a noticeable pattern in correlation across different seasons?

**Graphs**:
- **Heatmap**: Correlation matrix for key metrics.
- **Line Chart**: Changes in correlation values over seasons.

**Insights**:
- Drafted players tend to perform better on average. The first-round picks have significantly higher scoring and rebounding statistics compared to later rounds.
- The average draft pick in the dataset is 14th, with a standard deviation of 8.6, highlighting the distribution of players' draft positions.

---

### 6. **Quantitative Question 3**
**Question**: What is the average age of players in the dataset?  
**Follow-Up**: How has the average age changed over time?

**Graphs**:
- **Histogram**: Age distribution for all players.
- **Line Chart**: Average age of players over time.

**Insights**:
- The average birth year is 1986, making the players in the dataset around 39 years old in 2025.
- Younger players (born post-2000) increasingly contribute to the dataset, indicating the sport’s evolving talent pipeline.

---

## How to Run the Project

1. **Install Required Libraries**:
   ```bash
   pip install pandas matplotlib seaborn
   ```

2. **Run the Script**:
   ```bash
   python3 main.py
   ```

3. **Generated Outputs**:
   - All graphs are saved as PNG files in the `images/` folder.

---

## Future Improvements

- Add interactive visualizations using `plotly` or `dash`.
- Explore player trends based on draft details or high school data.
- Conduct predictive analysis to estimate player performance.
