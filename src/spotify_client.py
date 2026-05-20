import os
import base64
import requests
from dotenv import load_dotenv

from database import insert_artist

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
    print(artist_data)

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

artist = search_artist(token, artist_name)

print(artist)

insert_artist(artist)