from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Blueprints
    from .routes.health_routes import health_bp
    app.register_blueprint(health_bp)

    return app
