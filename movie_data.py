#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:14:16 2021

@author: jackcohen
"""
import requests as req
from movie_list import all_movies
from config import api_key
import csv

movie_data = {}

for year in all_movies.keys():
    movie_data = {}
    for movie in all_movies[year]:
        url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie}"
        data = req.get(url).json()
        movie_data[movie] = data
        all_movies[year] = movie_data

