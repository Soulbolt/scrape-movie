import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status
content = response.text

soup = BeautifulSoup(content, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
print(movie_titles)
