# Myaba Media Tech - Professional Media & ICT Solutions

[![Django](https://img.shields.io/badge/Django-5.0.6-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 About

Myaba Media Tech is a comprehensive ICT, media, and publishing company serving the Nkangala District Municipality and beyond. We specialize in web development, graphic design, news publishing through The Highveld Chronicle, and innovative digital solutions.

## ✨ Features

- **Responsive Web Design** - Mobile-first, professional layouts
- **Dynamic Content Management** - Easy-to-update service offerings
- **Contact Management** - Professional contact forms with email integration
- **SEO Optimized** - Search engine friendly structure
- **Performance Optimized** - Fast loading times and efficient caching
- **Security Enhanced** - Production-ready security configurations

## 🛠️ Tech Stack

- **Backend**: Django 5.0.6
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with responsive design
- **Deployment**: Render.com with WhiteNoise for static files
- **Email**: SMTP integration for contact forms

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/myabamedia-.git
cd myabamedia-
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Setup
Create a `.env` file in the root directory:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Database Setup
```bash
python manage.py migrate
python manage.py collectstatic
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## 📁 Project Structure

```
myabamedia-/
├── mediaApp/                 # Main Django application
│   ├── templates/           # HTML templates
│   ├── migrations/          # Database migrations
│   ├── views.py            # View controllers
│   ├── models.py           # Data models
│   ├── forms.py            # Form definitions
│   └── urls.py             # URL routing
├── myabamediatech/          # Django project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── static/                  # Static assets
│   ├── css/                # Stylesheets
│   └── images/             # Images and media
├── staticfiles/            # Collected static files
├── requirements.txt        # Python dependencies
├── runtime.txt            # Python version for deployment
└── manage.py              # Django management script
```

## 🌐 Deployment

### Production Environment Variables
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:password@host:port/database
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
EMAIL_HOST_USER=your-production-email
EMAIL_HOST_PASSWORD=your-production-password
```

### Deploy to Render.com
1. Connect your GitHub repository
2. Set environment variables in Render dashboard
3. Deploy with automatic builds on push

## 📧 Contact Configuration

The application uses Gmail SMTP for contact form submissions. Configure your email settings:

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password
3. Use the App Password in your environment variables

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Code Style
We follow PEP 8 guidelines. Use flake8 for linting:
```bash
flake8 .
```

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📱 Features Overview

### Pages
- **Home**: Dynamic hero section with rotating content
- **About**: Company information and history
- **Services**: Detailed service offerings with images
- **Contact**: Professional contact form with validation

### Services Offered
- Web Development & Design
- Graphic Design & Branding
- News Publishing (The Highveld Chronicle)
- System Design & Modeling
- Digital Marketing Solutions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Email**: info@myabamediatech.com
- **Phone**: +27 81 410 9337
- **Address**: 29 Geldenhuys, Delmas

## 🙏 Acknowledgments

- Django community for the excellent framework
- Font Awesome for icons
- Google Fonts for typography
- All our clients and community members

---

**Myaba Media Tech** - *Connecting communities and empowering businesses in the Nkangala District Municipality and beyond.*
