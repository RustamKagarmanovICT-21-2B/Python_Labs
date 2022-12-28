import requests
from bs4 import BeautifulSoup
from sklearn import datasets
from functools import reduce


num_list = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, num_list)))
print(reduce(lambda x, y: x + y, num_list))


url = "https://perm.kinoafisha.info/cinema/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
all_cinemas_names = soup.find_all(class_="cinemaList_name")
cinemas = []
for item in all_cinemas_names:
    item_name = item.text
    cinemas.append(item_name)
print(list(map(lambda x: "Кинотеатр " + x,cinemas)))
print(reduce(lambda x, y: x +" " + y, cinemas))


iris = datasets.load_iris()
names_list = list(iris.target_names)

print(list(map(lambda x: "Name " + x , names_list)))
print(reduce(lambda x, y: x +" " + y, names_list))