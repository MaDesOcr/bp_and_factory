from flask import Flask, request

app = Flask(__name__)

# All routes live in a single file (works for tiny apps, not great for scaling).

@app.get("/")
def index():
    return {"message": "Hello from single-file app"}

@app.get("/users")
def list_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.get("/users/<name>")
def get_user(name: str):
    return {"user": name}

@app.post("/users")
def create_user():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return {"error": "name is required"}, 400
    # For teaching purposes: not persisted
    return {"created": {"name": name}}, 201

if __name__ == "__main__":
    app.run(debug=True)
