import pandas as pd

from database import engine


query = """
SELECT
    artists.name AS artist,
    tracks.name AS track,
    tracks.duration_ms,
    tracks.explicit
FROM tracks
JOIN artists
ON tracks.artist_id = artists.id
"""

df = pd.read_sql(query, engine)

print(df.head())

print("\nTotal tracks:")
print(len(df))

print("\nTracks per artist:")
print(df["artist"].value_counts())