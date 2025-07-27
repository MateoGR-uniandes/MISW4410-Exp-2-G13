import os
import time
from flask import Flask
from flask_restful import Api
from sqlalchemy.exc import OperationalError
from models.models import db
from views.health_check import HealthCheck
from views.create_product import CreateProduct

def create_app():
    app = Flask(__name__)


    DB_USER = os.getenv("MYSQL_USER", "root")
    DB_PASS = os.getenv("MYSQL_PASSWORD", "my-secret-pw")
    DB_HOST = os.getenv("MYSQL_HOST", "localhost")
    DB_PORT = os.getenv("MYSQL_PORT", "3306")
    DB_NAME = os.getenv("MYSQL_DATABASE", "inventory")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        retries = 5
        for i in range(retries):
            try:
                db.create_all()
                print("[INFO] Database connected and models created.")
                break
            except OperationalError as e:
                print(f"[WARN] Database not ready, retrying ({i+1}/{retries})...")
                time.sleep(5)
        else:
            print("[ERROR] Could not connect to database after several retries.")
            raise

    api = Api(app)
    api.add_resource(HealthCheck, '/ping')
    api.add_resource(CreateProduct, '/products')
    
    return app

if __name__ == "__main__":
    application = create_app()
    application.run(debug=True, host="0.0.0.0", port=5000)