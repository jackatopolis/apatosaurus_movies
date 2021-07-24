import requests as req
from bs4 import BeautifulSoup

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