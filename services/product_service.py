from models.models import Product
from repository.product_repository import ProductRepository
import uuid

class ProductService:

    @staticmethod
    def create_product(data):
        product = Product(
            product_id=uuid.uuid4(),
            name=data["name"],
            description=data.get("description"),
            category=data["category"],
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )
        return ProductRepository.create_product(product)

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_products_by_category(category):
        return ProductRepository.get_products_by_category(category)

    @staticmethod
    def update_product(product_id, data):
        product = ProductRepository.get_product_by_id(product_id)
        if not product:
            return None

        if "name" in data:
            product.name = data["name"]
        if "description" in data:
            product.description = data["description"]
        if "category" in data:
            product.category = data["category"]
        if "price" in data:
            product.price = float(data["price"])
        if "quantity" in data:
            product.quantity = int(data["quantity"])

        return ProductRepository.update_product(product)

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.get_product_by_id(product_id)
        if product:
            ProductRepository.delete_product(product)
            return True
        return False

    @staticmethod
    def update_inventory(product_id, quantity):
        return ProductRepository.update_inventory(product_id, quantity)