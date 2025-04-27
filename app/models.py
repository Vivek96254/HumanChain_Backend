from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialize extensions (but don't bind them yet)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind extensions to app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from app.routes import incident_bp
    app.register_blueprint(incident_bp)

    return app

# models.py
from datetime import datetime
from . import db

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'severity': self.severity,
            'reported_at': self.reported_at.isoformat()
        }
