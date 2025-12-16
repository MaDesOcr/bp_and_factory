from flask import Flask
from users import users_bp

app = Flask(__name__)

# Register the blueprint (routes moved out of app.py)
app.register_blueprint(users_bp)

@app.get("/")
def index():
    return {"message": "Hello from app + blueprint"}

if __name__ == "__main__":
    app.run(debug=True)
