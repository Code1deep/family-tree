# app/config.py
import os

class Config:
    # Utilisez SQLite par défaut (plus simple pour commencer)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'family.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'votre-cle-secrete-ici'