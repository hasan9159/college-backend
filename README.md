# College Management API ⚙️

A simple Django + Django REST Framework project to manage students, courses, and enrollments.

---

## ✅ Features

- CRUD for Students, Courses, and Enrollments
- Enrollment timestamp and unique constraint (student + course)
- Admin site enabled
- Ready for environment-based configuration via `.env`

---

## 🔧 Requirements

Install the project dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ⚙️ Environment

Create your local `.env` from the provided example:

```bash
cp .env.example .env
# then edit `.env` and set a secure SECRET_KEY and any DB settings
```

Note: `.env` is listed in `.gitignore` by default — **do not commit** your real `.env`.

If you want Django to read the `.env` values, install `django-environ` (already in `requirements.txt`) and add something like this at the top of `college/settings.py`:

```python
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}
```

I can update `settings.py` to use `django-environ` if you'd like.

Alternatively, `settings.py` currently reads Postgres values with `os.getenv`. You can set these variables in your `.env` if you prefer:

```
DB_NAME=college_db
DB_USER=postgres
DB_PASSWORD=admin123
DB_HOST=localhost
DB_PORT=5432
```

If you store these values in `.env`, make sure the file is loaded before Django reads settings. Install `python-dotenv` (already in `requirements.txt`) and add at the top of `college/settings.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

This will allow `os.getenv('DB_NAME')` and similar calls to work as expected.

---

## 🚀 Quick start (development)

```bash
# apply migrations
python manage.py migrate

# create a superuser
python manage.py createsuperuser

# run dev server
python manage.py runserver
```

---

## 📡 API Endpoints

- `GET /api/students/` — list students
- `POST /api/students/` — create student
- `GET /api/students/{id}/` — retrieve a student
- `PUT/PATCH/DELETE /api/students/{id}/` — update / delete

- `GET /api/courses/` — list courses
- `POST /api/courses/` — create course
- `GET /api/courses/{id}/` — retrieve a course

- `GET /api/enrollments/` — list enrollments
- `POST /api/enrollments/` — create enrollment
- `GET /api/enrollments/{id}/` — retrieve enrollment

---

## 🔐 Next improvements (suggestions)

- Add authentication + permissions (Token or JWT)
- Add filtering, searching, and pagination
- Add tests and CI configuration
- Configure production-ready settings (WhiteNoise, allowed hosts, secure secrets)

---

If you'd like, I can also:
- Update `settings.py` to read from `.env` (I can do that now),
- Add tests and CI config,
- Or generate a `requirements.txt` from your virtualenv (pip freeze) if you prefer exact pins.
