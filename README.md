# MovieLens API

## 📌 Overview
MovieLens API is a backend service built with Django and Django REST Framework (DRF) that provides functionalities for managing movie data, user authentication, and ticket booking.

## 🚀 Features
- User authentication (Login, Logout, Token-based authentication)
-Movie data retrieval (CRUD operations, post ratings, and tags)
- API documentation with Swagger

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Authentication:** JWT (JSON Web Token)
- **Database:** PostgreSQL / SQLite (configurable)
- **API Documentation:** drf-yasg (Swagger)

## 📥 Installation & Setup
### 1️⃣ Clone the repository
```bash
git clone https://github.com/SaiRaghav26/movielens_api.git
cd movielens_api
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply database migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server
```bash
python manage.py runserver
```

## 📖 API Documentation
Once the server is running, you can access the API documentation:
- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## 🔑 Authentication
- **Login:** `POST /api/login/`
- **Logout:** `POST /api/logout/`
- **JWT Authentication:** Access and Refresh tokens are used.

## 🛠️ Running Tests
To run tests, use:
```bash
python manage.py test
```

## 🛠️ Deployment
You can deploy the API using Docker or a cloud platform like AWS, Heroku, or Render. Additional configurations might be required.

## 📜 License
This project is licensed under the MIT License.

---
Feel free to contribute and improve this API! 🚀

