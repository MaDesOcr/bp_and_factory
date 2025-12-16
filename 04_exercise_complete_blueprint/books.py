from flask import Blueprint, request

# Fake in-memory "database" for the exercise.
BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt & David Thomas"},
]

# TODO 1: Implement GET /books  -> return {"items": BOOKS}
# TODO 2: Implement GET /books/<int:book_id> -> return {"item": book} or 404
# TODO 3: Implement POST /books with JSON body {"title": "...", "author": "..."} -> validate, append, return 201
# TODO 4 (bonus): Implement DELETE /books/<int:book_id> -> delete or 404

# Tips:
# - use request.get_json(silent=True) or {}
# - return (dict, status_code)
# - choose the next id with max(...) + 1
