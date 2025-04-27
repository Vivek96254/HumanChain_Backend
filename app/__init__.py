from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

# Initialize extensions (but don't bind them yet)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # app = Flask(__name__)
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)

    CORS(app)

    # Bind extensions to app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from app.routes import incident_bp
    app.register_blueprint(incident_bp)

    SWAGGER_URL = '/docs'  # URL to access Swagger UI
    API_URL = '/static/swagger.yaml'  # Path to your swagger.yaml

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={ 
            'app_name': "HumanChain Incident Log API"
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    return app