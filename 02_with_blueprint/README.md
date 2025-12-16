# 02 — Same app, refactored with a Blueprint

## What changed?
- `users` routes moved to `users.py`
- `app.py` only creates the app + registers the blueprint

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Routes
- GET  `/`
- GET  `/users`
- GET  `/users/<name>`
- POST `/users`
