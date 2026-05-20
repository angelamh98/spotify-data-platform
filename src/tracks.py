import requests


def get_artist_albums(token, artist_id):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    albums = []

    limit = 10
    offset = 0

    while True:

        url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"

        params = {
            "limit": limit,
            "offset": offset
        }

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            print("Spotify albums request failed")
            print("Status code:", response.status_code)
            print("URL:", response.url)
            print("Response:", response.text)

        response.raise_for_status()

        data = response.json()

        for album in data["items"]:

            album_data = {
                "id": album["id"],
                "artist_id": artist_id,
                "name": album["name"],
                "release_date": album["release_date"],
                "total_tracks": album["total_tracks"],
                "spotify_url": album["external_urls"]["spotify"]
            }

            albums.append(album_data)

        if data["next"] is None:
            break

        offset += limit

    return albums


def get_album_tracks(token, album):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    tracks = []

    limit = 50
    offset = 0

    while True:

        url = f"https://api.spotify.com/v1/albums/{album['id']}/tracks"

        params = {
            "limit": limit,
            "offset": offset
        }

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            print("Spotify tracks request failed")
            print("Status code:", response.status_code)
            print("URL:", response.url)
            print("Response:", response.text)

        response.raise_for_status()

        data = response.json()

        for track in data["items"]:

            track_artist_ids = [
                artist["id"]
                for artist in track["artists"]
            ]

            if album["artist_id"] not in track_artist_ids:
                continue

            track_data = {
                "id": track["id"],
                "artist_id": album["artist_id"],
                "album_id": album["id"],
                "name": track["name"],
                "duration_ms": track["duration_ms"],
                "explicit": track["explicit"],
                "spotify_url": track["external_urls"]["spotify"],
                "popularity": None
            }

            tracks.append(track_data)

        if data["next"] is None:
            break

        offset += limit

    return tracks