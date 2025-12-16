from flask import Blueprint, request, jsonify

users_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")

@users_bp.get("")
def list_users():
    return jsonify(items=[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])

@users_bp.post("")
def create_user():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify(error="name is required"), 400
    return jsonify(created={"id": 3, "name": name}), 201
