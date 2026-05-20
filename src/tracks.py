import requests


def get_artist_tracks(token, artist_id):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"

    params = {
        "include_groups": "album",
        "limit": 3
    }

    response = requests.get(
        albums_url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    albums_data = response.json()

    tracks = []

    for album in albums_data["items"]:

        album_id = album["id"]

        tracks_url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"

        tracks_response = requests.get(
            tracks_url,
            headers=headers
        )

        tracks_response.raise_for_status()

        tracks_data = tracks_response.json()

        for track in tracks_data["items"]:

            track_data = {
                "id": track["id"],
                "artist_id": artist_id,
                "name": track["name"],
                "duration_ms": track["duration_ms"],
                "explicit": track["explicit"],
                "spotify_url": track["external_urls"]["spotify"],
                "popularity": None
            }

            tracks.append(track_data)

    return tracks