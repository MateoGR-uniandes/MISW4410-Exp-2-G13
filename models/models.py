from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import CHAR
import uuid

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    pid = db.Column(db.Integer, primary_key=True)
    productcode = db.Column(db.String(45), nullable=False)
    productname = db.Column(db.String(45), nullable=False)
    costprice = db.Column(db.Float, nullable=False)
    sellprice = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {
            "pid": str(self.pid),
            "productcode": self.productcode,
            "productname": self.productname,
            "costprice": self.costprice,
            "sellprice": self.sellprice,
            "brand": self.brand
        }