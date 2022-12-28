import pandas as pd
from pandas import read_csv
import requests
from functools import reduce
from bs4 import BeautifulSoup

def map(list, function):
    for i in range(len(list)):
        list[i] = function(list[i])
    return list

#созданный список
old_list = ['1', '2', '3', '4', '5']
new_list = list(map(old_list, int))
for i in range(len(new_list)):
    new_list[i] = new_list[i] + 5
print(new_list)

#датасет
arr_people = []
table_countries = pd.read_csv('country.csv', sep=',')
arr_people = table_countries['people'].tolist()
print("Количество людей в странах: ", reduce(lambda a, x: a + x, arr_people, 0))

#парсинг
arr_filma_score = []
url = 'https://www.kinoafisha.info/rating/movies/2022/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
filma_score = soup.find_all('span', class_='rating_num')
for i in filma_score:
    arr_filma_score.append(i.text)
print("Количество фильмов с оценкой 7.0: ", reduce(lambda a, x: a + x.count('7.0'), arr_filma_score, 0))
