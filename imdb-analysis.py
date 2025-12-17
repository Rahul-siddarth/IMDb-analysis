import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("movies.csv")


df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')


df['IMDB_Rating'] = pd.to_numeric(df['IMDB_Rating'], errors='coerce')


df = df.dropna(subset=['Released_Year', 'IMDB_Rating'])

# flitering for movies releases after 2000
df = df[df['Released_Year'] > 2000]
# Movies released per year
movies_per_year = df.groupby('Released_Year').size().reset_index(name='Count')

# Sort by rating top 10 movies
top10 = df.sort_values(by="IMDB_Rating", ascending=False).head(10)

# Spliting genres
df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre')

# Group by genre mean rating
genre_stats = (
    df.groupby('Genre')['IMDB_Rating']
    .mean()
    .reset_index(name='mean_rating')
    .sort_values(by='mean_rating', ascending=False)
)



# Most frequent directors
# Split directors if multiple are listed
df['Director'] = df['Director'].str.split(', ')
df = df.explode('Director')

director_counts = (
    df['Director']
    .value_counts()
    .reset_index()
    )
director_counts.columns = ['Director', 'Count']


# IMDb Rating Distribution

plt.hist(df['IMDB_Rating'], bins=20, color='coral', edgecolor='black')
plt.title('IMDb Rating Distribution')
plt.xlabel('IMDb Rating')
plt.ylabel('Number of Movies')
plt.grid(axis='y', alpha=0.75)
plt.show()

# IMDb Rating vs Number of Votes correalation

plt.scatter(df['IMDB_Rating'], df['No_of_Votes'], color='teal')
plt.title('IMDb Rating vs Number of Votes')
plt.xlabel('IMDb Rating')
plt.ylabel('Number of Votes (in millions)')
plt.grid()
plt.show()


# Top 10 Movies by IMDb Rating

plt.barh(top10['Series_Title'], top10['IMDB_Rating'], color='skyblue')
plt.title('Top 10 Movies by IMDb Rating (After 2000)')
plt.xlabel('IMDb Rating')
plt.gca().invert_yaxis()
plt.show()

# most frequent directors

plt.barh(director_counts['Director'].head(10), director_counts['Count'].head(10), color='lightgreen')
plt.title('Top 10 Most Frequent Directors (After 2000)')
plt.xlabel('Number of Movies Directed')
plt.gca().invert_yaxis()
plt.show()

# avg IMDb Rating by Genre

plt.barh(genre_stats['Genre'], genre_stats['mean_rating'], color='orchid')
plt.title('Average IMDb Rating by Genre (After 2000)')
plt.xlabel('Average IMDb Rating')
plt.gca().invert_yaxis()
plt.show()

# Movies Released per Year (after 2000)

plt.plot(movies_per_year['Released_Year'], movies_per_year['Count'], marker='o', color='orange')
plt.title('Movies Released per Year (After 2000)')
plt.xlabel('Year')
plt.ylabel('Number of Movies Released (in hundreds)')
plt.xticks(movies_per_year['Released_Year'])
plt.grid()
plt.show()

# Meta Score vs IMDb Rating correlation

plt.scatter(df['Meta_score'], df['IMDB_Rating'], color='purple')
plt.title('Meta Score vs IMDb Rating')
plt.xlabel('Meta Score')
plt.ylabel('IMDb Rating')
plt.grid()
plt.show()

