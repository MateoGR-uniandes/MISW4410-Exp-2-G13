from flask import request
from flask_restful import Resource
from services.product_service import ProductService

class UpdateInventory(Resource):
    def patch(self, product_id):
        data = request.json
        if "quantity" not in data:
            return {"message": "Missing quantity"}, 400
        product = ProductService.update_inventory(product_id, data["quantity"])
        return product.to_dict() if product else ("Not Found", 404)