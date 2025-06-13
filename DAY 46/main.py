import requests
from bs4 import BeautifulSoup
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify credentials from environment variables
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")  # Use http://localhost:8888/callback or None

# Ask user for date
date = input("Enter the date in YYYY-MM-DD: ")

# Billboard URL for the given date
URL = f"https://www.billboard.com/charts/hot-100/{date}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

# Fetch the webpage
response = requests.get(URL, headers=headers)
response.raise_for_status()

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Select the song titles - updated CSS selector for Billboard 2025
# (If this selector breaks, inspect the Billboard page again)
all_songs = soup.select("li.o-chart-results-list__item h3#title-of-a-story")

# Clean up song names text
hundred_songs = [song.get_text(strip=True) for song in all_songs]

print(f"Found {len(hundred_songs)} songs on Billboard for {date}")

# Spotify scope
scope = "playlist-modify-private playlist-modify-public"

# Setup Spotify OAuth
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI or "http://localhost:8888/callback",  # fallback URI
    scope=scope,
    open_browser=True,
    cache_path="token.txt"
)

# Get token info
token_info = sp_oauth.get_access_token(as_dict=True)
access_token = token_info['access_token']

# Create Spotify client
sp = Spotify(auth=access_token)

# Get current user id
user_id = sp.current_user()["id"]
print(f"Logged in as user: {user_id}")

# Create a new private playlist
playlist_name = f"Billboard Hot 100 - {date}"
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f"Billboard Hot 100 songs from {date}"
)
print(f"Created playlist: {playlist_name}")

# Extract the year for search queries
year = date.split("-")[0]

song_uris = []

print("Searching for songs on Spotify and collecting URIs...")
for song in hundred_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    tracks = result.get("tracks", {}).get("items", [])
    if tracks:
        uri = tracks[0]["uri"]
        song_uris.append(uri)
        print(f"Added: {song}")
    else:
        print(f"Skipped (not found): {song}")

# Add songs to the playlist in batches of 100 (Spotify limit per request)
print(f"Adding {len(song_uris)} songs to the playlist...")
for i in range(0, len(song_uris), 100):
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris[i:i+100])

print("All songs added to playlist successfully!")
