# BookStore

Full-stack Book Store application — a FastAPI + PostgreSQL backend with two
React frontends (admin panel and user shop).

## Projects

| Folder | Description | Stack |
|--------|-------------|-------|
| `./` (repository root) | Backend REST API | FastAPI, SQLAlchemy, PostgreSQL |
| `BookStore-Frontend_admin-main` | Admin panel | React (Create React App) |
| `BookStore-Frontend_user-main` | User shop | React (Create React App) |

## Quick Start

### 1. Backend

The backend lives at the **repository root** (folders `app/`, files
`requirements.txt`, `run.py`).

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set your real `DATABASE_URL`
(see the backend `README.md` for details):

```
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DBNAME
```

Run the server:

```bash
python run.py
# or: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs

### 2. Frontends

```bash
# Admin panel
cd BookStore-Frontend_admin-main/BookStore-Frontend_admin-main
npm install
npm start

# User shop
cd BookStore-Frontend_user-main/BookStore-Frontend_user-main
npm install
npm start
```

Set `REACT_APP_API_URL` to your backend URL when deploying
(defaults to `http://127.0.0.1:8000` for local development).
