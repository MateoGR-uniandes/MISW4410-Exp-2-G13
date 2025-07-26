from flask_restful import Resource
from services.product_service import ProductService

class GetProducts(Resource):
    def get(self):
        products = ProductService.get_all_products()
        return [p.to_dict() for p in products], 200