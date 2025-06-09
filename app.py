# Fichier app/app.py

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
from config import Config
app.config.from_object(Config)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle SQLAlchemy
class Membre(db.Model):
    __tablename__ = 'membre'

    id = db.Column(db.Integer, primary_key=True)  # PostgreSQL gère l'auto-incrément
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    father_id = db.Column(db.Integer, db.ForeignKey('membre.id'), nullable=True)
    mother_id = db.Column(db.Integer, db.ForeignKey('membre.id'), nullable=True)

    birth_date = db.Column(db.Text)
    death_date = db.Column(db.Text)
    birth_place = db.Column(db.Text)
    residence = db.Column(db.Text)
    external_link = db.Column(db.Text)
    image_url = db.Column(db.Text)
    mother = db.Column(db.Text)
    has_offspring = db.Column(db.Boolean)
    alive = db.Column(db.Boolean)
    death_reason = db.Column(db.Text)
    died_in_battle = db.Column(db.Boolean)
    known_enemies = db.Column(db.Text)
    fitan = db.Column(db.Text)
    notes = db.Column(db.Text)
    photo_url = db.Column(db.Text)
    gender = db.Column(db.Text)

    # Relations possibles (optionnelles)
    father = db.relationship('Membre', remote_side=[id], foreign_keys=[father_id], post_update=True, backref='enfants_du_pere')
    mother = db.relationship('Membre', remote_side=[id], foreign_keys=[mother_id], post_update=True, backref='enfants_de_la_mere')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/membres')
def api_membres():
    membres = Membre.query.all()
    data = []
    for m in membres:
        data.append({
            "id": m.id,
            "name": f"{m.first_name} {m.last_name}",
            "firstName": m.first_name,
            "lastName": m.last_name,
            "parentIds": list(filter(None, [m.father_id, m.mother_id]))
        })
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

