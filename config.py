import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    """Application settings loaded from environment variables where possible."""

    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-before-deployment")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'instance' / 'biorisk.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
