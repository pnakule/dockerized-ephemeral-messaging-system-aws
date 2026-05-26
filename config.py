import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "xyz"),
    "user": os.getenv("DB_USER", "xyz"),
    "password": os.getenv("DB_PASSWORD", "xyz"),
    "database": os.getenv("DB_NAME", "xyz")
}
