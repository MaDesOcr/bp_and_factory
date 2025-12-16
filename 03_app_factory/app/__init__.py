from flask import Flask, jsonify
from .config import Config
from .routes.users import users_bp
from .routes.products import products_bp

def create_app(config_object=None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object or Config)

    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    return app
