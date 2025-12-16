from flask import Blueprint, request

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.get("")
def list_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@users_bp.get("/<name>")
def get_user(name: str):
    return {"user": name}

@users_bp.post("")
def create_user():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return {"error": "name is required"}, 400
    return {"created": {"name": name}}, 201
