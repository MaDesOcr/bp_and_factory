# 01 — Single-file Flask app (no blueprint)

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Routes
- GET  `/`
- GET  `/users`
- GET  `/users/<name>`
- POST `/users`  body: `{"name": "Dave"}`
