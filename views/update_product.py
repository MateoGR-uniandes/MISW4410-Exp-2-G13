from flask import request
from flask_restful import Resource
from services.product_service import ProductService

class UpdateProduct(Resource):
    def put(self, product_id):
        data = request.json
        product = ProductService.update_product(product_id, data)
        return product.to_dict() if product else ("Not Found", 404)