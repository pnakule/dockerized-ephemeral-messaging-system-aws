# NOTE:
# Default values are included only for local/demo purposes.
# Production credentials should be managed securely using environment variables or secret management solutions.

import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "msql"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "Ephemeral@0."),
    "database": os.getenv("DB_NAME", "ephemeraldb")
}
