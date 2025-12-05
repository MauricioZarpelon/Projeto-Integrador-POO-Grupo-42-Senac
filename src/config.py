# src/config.py

import os

class Config:
    SECRET_KEY = "Miracles29#"  # pode ser qualquer string
    SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
