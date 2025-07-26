from models.models import db, Product
from sqlalchemy.exc import SQLAlchemyError

class ProductRepository:

    @staticmethod
    def create_product(product):
        try:
            db.session.add(product)
            db.session.commit()
            return product
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_products_by_category(category):
        return Product.query.filter_by(category=category).all()

    @staticmethod
    def update_product(product):
        try:
            db.session.commit()
            return product
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_product(product):
        try:
            db.session.delete(product)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_inventory(product_id, quantity):
        product = Product.query.get(product_id)
        if product:
            product.quantity = quantity
            try:
                db.session.commit()
                return product
            except SQLAlchemyError as e:
                db.session.rollback()
                raise e
        return None