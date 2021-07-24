import requests as req
from bs4 import BeautifulSoup
from config import api_key

# Scrape top 50 movies for each year between 1980-2020
attr1 = {"class":"a-text-left mojo-field-type-release mojo-cell-wide"}
all_movies = {}

for j in range(1980,2021):
    url = f'https://www.boxofficemojo.com/year/{j}/?grossesOption=calendarGrosses'
    r1 = req.get(url)
    soups = BeautifulSoup(r1.content, features="lxml")
    hello = soups.find_all('td',attr1)
    movies = []
    for i in range(50):
        movie = hello[i].text
        movies.append(movie)
    all_movies[j]=movies
    
    
url = f"http://www.omdbapi.com/?apikey={api_key}&t="
