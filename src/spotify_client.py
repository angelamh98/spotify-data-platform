import os
import base64
import requests
from dotenv import load_dotenv

from database import (
    insert_artist,
    insert_album,
    insert_track,
    get_artist_by_name
)

from tracks import (
    get_artist_albums,
    get_album_tracks
)

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    return response.json()["access_token"]


def get_auth_header(token):
    return {
        "Authorization": f"Bearer {token}"
    }


def search_artist(token, artist_name):
    headers = get_auth_header(token)

    search_url = "https://api.spotify.com/v1/search"

    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }

    search_response = requests.get(search_url, headers=headers, params=params)
    search_response.raise_for_status()

    search_data = search_response.json()
    items = search_data["artists"]["items"]

    if not items:
        raise ValueError(f"No artist found for: {artist_name}")

    artist_id = items[0]["id"]

    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"

    artist_response = requests.get(artist_url, headers=headers)
    artist_response.raise_for_status()

    artist_data = artist_response.json()

    artist = {
        "id": artist_data["id"],
        "name": artist_data["name"],
        "spotify_url": artist_data["external_urls"]["spotify"],
        "popularity": artist_data.get("popularity"),
        "followers": artist_data.get("followers", {}).get("total"),
        "genres": ", ".join(artist_data.get("genres", []))
    }

    return artist


token = get_token()

artist_name = input("Enter artist name: ")

existing_artist = get_artist_by_name(artist_name)

if existing_artist:
    print("Artist found in database!")

    artist = {
        "id": existing_artist[0],
        "name": existing_artist[1]
    }

else:
    print("Artist not found in database.")
    print("Fetching from Spotify API...")

    artist = search_artist(token, artist_name)

    print(artist)

    insert_artist(artist)

albums = get_artist_albums(token, artist["id"])

print(f"\nFound {len(albums)} albums\n")

for album in albums:
    print(album)

    insert_album(album)

    tracks = get_album_tracks(token, album)

    print(f"Found {len(tracks)} tracks\n")

    for track in tracks:
        print(track)

        insert_track(track)