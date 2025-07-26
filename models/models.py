from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import CHAR
import uuid

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "product_id": str(self.product_id),
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }