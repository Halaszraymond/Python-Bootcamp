import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in all_movies]
movies = movies[::-1]

with open("movies.txt", "w") as movies_file:
    for movie in movies:
        movies_file.write(f"{movie}\n")



