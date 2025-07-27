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
    def get_product_by_id(pid):
        return Product.query.get(pid)

    @staticmethod
    def get_all_products():
        return Product.query.all()

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
    def update_costs(pid, costprice, sellprice):
        product = Product.query.get(pid)
        if product:
            product.costprice = costprice
            product.sellprice = sellprice
            try:
                db.session.commit()
                return product
            except SQLAlchemyError as e:
                db.session.rollback()
                raise e
        return None