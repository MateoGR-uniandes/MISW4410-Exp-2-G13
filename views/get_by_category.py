from flask_restful import Resource
from services.product_service import ProductService

class GetProductsByCategory(Resource):
    def get(self, category):
        products = ProductService.get_products_by_category(category)
        return [p.to_dict() for p in products], 200