import os
import time
from flask import Flask
from flask import jsonify
from flask_restful import Api
from sqlalchemy.exc import OperationalError
from models.models import db
from views.health_check import HealthCheck
from views.create_product import CreateProduct
from views.get_product import GetProduct
from views.get_products import GetProducts
from views.get_by_category import GetProductsByCategory
from views.update_product import UpdateProduct
from views.delete_product import DeleteProduct
from views.update_inventory import UpdateInventory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify({"status": "OK", "message": "Welcome to the Product Service"})

    DB_USER = os.getenv("MYSQL_USER", "admin")
    DB_PASS = os.getenv("MYSQL_PASSWORD", "password")
    DB_HOST = os.getenv("MYSQL_HOST", "localhost")
    DB_PORT = os.getenv("MYSQL_PORT", "3306")
    DB_NAME = os.getenv("MYSQL_DATABASE", "ims-cloud-db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Initialize database connection without blocking app startup
    def initialize_database():
        with app.app_context():
            retries = 5
            for i in range(retries):
                try:
                    db.create_all()
                    app.logger.info("Database connected and models created.")
                    break
                except OperationalError as e:
                    app.logger.warning(f"Database not ready, retrying ({i+1}/{retries})...")
                    time.sleep(5)
            else:
                app.logger.error("Could not connect to database after several retries.")

    # Use app.app_context() to push the context manually
    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Database connected during startup.")
        except OperationalError as e:
            app.logger.warning("Database not ready during startup, will retry on first request.")
            # Start a thread to keep trying in background
            from threading import Thread
            Thread(target=initialize_database, daemon=True).start()

    api = Api(app)
    api.add_resource(HealthCheck, '/ping')
    api.add_resource(CreateProduct, '/products')
    api.add_resource(GetProduct, '/products/<string:product_id>')
    api.add_resource(GetProducts, '/products')
    api.add_resource(GetProductsByCategory, '/products/category/<string:category>')
    api.add_resource(UpdateProduct, '/products/<string:product_id>')
    api.add_resource(DeleteProduct, '/products/<string:product_id>')
    api.add_resource(UpdateInventory, '/products/<string:product_id>/inventory')

    return app

application = create_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)