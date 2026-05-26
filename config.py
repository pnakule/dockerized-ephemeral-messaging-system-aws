import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "msql"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "Ephemeral@0."),
    "database": os.getenv("DB_NAME", "ephemeraldb")
}
