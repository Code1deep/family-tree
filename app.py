# Fichier app/app.py

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/family.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle SQLAlchemy
class Membre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    father_id = db.Column(db.Integer, db.ForeignKey('membre.id'))
    mother_id = db.Column(db.Integer, db.ForeignKey('membre.id'))

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

