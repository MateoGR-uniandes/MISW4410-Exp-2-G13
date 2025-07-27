from models.models import Product
from repository.product_repository import ProductRepository
import uuid

class ProductService:

    @staticmethod
    def create_product(data):
        product = Product(
            productcode=["productcode"],
            productname=data["productname"],
            brand=data.get("brand"),
            costprice=float(data["costprice"]),
            sellprice=float(data["sellprice"])
        )

        return ProductRepository.create_product(product)

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def update_product(product_id, data):
        product = ProductRepository.get_product_by_id(product_id)
        if not product:
            return None

        if "productcode" in data:
            product.productcode = data["productcode"]
        if "productname" in data:
            product.productname = data["productname"]
        if "brand" in data:
            product.brand = data["brand"]
        if "costprice" in data:
            product.costprice = float(data["costprice"])
        if "sellprice" in data:
            product.sellprice = float(data["sellprice"])

        return ProductRepository.update_product(product)

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.get_product_by_id(product_id)
        if product:
            ProductRepository.delete_product(product)
            return True
        return False

    @staticmethod
    def update_costs(product_id, costprice, sellprice):
        return ProductRepository.update_costs(product_id, costprice, sellprice)