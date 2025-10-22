# Blogicum

A full-featured blogging platform built with Django that allows users to create, edit, and share blog posts with images, comments, and categorization.

## 📋 Overview

Blogicum is a comprehensive blogging application that provides a complete platform for content creation and community engagement. Users can publish blog posts with images, organize content by categories and locations, and interact through comments.

## ✨ Features

### Core Functionality
- **Blog Posts**: Create, read, update, and delete blog posts
- **Image Uploads**: Attach images to blog posts
- **Comments**: Full commenting system with CRUD operations
- **Categories**: Organize posts by topic categories
- **Locations**: Tag posts with geographical locations
- **User Profiles**: Customizable user profiles with bio and avatar
- **Scheduled Publishing**: Set future publication dates for posts

### User Management
- User registration and authentication
- Login/logout functionality
- Password reset via email (file-based backend)
- Profile editing
- User-specific post listings

### Content Features
- **Pagination**: 20 posts per page for optimal performance
- **Published/Unpublished**: Control post visibility
- **Comment Count**: Display comment count on posts
- **Author Attribution**: All posts and comments linked to authors
- **Responsive Design**: Bootstrap 5 integration

### Security & Permissions
- Login-required views for creating/editing content
- Author-only editing: Users can only edit their own posts and comments
- CSRF protection
- Published content filtering

## 🛠 Technologies Used

- **Python 3.x**
- **Django 5.2.7**: Web framework
- **SQLite**: Database
- **Pillow 12.0.0**: Image processing
- **django-bootstrap5**: UI framework
- **django-debug-toolbar**: Development debugging

### Development Tools
- **pytest & pytest-django**: Testing framework
- **flake8**: Code linting
- **Faker**: Test data generation
- **mixer**: Model instance generation for tests

## 📁 Project Structure

```
blogicum/
├── blogicum/
│   ├── blog/              # Main blog application
│   │   ├── models.py      # Post, Category, Location, Comment models
│   │   ├── views.py       # Class-based views for all features
│   │   ├── forms.py       # Forms for posts and comments
│   │   └── urls.py        # URL routing
│   ├── core/              # Core functionality
│   │   └── models.py      # Abstract base models
│   ├── pages/             # Static pages (About, Rules)
│   ├── users/             # User management
│   │   └── forms.py       # Custom user forms
│   ├── blogicum/          # Project settings
│   │   ├── settings.py    # Django configuration
│   │   └── urls.py        # Root URL configuration
│   ├── templates/         # HTML templates
│   ├── static_dev/        # Static files (CSS, JS, images)
│   ├── media/             # User-uploaded content
│   ├── manage.py          # Django management script
│   └── db.sqlite3         # SQLite database
├── tests/                 # Test suite
├── requirements.txt       # Python dependencies
├── setup.cfg              # Configuration for tools (flake8, etc.)
└── README.md             # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blogicum
   ```

2. **Create and activate virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to project directory**
   ```bash
   cd blogicum
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📖 Usage

### Creating Content

1. **Register/Login**: Create an account or log in
2. **Create Post**: Click "New Post" to create a blog post
3. **Add Details**: Enter title, text, select category and location
4. **Upload Image**: Optionally attach an image
5. **Set Publication Date**: Choose immediate or scheduled publication
6. **Publish**: Submit to make post live

### Interacting with Posts

- **View Posts**: Browse the homepage for all published posts
- **Filter by Category**: Click on categories to filter posts
- **View Profile**: See all posts by a specific author
- **Add Comments**: Comment on posts (requires login)
- **Edit/Delete**: Manage your own posts and comments

### Admin Panel

Access the Django admin interface to:
- Manage all posts, categories, locations
- Moderate comments
- Manage users
- View and edit all content

## 🗄 Database Models

### Post
- `title`: Post title
- `text`: Post content
- `image`: Optional post image
- `pub_date`: Publication date/time
- `author`: Foreign key to User
- `category`: Foreign key to Category
- `location`: Foreign key to Location
- `is_published`: Publication status
- `created_at`: Creation timestamp

### Comment
- `text`: Comment content
- `post`: Foreign key to Post
- `author`: Foreign key to User
- `created_at`: Creation timestamp

### Category
- `title`: Category name
- `description`: Category description
- `slug`: URL-friendly identifier
- `is_published`: Publication status

### Location
- `name`: Location name
- `is_published`: Publication status

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=blogicum
```

## 🔧 Configuration

### Key Settings (blogicum/settings.py)

- **Language**: Russian (`LANGUAGE_CODE = 'ru-RU'`)
- **Time Zone**: UTC
- **Media Files**: Stored in `media/` directory
- **Static Files**: Served from `static_dev/` in development
- **Debug Mode**: Enabled (disable in production)
- **Allowed Hosts**: `127.0.0.1`, `localhost`

### Email Configuration

Email backend is configured for file-based storage during development:
- Emails saved to: `sent_emails/` directory

## 🎨 Frontend

- **Bootstrap 5**: Responsive design framework
- **Custom Templates**: Jinja2-style Django templates
- **Static Assets**: CSS, JavaScript, and images in `static_dev/`
- **Media Uploads**: User-uploaded images stored in `media/posts_images/`

## 🔐 Security Features

- CSRF protection enabled
- Password validation
- Login required for content creation
- Author-based permissions
- Secure file uploads

## 📝 Development

### Code Quality Tools

- **flake8**: PEP 8 style guide enforcement
- **pep8-naming**: Naming convention checks
- **flake8-docstrings**: Docstring convention checks
- **yapf**: Code formatter

Run linting:
```bash
flake8
```

### Debug Toolbar

Django Debug Toolbar is enabled for development at:
- Internal IP: `127.0.0.1`

Access toolbar panels for:
- SQL queries
- Template rendering
- Cache usage
- Request/response details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django framework and community
- Bootstrap for UI components
- All contributors and testers

## 📞 Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Made with ❤️ using Django**
