from flask import Flask
from config import Config
from models import db
from blueprints.main import main_bp
from blueprints.api import api_bp

def create_app():
    app = Flask(__name__,template_folder='templates', static_folder='static')
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
