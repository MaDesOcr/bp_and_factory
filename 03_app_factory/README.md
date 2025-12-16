# 03 — Application Factory + Blueprints

## Run
```bash
pip install -r requirements.txt
flask --app wsgi run --debug
```

## Why app factory?
- cleaner structure
- easier configuration (dev/test/prod)
- easier testing

## Routes
- GET `/health`
- GET `/api/v1/users`
- POST `/api/v1/users`
- GET `/api/v1/products`
