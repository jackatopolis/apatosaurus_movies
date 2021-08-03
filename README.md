# Project 1 - Ideal Movie Characteristics
#### By: Team Apatosaurus (Jack Cohen (PM), Novak Radovic, Swapnali Mehta)
#### August 3, 2021

## Abstract
The goal of this project is to analyze information from the top box office revenue movies from years 1980-2020 to find trends in the data that would help a producer today create a movie with characteristics that maximize the chance it generates the largest revenue possible. Movie characteristics include genre, runtime, MPAA rating, and release month. It was found that to maximize revenue in 2021, a movie should include genres sci-fi, adventure, and animation, have a runtime between 145-155 minutes, have an MPAA rating PG-13, and be released in May or December.

## Background
Movie producers need to make decisions about what movies to make in order to maximize their revenue. Variables like genre, runtime, MPAA rating, and release month affect the box office revenue and metascore ratings, essentially dictating the movie’s success. The next logical question is: What are the ideal movie characteristics that maximize revenue?

To answer this question, the team took the top 50 box office revenue movies from the Box Office Mojo website using BeautifulSoup, then used the OMDB API to obtain relevant information on these movies. The movie information data was then cleaned by removing movies that had missing information. After that, the data was processed to find the revenue per movie each variable generates. Using trends over the past 40/20/10/5 years, the team was able to find the top revenue per movie producing genres, runtime, MPAA rating, and release month.

## Analysis

By first creating a correlation heatmap with Seaborn, we can see that there are some little correlations between runtime, ratings, and box office revenue. It is clear that no one variable will maximize movie revenue on its own. Therefore it is important to consider all variables and create various hypotheses.

### Hypotheses
Longer movie runtimes produce better IMDB score and metascore, which then produce more box office revenue. Long runtimes allow for more complex plots and plot twists.
Comedy, action, drama, and adventure are the largest revenue producing genres. Adventure movies will increase over time, as people require more stimulus and plot twists to be satisfied with a movie.
Movies with a PG-13 rating will be most popular and generate more revenue, since they are more accessible to a larger population.
The best time to release the movie is in June or December, since schools have summer/winter break and have more free time to go to the theaters.

### Null Hypothesis
Movie runtimes have no influence on IMDB score, metascore, or box office revenue.
No genre correlates with increased revenue
Movies without a PG-13 rating will be most popular and generate more revenue
There is no best month to release a movie

### Genre
The team found the genres that produced the most revenue per movie for each year and the genres that appeared in the most movies each year, then used this data to create a histogram of the most frequently appearing movie genres for the past 40/20/10/5 years. Looking at data from 1980-2020 and 2000-2020, it is clear that comedy is the most frequently appearing genre, followed by adventure/drama/action. This trend changes in the past 5/10 years, where adventure becomes the most frequent. Analyzing the revenue per movie for each genre, it’s clear that Sci-Fi is the genre that produces the most revenue per movie, regardless of the timeframe.

### Runtime
After plotting movie Runtimes against IMDB score, metascore, and box office revenue, the correlation is clear. All of the P-values are very small which makes them statistically significant and support our alternate hypothesis that longer runtimes lead to increased revenue and more favorable ratings. The graphs of different movie group runtimes clearly demonstrate that movies between 145-155 minutes are the most profitable.

### Movie Release Month
Regarding movie release month, the data shows that releasing movies in May and December yield the most profit, since that is when they make the most money and the market is not too saturated as it is in June or July. 

### MPAA Ratings
The team looked at the frequency of R, PG-13, PG, G rated movies through the years and concluded that the number of R-rated movies dropped significantly, while the number of PG-13 movies increased to the point where they make up most of the top revenue generating movies. As a result, the team concluded that to increase the chance of generating the most revenue, the movie should be rated PG-13 movies in order to reach a broader audience.

## Conclusion

Ideal characteristics a movie should have to maximize revenue in 2021 are:
Genres: Sci-Fi, Adventure, Animation
Runtime: 145 to 155 minutes
Release month: May or December
MPAA Rating: PG-13

## Improvements and Limitations

While the data used provided significant insights to the movie industry, there are limitations to the research that could be improved to increase the efficacy of the analysis. These limitations include:
No budget information, no profitability information; revenue can be large, but is insignificant if no cost is taken into account
Box office records only go back to 1977
Some movies didn’t have records in the OMDB APIs
Look at other revenue streams and not just the Box Office revenue
