# Spotify Data Platform

A Spotify-based data engineering project built with Python, PostgreSQL, Docker, and the Spotify Web API.

The platform incrementally ingests artist and track data from Spotify, transforms API responses into structured datasets, and stores the information in a relational PostgreSQL database.

---

# Overview

This project simulates a real-world data ingestion pipeline:

```text
User Input
    ↓
Spotify API
    ↓
Python ETL Pipeline
    ↓
Data Transformation
    ↓
PostgreSQL (Docker)
```

The system checks whether an artist already exists in the database before calling the Spotify API, reducing unnecessary API requests and simulating incremental ingestion strategies used in production systems.

---

# Features

- Spotify API authentication
- Token-based API requests
- Incremental artist ingestion
- Relational PostgreSQL schema
- Artist and track storage
- SQLAlchemy database integration
- Dockerized PostgreSQL infrastructure
- JSON transformation pipelines
- SQL joins and relational queries

---

# Tech Stack

- Python
- PostgreSQL
- Docker
- SQLAlchemy
- Spotify Web API
- dotenv

---

# Database Schema

## artists

```sql
CREATE TABLE artists (
    id TEXT PRIMARY KEY,
    name TEXT,
    spotify_url TEXT,
    popularity INTEGER,
    followers INTEGER,
    genres TEXT
);
```

## tracks

```sql
CREATE TABLE tracks (
    id TEXT PRIMARY KEY,
    artist_id TEXT REFERENCES artists(id),
    name TEXT,
    popularity INTEGER,
    duration_ms INTEGER,
    explicit BOOLEAN,
    spotify_url TEXT
);
```

---

# Project Structure

```text
spotify-data-platform/
│
├── src/
│   ├── spotify_client.py
│   ├── database.py
│   └── tracks.py
│
├── data/
├── notebooks/
├── tests/
│
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# Running PostgreSQL with Docker

```bash
docker compose up -d
```

---

# Running the Pipeline

Activate virtual environment:

```bash
source venv/bin/activate
```

Run the application:

```bash
python src/spotify_client.py
```

---

# Example SQL Query

```sql
SELECT
    artists.name AS artist,
    tracks.name AS track
FROM tracks
JOIN artists
ON tracks.artist_id = artists.id;
```

---

# Future Improvements

- Album ingestion
- Audio features ingestion
- Pandas analytics layer
- Streamlit dashboards
- Automated ETL jobs
- Recommendation systems
- Machine learning models
- AI-powered music insights

---

# Author

Angela Martin Herrera

GitHub:
https://github.com/angelamh98