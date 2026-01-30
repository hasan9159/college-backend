# College Management API ⚙️


## 🔧 Requirements

Install the project dependencies:

```bash
pip install -r requirements.txt
```



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

