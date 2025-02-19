# Movie Rating API

## 📌 Overview
A Django REST Framework-based API for managing movies, tags, and ratings. Users can register, log in, and rate movies while filtering by genres and tags.

## 🚀 Features
- User authentication (Register & Login with JWT)
- CRUD operations for Movies, Ratings, and Tags
- Filtering and ordering support
- Average movie rating calculation
- Interactive API documentation using Swagger

---

## 🔧 Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/movie-rating-api.git
cd movie-rating-api
```

### 2️⃣ **Create and Activate a Virtual Environment**
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Configure the Database** (MySQL, PostgreSQL, or SQLite)
Modify `settings.py` to match your database configuration. Example for MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moviedb',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ **Run Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ **Create a Superuser** (For Admin Panel)
```sh
python manage.py createsuperuser
```

### 7️⃣ **Run the Development Server**
```sh
python manage.py runserver
```
Visit: **http://127.0.0.1:8000/**

---

## 🔑 Authentication

### **Register a User**
```sh
POST /api/register/
```
**Payload:**
```json
{
  "username": "testuser",
  "password": "securepassword"
}
```

### **Login to Get JWT Token**
```sh
POST /api/login/
```
**Payload:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```
**Response:**
```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```
Use the `access` token in the `Authorization` header for protected endpoints:
```sh
Authorization: Bearer jwt_access_token
```

---

## 📜 API Endpoints

### 🎬 **Movies**
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/movies/` | List all movies with tags & average rating |
| GET | `/api/movies/{id}/` | Retrieve a specific movie |
| POST | `/api/movies/` | Add a new movie |
| PATCH | `/api/movies/{id}/` | Update movie details |
| DELETE | `/api/movies/{id}/` | Delete a movie |

### ⭐ **Ratings**
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/ratings/` | Add a movie rating |

### 🔖 **Tags**
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/tags/` | Add a new tag |

---

## 📄 API Documentation
### **Swagger UI:**  
👉 **http://127.0.0.1:8000/swagger/**

### **ReDoc:**  
👉 **http://127.0.0.1:8000/redoc/**

---

## 🛠️ Troubleshooting

### **Port Already in Use**
Run the server on a different port:
```sh
python manage.py runserver 8001
```

### **Database Errors**
Ensure MySQL is running, or delete existing migrations:
```sh
rm -rf migrations/__pycache__
python manage.py makemigrations
python manage.py migrate
```

### **Invalid JWT Token**
Ensure the token is included in the `Authorization` header:
```sh
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## 🏗️ Future Enhancements
- User roles & permissions
- Movie recommendations
- Enhanced filtering

💡 **Contributions are welcome!** 🚀

