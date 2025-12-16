from flask import Blueprint, jsonify

products_bp = Blueprint("products", __name__, url_prefix="/api/v1/products")

@products_bp.get("")
def list_products():
    return jsonify(items=[{"id": 10, "name": "Keyboard"}, {"id": 11, "name": "Mouse"}])
