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