# Agent Instructions for `chipanda`

This document provides instructions for an AI development agent to understand and contribute to the `chipanda` project.

## 1. Project Overview

`chipanda` is a web application built with the Django framework.

**The main goal of the application is to serve as a real estate platform where users can list, search, and view properties available for rent or purchase, complete with features like photos, detailed descriptions, and agent contact information.**

## 2. Technology Stack

* **Backend Framework:** Django (Preference: Django for backend/APIs)
* **Programming Language:** Python
* **Database:** SQLite (for development)
* **Environment Management:** `django-environ` for `.env` management.
* **Frontend Styling:** **Tailwind CSS CLI** for compiling styles.

## 3. Project Structure

The project follows a modular Django layout. Global templates are housed within the project configuration app (`chipanda/`).

```
chipanda/
├── .env 
├── .env-example
├── accounts/       # User registration and agent profiles
├── chipanda/       # Project configuration & Global Templates
│   ├── templates/  # Base templates (e.g., base.html)
│   ├── settings.py 
│   ├── urls.py     # Root URL configuration
│   └── ...
├── home/           # Main landing page
├── listings/       # Property listings core
│   ├── templates/  # App-specific templates
│   ├── models.py   # Property model with dynamic __str__
│   ├── admin.py    # Tailored admin interface
│   └── ...
├── manage.py
└── requirements.txt

```

## 4. Key Files

* `chipanda/settings.py`: Includes `listings`, `accounts`, and **`chipanda`** itself in `INSTALLED_APPS` to enable global template discovery.
* `listings/models.py`: Defines the `Property` model. Note: Does **not** use `title` or `description` fields; it generates a string representation dynamically from property details.
* `requirements.txt`: Current dependencies: `Django`, `django-environ`.

## 5. How to Run the Project (VS Code Debug)

1. **Environment Setup:**
* Create/Activate venv: `python -m venv venv`
* `pip install -r requirements.txt`
* `cp .env-example .env` (Then update your `SECRET_KEY`).
* `npm install` (For Tailwind CSS).


2. **Database:**
* `python manage.py migrate`


3. **Run (VS Code):**
* Open the **Debug/Run panel** (`Ctrl+Shift+D`).
* Run **"Python Debugger: Django"** and **"Tailwind CLI Watcher"**.



## 6. Development Goals & Tasks

* [X] **Create core apps:** `accounts`, `home`, and `listings`.
* [X] **Define Property Model:** Localized fields (province, city, toilet_type) + dynamic `__str__`.
* [X] **Set up Admin Interface:** Customized `PropertyAdmin`.
* [X] **Create Views for Listings:** CBVs (`ListView`, `DetailView`) implemented.
* [X] **Configure URLs:** Routing connected at app and project levels.
* [X] **Build Templates:** `base.html` and listing templates using Tailwind CSS.
* [ ] **Set up Static Files:** Configure media/static settings for images and CSS.
* [ ] **Develop User Authentication:** Complete the `accounts` app.
