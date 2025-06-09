# Fichier app/app.py
import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'family.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Membre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    father_id = db.Column(db.Integer, db.ForeignKey('membre.id'))
    mother_id = db.Column(db.Integer, db.ForeignKey('membre.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": f"{self.first_name} {self.last_name}",
            "parentIds": list(filter(None, [self.father_id, self.mother_id]))
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/membres')
def api_membres():
    membres = Membre.query.all()

    return jsonify([m.to_dict() for m in members])

if __name__ == '__main__':
    app.run()

