from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://spotify_user:spotify_password@localhost:5433/spotify_db"

engine = create_engine(DATABASE_URL)


def insert_artist(artist):
    query = text("""
        INSERT INTO artists (
            id,
            name,
            spotify_url,
            popularity,
            followers,
            genres
        )
        VALUES (
            :id,
            :name,
            :spotify_url,
            :popularity,
            :followers,
            :genres
        )
        ON CONFLICT (id) DO NOTHING
    """)

    with engine.connect() as connection:
        connection.execute(query, artist)
        connection.commit()

    print(f"Artist '{artist['name']}' inserted successfully!")


def insert_album(album):
    query = text("""
        INSERT INTO albums (
            id,
            artist_id,
            name,
            release_date,
            total_tracks,
            spotify_url
        )
        VALUES (
            :id,
            :artist_id,
            :name,
            :release_date,
            :total_tracks,
            :spotify_url
        )
        ON CONFLICT (id) DO NOTHING
    """)

    with engine.connect() as connection:
        connection.execute(query, album)
        connection.commit()

    print(f"Album '{album['name']}' inserted successfully!")


def insert_track(track):
    query = text("""
        INSERT INTO tracks (
            id,
            artist_id,
            album_id,
            name,
            popularity,
            duration_ms,
            explicit,
            spotify_url
        )
        VALUES (
            :id,
            :artist_id,
            :album_id,
            :name,
            :popularity,
            :duration_ms,
            :explicit,
            :spotify_url
        )
        ON CONFLICT (id) DO NOTHING
    """)

    with engine.connect() as connection:
        connection.execute(query, track)
        connection.commit()

    print(f"Track '{track['name']}' inserted successfully!")


def get_artist_by_name(artist_name):
    query = text("""
        SELECT *
        FROM artists
        WHERE LOWER(name) = LOWER(:name)
    """)

    with engine.connect() as connection:
        result = connection.execute(query, {"name": artist_name})
        artist = result.fetchone()

    return artist