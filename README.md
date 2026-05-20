# Spotify Data Platform

A data engineering project built with Python, PostgreSQL, Docker, and the Spotify API.

This project extracts artist data from Spotify, transforms the JSON responses, and stores the information in a PostgreSQL database running inside Docker.

---

# Tech Stack

- Python
- PostgreSQL
- Docker
- SQLAlchemy
- Spotify Web API
- dotenv

---

# Architecture

```text
Spotify API
     ↓
Python ETL Pipeline
     ↓
PostgreSQL (Docker)
```

---

# Features

- Authenticate with Spotify API
- Generate access tokens automatically
- Search artists dynamically
- Transform JSON responses
- Store artist data in PostgreSQL
- Dockerized PostgreSQL database
- Modular Python structure

---

# Project Structure

```text
spotify-data-platform/
│
├── src/
│   ├── spotify_client.py
│   └── database.py
│
├── data/
├── notebooks/
├──