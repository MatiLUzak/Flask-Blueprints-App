from flask import Flask
from config import Config
from models import db
from models.datapoint import DataPoint

def create_app():
    app = Flask(__name__,template_folder='templates', static_folder='static')
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    @app.route('/')
    def hello_world():  # put application's code here
       return 'Hello World!'

    return app


if __name__ == '__main__':
    app=create_app()
    app.run()
