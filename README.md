# 🚀 Django REST API - Python Machine Test

A complete Django REST API system for managing Users, Clients, and Projects with full CRUD operations and authentication.

## 📋 Features

- **👥 User Management**: Django's built-in User model with admin panel
- **🏢 Client Management**: Full CRUD operations via REST API
- **📋 Project Management**: Create projects and assign multiple users
- **🔐 Authentication**: Session-based authentication for secure API access
- **📊 Admin Interface**: Django admin panel for easy data management
- **🚀 REST API**: Full REST API with JSON input/output

## 🛠️ Tech Stack

- **Django 5.1.5**: Web framework
- **Django REST Framework 3.15.0**: REST API framework
- **SQLite**: Database (can be easily changed to PostgreSQL for production)
- **WhiteNoise**: Static file serving
- **Gunicorn**: WSGI server for production

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd django_api
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create admin user**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Home page: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API base: http://127.0.0.1:8000/api/

## 📚 API Documentation

### Authentication
All API endpoints require authentication. Use session authentication or basic authentication.

### Clients API

#### List all clients
```http
GET /api/clients/
```

#### Create a new client
```http
POST /api/clients/
Content-Type: application/json

{
  "client_name": "Example Client"
}
```

#### Get client details
```http
GET /api/clients/{id}/
```

#### Update client (full update)
```http
PUT /api/clients/{id}/
Content-Type: application/json

{
  "client_name": "Updated Client Name"
}
```

#### Update client (partial update)
```http
PATCH /api/clients/{id}/
Content-Type: application/json

{
  "client_name": "Updated Client Name"
}
```

#### Delete client
```http
DELETE /api/clients/{id}/
```

### Projects API

#### List user's projects
```http
GET /api/projects/
```

#### Create project for client
```http
POST /api/clients/{client_id}/projects/
Content-Type: application/json

{
  "project_name": "Example Project",
  "users": [1, 2, 3]
}
```

## 🏗️ Project Structure

```
django_api/
├── django_api/          # Main project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI application
├── home/                # Home app
│   ├── views.py         # Home page views
│   └── templates/       # HTML templates
├── clients/             # Clients app
│   ├── models.py        # Client model
│   ├── views.py         # Client API views
│   ├── serializers.py   # Client serializers
│   ├── urls.py          # Client URLs
│   └── admin.py         # Client admin
├── projects/            # Projects app
│   ├── models.py        # Project model
│   ├── views.py         # Project API views
│   ├── serializers.py   # Project serializers
│   ├── urls.py          # Project URLs
│   └── admin.py         # Project admin
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel deployment config
└── README.md           # This file
```

## 🌐 Deployment

### Vercel Deployment

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy to Vercel**
   ```bash
   vercel
   ```

3. **Set environment variables in Vercel dashboard**
   - `DJANGO_SETTINGS_MODULE=django_api.settings`
   - `SECRET_KEY=your-secret-key`

### Other Platforms

The project can be deployed to any platform that supports Python/Django:
- Heroku
- Railway
- DigitalOcean App Platform
- AWS Elastic Beanstalk

## 🔧 Configuration

### Environment Variables

Create a `.env` file for local development:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database

The project uses SQLite by default. For production, consider using PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🧪 Testing

### Manual Testing

1. **Create test users via admin panel**
2. **Test API endpoints using curl or Postman**
3. **Verify authentication works correctly**

### Example API Tests

```bash
# Get all clients
curl -X GET http://127.0.0.1:8000/api/clients/

# Create a client
curl -X POST http://127.0.0.1:8000/api/clients/ \
  -H "Content-Type: application/json" \
  -d '{"client_name": "Test Client"}'

# Create a project
curl -X POST http://127.0.0.1:8000/api/clients/1/projects/ \
  -H "Content-Type: application/json" \
  -d '{"project_name": "Test Project", "users": [1]}'
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the Django documentation
2. Review the API documentation above
3. Create an issue in the repository

---

**🎯 Ready for Vercel Deployment!** This Django REST API project is fully configured for deployment on Vercel and other cloud platforms. 