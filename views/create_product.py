from flask import request
from flask_restful import Resource
from services.product_service import ProductService
from sqlalchemy.exc import IntegrityError


class CreateProduct(Resource):
    def post(self):
        data = request.json
        required = ["productcode", "productname", "costprice", "sellprice", "brand"]
        missing = [f for f in required if f not in data]
        if missing:
            return {"message": f"Missing fields: {', '.join(missing)}"}, 400

        try:
            product = ProductService.create_product(data)
            return product.to_dict(), 201
        except IntegrityError:
            return None, 412
        except Exception as e:
            return {"message": str(e)}, 500