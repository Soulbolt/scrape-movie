import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status
content = response.text
# Store websites content
soup = BeautifulSoup(content, "html.parser")
# Get movie titles
movie_titles = soup.find_all(name="h3", class_="title")

# For loop to create file if it does not exist and add movie tiles on reverse to view titles from 1-100 into a txt file.
for title in reversed(movie_titles):
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(title.getText()+"\n")
