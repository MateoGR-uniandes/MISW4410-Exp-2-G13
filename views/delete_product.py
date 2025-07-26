from flask_restful import Resource
from services.product_service import ProductService

class DeleteProduct(Resource):
    def delete(self, product_id):
        success = ProductService.delete_product(product_id)
        return ("Deleted", 204) if success else ("Not Found", 404)