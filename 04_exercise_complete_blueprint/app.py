from flask import Flask
from books import books_bp

app = Flask(__name__)
app.register_blueprint(books_bp)

@app.get("/")
def index():
    return {"message": "Blueprint exercise: Books API"}

if __name__ == "__main__":
    app.run(debug=True)
