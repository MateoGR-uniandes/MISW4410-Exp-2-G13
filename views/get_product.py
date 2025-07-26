from flask_restful import Resource
from services.product_service import ProductService

class GetProduct(Resource):
    def get(self, product_id):
        product = ProductService.get_product_by_id(product_id)
        return product.to_dict() if product else ("Not Found", 404)