from django.shortcuts import render
import requests

# Create your views here.

def get_movies_data():

    for i in range(1, 4):
        URL = 'https://api.themoviedb.org/3/movie/popular'
        params = {'language': 'ko-KR', 'page': i}
        headers = {'accept': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZGIzMmNlYzFjMTM0NGNjMzlmZWQ1N2MxZTI5MGFiNCIsInN1YiI6IjYzZDMxYmE2MDMxYTFkMDA4M2EwOTFlYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Lor3ESAInBSsko8e9uaQusOBVJ_DOxZY6gAfUAfWPM4'}
    
        res = requests.get(URL, params=params, headers=headers).json()
        print(res['results'])
        print('---------------------------------------------------------------------')