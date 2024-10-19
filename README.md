# Farasite Custom CMS

## Project Overview
This project is a custom CMS (Content Management System) developed for managing multiple websites based on their domain names. It also includes a **Telegram bot** for handling **Contact Us** requests and introducing the company. The project is built with **Django** and features dynamic menus, content management, and sections like statistics, partners, FAQs, branches, news, articles, galleries, and more.

### Key Features
- **Domain-Based Management**: Each website is managed based on its domain.
- **Telegram Bot**: A Telegram bot for managing Contact Us requests and introducing the company.
- **Dynamic Menus**: Menus are dynamically sorted and displayed based on priorities.
- **Content Sections**: Includes sections like statistics, partners, FAQs, branches, news, articles, galleries, and more.
- **REST API**: Built using Django REST Framework for handling server-side operations.

## Requirements
To run this project, you need:

- **Python 3.9+**
- **Django 3.2**
- **PostgreSQL** (or any supported database)
- **Docker** and **Docker Compose** (for containerized deployment)

### Python Dependencies
```plaintext
Django==3.2
djangorestframework==3.12.4
pandas==1.5.3
requests==2.31.0
django-dbbackup==3.3.0
django-cors-headers==3.12.0
django-summernote==0.8.20.0
django-colorfield==0.7.2
django-tinymce==3.4.0
python-dateutil==2.8.2
persiantools==1.6.0
gunicorn==20.1.0
dj-database-url==1.0.0
python-dotenv==1.0.0
opencv-python==4.8.0.76
reportlab==3.6.12
arabic-reshaper==2.1.1
python-bidi==0.4.2
GuardPyCaptcha==1.0.1
decouple==3.8
