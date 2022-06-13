import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = f"https://www.billboard.com/charts/hot-100/{travel_date}"
CLIENT_ID = "{your_client_id}"
CLIENT_SECRET = "{your_client_secret}"
REDIRECT_URL = "http://example.com"
SCOPE = "playlist-modify-private"
USERNAME = "Halaszraymond"
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="h3", class_="a-no-trucate")
song_titles = [song.getText().strip("\t\n") for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope=SCOPE,
        username=USERNAME,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = travel_date.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, Skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{travel_date} Billboard 100",
    public=False,
)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris,
)


